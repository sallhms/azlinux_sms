
There will be a directory created with the name "output".  This directory will have the extracted sources of the packages kept in 
package wise directory structure, like "output/pkgname/".  If there is an "output" directory already existing please beware that
it will be overwritten.

The input cgmanifest json file gets overwritten.  Therefore, use a copy of the sample_cgmanifest_ORIG.json.  For the same reason
the file sample_cgmanifest_ORIG.json has been made read-only, so that overwriting the sample file is not easy.

The file sample_pkglist_file is provided to show that we just need to provide the packages one package name per line in this file.
