The v1.2 is different from v1.1:
1. It uses str function over the cell.value for comparison against the version string variable "pkgvr_from_bblist".
   Earlier in v1.1 since the str function was not used, the comparison would give a mismatch for matching version numbers.


