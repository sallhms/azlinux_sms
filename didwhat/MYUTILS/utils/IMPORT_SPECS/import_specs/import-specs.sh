#!/bin/bash

set -e

function clean_up {
    echo "====== Cleaning up ======"

    if [[ -d "$DOWNLOAD_DIR" ]]
    then
        rm -rf "$DOWNLOAD_DIR"
    fi
}
trap clean_up EXIT SIGINT SIGTERM

expand_srpms() {
    local import_srpm_dir=$1
    local build_spec_dir=$2
    local logs_dir=$3
    local tools_dir
    local srpms

    tools_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." >/dev/null 2>&1 && pwd )"

    srpms=$(find "$import_srpm_dir" -type f -name '*.src.rpm')
    for srpm_file in $srpms; do
        spec_name=$(rpm -qp "$srpm_file" --define='with_check 1' --queryformat '%{NAME}/%{NAME}.spec' 2>/dev/null)
        spec_destination=$build_spec_dir/$spec_name
        spec_dir=$(dirname "$spec_destination")
        srpm_log="$logs_dir/$spec_name.log"
        srpm_log_dir=$(dirname "$srpm_log")

        mkdir -p "$spec_dir"
        mkdir -p "$srpm_log_dir"

        echo "Extracting $spec_destination"
        cd "$spec_dir" && rpm2cpio "$srpm_file" | cpio -idvu &>"$srpm_log" || echo "Failed to expand $srpm_file"

        if ! "$tools_dir/sanitize_specs/sanitize_specs.sh" "$spec_destination"
        then
            found_errors=1
        fi
    done

    if [[ -n $found_errors ]]
    then
        echo "WARNING: finished with errors, check logs above." >&2
    fi
}

print_usage() {
    echo "Usage:"
    echo "import-specs.sh [distro] [package list file]"
    echo
    echo "Supported distros: fedora, centos, opensuse"
    echo
    echo "Example: import-specs.sh fedora /path/to/packagelist.txt"
    exit
}

if [ -z "$2" ]; then
    print_usage
fi

DISTRO=$1
PACKAGE_LIST=$2

SCRIPT_DIR="$(cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd)"
OUTPUT_DIR="$SCRIPT_DIR/output/$DISTRO"
LOGS_DIR="$OUTPUT_DIR/logs"
SPECS_DIR="$OUTPUT_DIR/specs"
IMAGE_TAG="$DISTRO-srpm-importer"

DOWNLOAD_DIR="$(mktemp -d)"

mkdir -p "$LOGS_DIR"
mkdir -p "$SPECS_DIR"


cp "$PACKAGE_LIST" "$DOWNLOAD_DIR/packagelist.txt"

echo "====== Preparing Docker image ======"
docker build -t "$IMAGE_TAG" -f "$SCRIPT_DIR/container/$DISTRO.Dockerfile" "$SCRIPT_DIR/container"

echo "====== Retrieving source RPMs ======"
docker run -v "$DOWNLOAD_DIR":/srpms --rm "$IMAGE_TAG"

echo "====== Expanding retrieved source RPMs ======"
expand_srpms "$DOWNLOAD_DIR" "$SPECS_DIR" "$LOGS_DIR"

echo "SPECs written to $SPECS_DIR"
