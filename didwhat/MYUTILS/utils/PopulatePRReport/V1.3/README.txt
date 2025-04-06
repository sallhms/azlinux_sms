The v1.3 is different from v1.2:

1. It takes the input for the column "Version in 3.0" from "all-1563-pkg-list1.xlsx" in "C:\Users\v-nsallh\OneDrive - Microsoft\Documents\Work\PackageUpgrades-3.0\AutoAnalyzed\Analysis_Result_BeingUsed_06Nov".

The file "all-1563-pkg-list1.xlsx" is the file that was being used for the analysed packages since 6 Nov.  In this xlsx the Package Version number in 3.0-dev branch is correctly derived.

So, our consolidated sheet can pick this column value.

In absence of this, several cells remained blank in the consolidated sheet which led to false mismatch of 3.0-dev version and Fedora 41 version.
