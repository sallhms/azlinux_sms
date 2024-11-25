Name:           jzlib
Version:        1.1.3
Release:        31%{?dist}
Summary:        Re-implementation of zlib in pure Java
License:        BSD-3-Clause
URL:            http://www.jcraft.com/jzlib/
BuildArch:      noarch
#ExclusiveArch:  %{java_arches} noarch
Source0:        https://github.com/ymnk/jzlib/archive/%{version}.tar.gz

# This patch is sent upstream: https://github.com/ymnk/jzlib/pull/15
Patch0:         jzlib-javadoc-fixes.patch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

%description
The zlib is designed to be a free, general-purpose, legally unencumbered 
-- that is, not covered by any patents -- loss-less data-compression 
library for use on virtually any computer hardware and operating system. 
The zlib was written by Jean-loup Gailly (compression) and Mark Adler 
(decompression). 

%package        javadoc
Summary:        API documentation for %{name}

%description    javadoc
%{summary}.

%package        demo
Summary:        Examples for %{name}
Requires:       %{name} = %{version}-%{release}

%description    demo
%{summary}.

%prep
%setup -q
%patch 0

%pom_xpath_set "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:source" 1.8
%pom_xpath_set "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:target" 1.8

# Make into OSGi bundle
%pom_xpath_inject "pom:project" "<packaging>bundle</packaging>"
%pom_add_plugin "org.apache.felix:maven-bundle-plugin" . "<extensions>true</extensions>"

%mvn_file : %{name}

%build
%mvn_build

%install
%mvn_install

# examples
install -dm 755 %{buildroot}%{_datadir}/%{name}
cp -pr example/* %{buildroot}%{_datadir}/%{name}

%files -f .mfiles
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%files demo
%doc %{_datadir}/%{name}

%changelog
* Wed Jul 24 2024 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.3-31
- Install license files in licensedir instead of docdir

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.1.3-29
- Rebuilt for java-21-openjdk as system jdk

* Sat Feb 24 2024 Marian Koncek <mkoncek@redhat.com> - 1.1.3-28
- Update Java source/target to 1.8

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 01 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.3-25
- Convert License tag to SPDX format

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.1.3-21
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 02 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.3-19
- Bump Java compiler source/target levels to 1.7

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 28 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.3-17
- Convert sources to SHA512

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 0:1.1.3-14
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jun 25 2020 Alexander Kurtakov <akurtako@redhat.com> 0:1.1.3-13
- Fix build with Java 11.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.3-10
- Mass rebuild for javapackages-tools 201902

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.3-9
- Mass rebuild for javapackages-tools 201901

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Mat Booth <mat.booth@redhat.com> - 0:1.1.3-8
- Add OSGi metadata

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 09 2014 Mat Booth <mat.booth@redhat.com> - 0:1.1.3-1
- Update to latest upstream, fixes rhbz #1079510
- Add patch for javadoc errors

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.1.2-3
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 14 2013 Mat Booth <fedora@matbooth.co.uk> 0:1.1.2-1
- Update to latest upstream, fixes rhbz #980461
- Fix bogus date in changelog

* Fri Jun 14 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.1-4
- Update to current packaging guidelines

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0:1.1.1-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Jan 7 2013 Alexander Kurtakov <akurtako@redhat.com> 0:1.1.1-1
- Update to latest upstream.

* Tue Oct 23 2012 Mat Booth <fedora@matbooth.co.uk> 0:1.1.0-3
- Add maven pom and depmap rhbz #806572.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Alexander Kurtakov <akurtako@redhat.com> 0:1.1.0-1
- Update to upstream 1.1.0 release.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 4 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.0.7-8
- Fix merge review comments bug#225956.

* Wed Apr 7 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.0.7-7.4
- Drop gcj_support.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0.7-7.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0.7-6.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.0.7-5.3
- drop repotag

* Thu May 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.0.7-5jpp.2
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0:1.0.7-5jpp.1
- Autorebuild for GCC 4.3

* Tue Aug 08 2006 Vivek Lakshmanan <vivekl@redhat.com> - 0:1.0.7-4jpp.1
- Re-sync with latest from JPP.
- Partially adopt new naming convention.

* Sat Jul 22 2006 Vivek Lakshmanan <vivekl@redhat.com> - 0:1.0.7-3jpp_2fc
- Rebuild.

* Sat Jul 22 2006 Vivek Lakshmanan <vivekl@redhat.com> - 0:1.0.7-3jpp_1fc
- Merge with latest version from JPP.

* Sat Jul 22 2006 Jakub Jelinek <jakub@redhat.com> - 0:1.0.5-2jpp_4fc
- Rebuilt

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0:1.0.5-2jpp_3fc
- rebuild

* Mon Mar  6 2006 Jeremy Katz <katzj@redhat.com> - 0:1.0.5-2jpp_2fc
- stop the scriptlet spew

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Mar 18 2005 Andrew Overholt <overholt@redhat.com> 1.0.5-2jpp_1fc
- Build into Fedora.
- Remove Distribution and Vendor tags.

* Tue Oct 19 2004 David Walluck <david@jpackage.org> 0:1.0.5-2jpp
- rebuild with jdk 1.4.2

* Tue Oct 19 2004 David Walluck <david@jpackage.org> 0:1.0.5-1jpp
- 0.1.5

* Mon Aug 23 2004 Randy Watler <rwatler at finali.com> - 0:1.0.3-2jpp
- Rebuild with ant-1.6.2

* Wed Jan 14 2004 Ralph Apel <r.apel@r-apel.de> - 0:1.0.3-1jpp
- First build.
