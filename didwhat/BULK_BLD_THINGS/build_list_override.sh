#!/usr/bin/bash

PROG_NAME=$0
print_usage()
{
	echo "Usage:"
	echo "${PROG_NAME##*/}: <build_list> <the_list_for_override_by_add> <the_list_for_override_by_rem>"
}

if [ $# -ne 3 ]
then
	print_usage
	exit
fi

BLD_LIST=$1
LST_OVRRD_BY_ADD=$2
LST_OVRRD_BY_REM=$3

for pkgname in `cat pkglist_override_build_by_add`
do
echo $pkgname >> $BLD_LIST 
done

for pkgname in `cat pkglist_override_build_by_rem`
do
/home/neerajs/utils/rem_full_line_match "$pkgname" $BLD_LIST 
done
