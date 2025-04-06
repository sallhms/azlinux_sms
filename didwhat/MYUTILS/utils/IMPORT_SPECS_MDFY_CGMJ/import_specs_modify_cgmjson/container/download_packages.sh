#!/bin/bash
set +e
rootdir="/srpms"
outfile="$rootdir/output.txt"
manifest="$rootdir/packagelist.txt"
if [ ! -d $rootdir ]
then
    echo "Directoy $rootdir not found!"
    echo "Please add the following to your docker command: -v ~/mydirectory:$rootdir"
    exit 1
fi
[ ! -f $manifest ] && echo "Invalid rpm manifest $manifest" && usage
cd $rootdir
echo "" > $outfile

download_package() {
    package=$1
    yumdownloader --source $package
    if [ $? -ne 0 ]; then
        echo COULD NOT DOWNLOAD $package >> $outfile
    else
        echo DOWNLOADED $package >> $outfile
    fi
}

while IFS= read -r line; do
    if [ -z "$line" ]; then
        continue
    fi
    download_package $line
done < $manifest
[[ -n $line ]] && download_package $line

chmod 666 /srpms/*
echo "Saved list of source rpms in $outfile"
