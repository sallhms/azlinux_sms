
usage()
{
	echo "Give the following command:"
	echo "$0 pkgname"
	echo "in the root of source code"
#	echo "arg passed is" $1
}

if [ $# -lt 1 ]
then
#usage "Insufficient arguments" 
usage 
exit
fi

pkgname=$1
echo pkgname is "$pkgname"
#echo "All OK"

grep -e "^Version:" -e "^Release:" SPECS-EXTENDED/$pkgname/$pkgname.spec 

#awk -F: '{printf $1 ":"  $2}' /sec_disk/Downloads/dailybuild/13Oct/Extracted_artifacts/build_state.csv
#grep -e "^Version:" SPECS-EXTENDED/$pkgname/$pkgname.spec | awk -F" " '{printf $1 ":"  $2 "\n"}' | awk -F":" '{printf $1 ":" $3 "\n"}'
grep -e "^Version:" SPECS-EXTENDED/$pkgname/$pkgname.spec | awk -F" " '{printf $1 ":"  $2 "\n"}' | awk -F":" '{printf $3 "\n"}'
Ver=`grep -e "^Version:" SPECS-EXTENDED/$pkgname/$pkgname.spec | awk -F" " '{printf $1 ":"  $2 "\n"}' | awk -F":" '{printf $3 "\n"}'`
echo "Ver = " $Ver


#grep -e "^Release:" SPECS-EXTENDED/$pkgname/$pkgname.spec | awk -F" " '{printf $1 ":"  $2 "\n"}' | awk -F":" '{printf $1 ":" $3 "\n"}' 
grep -e "^Release:" SPECS-EXTENDED/$pkgname/$pkgname.spec | awk -F" " '{printf $1 ":"  $2 "\n"}' | awk -F":" '{printf $3 "\n"}' | awk -F"%" '{printf $1 "\n"}'
Rel=`grep -e "^Release:" SPECS-EXTENDED/$pkgname/$pkgname.spec | awk -F" " '{printf $1 ":"  $2 "\n"}' | awk -F":" '{printf $3 "\n"}' | awk -F"%" '{printf $1 "\n"}'`
echo "Rel = " $Rel

echo "Ver-Rel = " $Ver"-"$Rel

