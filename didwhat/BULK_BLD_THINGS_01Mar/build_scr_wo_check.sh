#

PROG_NAME=$0

print_usage()
{
	echo "Usage:"
	echo "${PROG_NAME##*/}: <the fully qualified path to file containing build list of package> <Azure Linux Source Root Dir>"
	echo "    one package per line"
	exit
}

if [ $# -ne 2 ]
then
	print_usage
fi

BLD_LIST=$1
AZLINUX_DIR=$2

if [ ! -f $BLD_LIST ]
then
	echo "The list file $BLD_LIST was not found.  Either it does not exist or is not a file."
	print_usage
fi

if [ ! -d $AZLINUX_DIR ]
then
	echo "The Azure Linux Source Code Dir $AZLINUX_DIR was not found.  Either it does not exist or is not a directory."
	print_usage
fi

pk_bld_list=`awk '
	BEGIN {
		FS="/"
		first_pkg_printed=0;
	}
	{
		if ( first_pkg_printed == 1) {
			printf (" %s", $1);
		}
		else {
			printf ("%s", $1);
			first_pkg_printed = 1;
		}
	}
' $BLD_LIST`

#echo "pk_bld_list is $pk_bld_list"

num_pk=$(echo $pk_bld_list | wc --words)

echo "Number of packages in the build list = $num_pk"

pushd $AZLINUX_DIR/toolkit
PWD=`pwd`
echo changed to $PWD

export PACKAGE_URL_LIST="https://mariner3dailydevrepo.blob.core.windows.net/daily-repo-3-0-20241206-x86-64/built_rpms_all https://mariner3dailydevrepo.blob.core.windows.net/daily-repo-3-0-20241206-x86-64 https://packages.microsoft.com/azurelinux/3.0/prod/base/x86_64 https://packages.microsoft.com/azurelinux/3.0/prod/base/debuginfo/x86_64 https://packages.microsoft.com/azurelinux/3.0/prod/ms-oss/x86_64";

echo "Setting PACKAGE_URL_LIST from the calling script as follows:"
echo "------------------------------------------------------------"
echo "PACKAGE_URL_LIST=$PACKAGE_URL_LIST"

#Added dry run command so as to capture the run details in the build logs
echo "Dry run preceded actual run so as to capture the values passed:"
echo "---------------------------------------------------------------"
$AZLINUX_DIR/toolkit/pkgbld.sh -d -s ../SPECS-EXTENDED -p "$pk_bld_list"

#Actual build 
echo "Now triggering the actual build:"
echo "--------------------------------"
$AZLINUX_DIR/toolkit/pkgbld.sh -s ../SPECS-EXTENDED -p "$pk_bld_list"

popd
PWD=`pwd`
echo changed back to $PWD

#####################
#####################
######################$AZLINUX_DIR/pkgbld.sh -d -c -s ../SPECS-EXTENDED -p "CharLS devel"
######################$AZLINUX_DIR/pkgbld.sh -c -s ../SPECS-EXTENDED -p ""
#####################
#####################
