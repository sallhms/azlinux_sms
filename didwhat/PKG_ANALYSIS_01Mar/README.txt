

We have pushed a branch created from a specific commit id such that 
the REMOVED, EXISTS_IN_BOTH decisions are the same as were seen in 
output20.txt.

This commit id is "02fe186d1ee8583df3a58b069d4b7a27d608b689"
and 
the branch is "topic_upgRef_02fe186d1_13Dec".

This has been done on the basis on the following text that detail
the history and the reason behind this.

BUT THE ABOVE PUSHED BRANCH DIDN'T HELP BECAUSE THE REPO WAS sallhms.
As a result the PR queries with the author names fail against this
branch in sallhms repo.

We have cloned from microsoft now and created the same named branch
i.e. "topic_upgRef_02fe186d1_13Dec" over the same commit id of 3.0-dev, 
i.e. "02fe186d1ee8583df3a58b069d4b7a27d608b689".

With the above topic branch pushed to github we will always have 
this reference readily available.

===================================================================
===================================================================

The "output20.txt" is same is "checkoutput2.txt".

"output20.txt" had been generated using "pkg_py_analysis_v8" and certain 
code base of "https://github.com/microsoft/azurelinux.git".

"checkoutput2.txt" had been generated using "pkg_py_analysis_v8" and 
the commit id "02fe186d1ee8583df3a58b069d4b7a27d608b689" of 
"https://github.com/microsoft/azurelinux.git".

BACKGROUND:
-----------
"checkoutput2.txt" generation was an exercise carried out to determine
which version of the tool "pkg_py_analysis_v8" had been used, to 
generate "output20.txt".  

In that exercise when we used "pkg_py_analysis_v8" on a recent clone of 
the code base "https://github.com/microsoft/azurelinux.git", the output 
generated was different from "output20.txt".

I could find that the cause of this difference was that the head of 
code base was different.  As a result the version of some packages
in 3.0-dev now is up to date as compared to the time it was back in 
Dec 2024.  This also led to some packages being reported as "REMOVED"
now as against the earlier status of "EXISTS_IN_BOTH".

Therefore, "checkoutput2.txt" was generated using a commit id that was
done on 13 Dec 2024.  The commit id chosed was 
"02fe186d1ee8583df3a58b069d4b7a27d608b689".
The tool script was "pkg_py_analysis_v8_updated".  This script is different
from "pkg_py_analysis_v8" only in the path used for the 
"MSREPO_3DEV_WORKDIR", because we had removed the Microsoft AzLinux checkout
and had therefore to use a different checkout.

```
neerajs [ PKG_ANALYSIS_15Feb ]$ diff pkg_py_analysis_v8 pkg_py_analysis_v8_updated 
10c10,11
< MSREPO_3DEV_WORKDIR="/home/neerajs/work/REPOS/Microsoft_AZL/azurelinux"
---
> #MSREPO_3DEV_WORKDIR="/home/neerajs/work/REPOS/Microsoft_AZL/azurelinux"
> MSREPO_3DEV_WORKDIR="/home/neerajs/Downloads/docker_folder/REPOS/Microsoft_AZL/azurelinux"
neerajs [ PKG_ANALYSIS_15Feb ]$ 
```

Using the commit id "02fe186d1ee8583df3a58b069d4b7a27d608b689" and 
"pkg_py_analysis_v8" resulted in "checkoutput2.txt" being exactly same 
as "output20.txt".

CONCLUSION:
-----------
For repeated results we will stick to:
   1. "02fe186d1ee8583df3a58b069d4b7a27d608b689" commit id.
   2. The 3.0-dev build logs that we are using historically since 
      beginning and not the recent ones.  Because we carry out the "upgrade 
      required/not required" decisions based upon this build data.
   3. As long as the individual sheets are the same the results will be the 
      same.
