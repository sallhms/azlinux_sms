#

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
' /fifth_disk/bb_dec23/didwhat/list_pkgs_to_build_4`

#echo "pk_bld_list is $pk_bld_list"

num_pk=$(echo $pk_bld_list | wc --words)

echo "Number of packages in the build list = $num_pk"

export PACKAGE_URL_LIST="https://mariner3dailydevrepo.blob.core.windows.net/daily-repo-3-0-20241206-x86-64/built_rpms_all https://mariner3dailydevrepo.blob.core.windows.net/daily-repo-3-0-20241206-x86-64 https://packages.microsoft.com/azurelinux/3.0/prod/base/x86_64 https://packages.microsoft.com/azurelinux/3.0/prod/base/debuginfo/x86_64 https://packages.microsoft.com/azurelinux/3.0/prod/ms-oss/x86_64";

echo "Setting PACKAGE_URL_LIST from the calling script as follows:"
echo "------------------------------------------------------------"
echo "PACKAGE_URL_LIST=$PACKAGE_URL_LIST"

#Added dry run command so as to capture the run details in the build logs
echo "Dry run preceded actual run so as to capture the values passed:"
echo "---------------------------------------------------------------"
./pkgbld.sh -d -s ../SPECS-EXTENDED -p "$pk_bld_list"

#Actual build 
echo "Now triggering the actual build:"
echo "--------------------------------"
./pkgbld.sh -s ../SPECS-EXTENDED -p "$pk_bld_list"

#./pkgbld.sh -d -c -s ../SPECS-EXTENDED -p "CharLS devel"
#./pkgbld.sh -c -s ../SPECS-EXTENDED -p ""
