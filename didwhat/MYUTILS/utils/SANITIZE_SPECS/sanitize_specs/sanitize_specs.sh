#!/bin/bash

# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

shopt -s globstar

SCRIPT_DIR="$( cd "$(dirname "$0")" && pwd )"

source "$SCRIPT_DIR/binary_paths_mapping"
source "$SCRIPT_DIR/package_name_mapping"

add_vendor_info() {
    sed -i '1s;^;Vendor:         Microsoft Corporation\nDistribution:   Azure Linux\n;' "$1"
}

check_args() {
    if [ -z "$1" ]; then
        echo "Must provide at least one directory or spec file path. See instructions below." >&2
        print_usage
        exit 1
    fi

    for file_path in "$@"
    do
        if [[ -d "$file_path" ]]
        then
            continue
        fi

        if [[ ! -f "$file_path" ]]
        then
            echo "Path \"$file_path\" doesn't exist. See instructions below." >&2
            print_usage
            exit 1
        fi

        if [[ ! $file_path =~ \.spec$ ]]
        then
            echo "WARNING: path \"$file_path\" is neither a directory nor a file with the '.spec' extension. Assuming it's a spec file." >&2
        fi
    done
}

print_usage() {
    echo "Usage:"
    echo "sanitize_specs.sh spec_or_dir_path1 [spec_or_dir_path2] ..."
    echo
    echo "Example: sanitize all *.spec files inside a directory".
    echo "   sanitize_specs.sh SPECS"
    echo
    echo "Example: sanitize a specific *.spec file."
    echo "   sanitize_specs.sh SPECS/mailx/mailx.spec"
}

sanitize_binary_paths() {
    local binary_paths_count
    local found_unknown_paths
    local original_path
    local path_to_fix_regex
    local replacement_path
    local spec_path

    spec_path="$1"

    # The regex looks for lines to replace, but ignores comments, changelog entries (they start with "*" or "-"), and "Provides" tags.
    path_to_fix_regex="^(?"'!'"\s*(Provides|[-#*]))(.*)((?<"'!'"[a-zA-Z0-9])$BINARY_PATHS_REGEX)\b(?"'!'"[-_])"

    # Checking all (Build)Requires for known paths. We expect to know all paths before we attempt any clean-up.
    for original_path in $(grep -oP "^(Build)?Requires(\([^)]+\))?:.*\s/\S*" "$spec_path" | grep -oP "(?<=\s)/[^,\s)]*" | sort | uniq)
    do
        replacement_path=${binary_paths_map["$original_path"]}
        if [[ -z "${binary_paths_map["$original_path"]}" && -z "${same_paths["$original_path"]}" ]]
        then
            echo "---------------- ERROR ----------------" >&2
            echo "New, unknown (Build)Requires path '$original_path'! Consult and/or update the 'binary_paths_map' and 'same_paths' variables." >&2
            echo "---------------- ERROR ----------------" >&2
            found_unknown_paths=1
        fi
    done
    if [[ -n $found_unknown_paths ]]
    then
        echo "Found errors, exiting." >&2
        exit 1
    fi

    # Now we search for all paths we know we need to map.
    # We don't limit ourselves to (Build)Requires as fixable paths are also used inside spec's scripts.
    binary_paths_count=$(grep -c -oP "$path_to_fix_regex" "$spec_path")
    if [[ $binary_paths_count -eq 0 ]]
    then
        echo "Found no binary paths to fix. Exiting."
        return
    fi

    for original_path in $(grep -oP "$path_to_fix_regex" "$spec_path" | grep -oP "$BINARY_PATHS_REGEX" | sort | uniq)
    do
        replacement_path=${binary_paths_map["$original_path"]}
        if [[ -z "$replacement_path" || "$replacement_path" == "MISSING" ]]
        then
            echo "ERROR: no mapping for binary path '$original_path' found! Consult and/or update the 'binary_paths_map' variable. Exiting." >&2
            exit 1
        fi

        echo "Replacing: '$original_path' -> '$replacement_path'."
        perl -ne "s:$path_to_fix_regex:\2$replacement_path:g; print;" < "$spec_path" | sponge "$spec_path"
    done
}

sanitize_package_names(){
    local original_package
    local replacement_package
    local requirement_line_regex
    local spec_path
    local targeted_fix_regex

    spec_path="$1"

    # The regex looks for (Build)Requires lines with replacable package names
    requirement_line_regex="(Build)?Requires(\([^)]+\))?:.*\s${PACKAGE_NAME_REGEX}[\s=><].*"

    for original_package in $(grep -oP "$requirement_line_regex" "$spec_path" | grep -oP "$PACKAGE_NAME_REGEX" | sort | uniq)
    do
        replacement_package=${package_name_map["$original_package"]}
        if [[ -n "$replacement_package" ]]
        then
            targeted_fix_regex="((Build)?Requires(\([^)]+\))?:.*)($original_package)(.*)"
            echo "Replacing: '$original_package' -> '$replacement_package'."
            perl -ne "s#$targeted_fix_regex#\1$replacement_package\5#g; print;" < "$spec_path" | sponge "$spec_path"
        else
            echo "ERROR: no mapping for package name '$original_package' found! Consult and/or update the 'package_name_map' variable. Exiting." >&2
            exit 1
        fi
    done
}

sanitize_spec_file() {
    local spec_path

    spec_path="$1"

    echo "Sanitizing \"$spec_path\":"

    add_vendor_info "$spec_path"
    sanitize_binary_paths "$spec_path"
    sanitize_package_names "$spec_path"

    echo "Sanitized  \"$spec_path\"."
}

sanitize_specs_directory() {
    local directory_path
    local specs_count

    directory_path="$1"

    specs_count=$(find "$directory_path" -type f -name "*.spec" -printf '.' | wc -c)
    if [[ $specs_count -eq 0 ]]
    then
        echo "No spec files found inside the \"$directory_path\" directory."
        return
    fi

    echo "Sanitizing all spec files inside the \"$directory_path\" directory."
    for spec_path in "$directory_path"/**/*.spec
    do
        sanitize_spec_file "$spec_path"
    done
}

check_args "$@"

for file_path in "$@"
do
    if [[ -d "$file_path" ]]
    then
        sanitize_specs_directory "$file_path"
    else
        sanitize_spec_file "$file_path"
    fi
done
