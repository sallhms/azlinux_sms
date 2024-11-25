Name:           regexp
Epoch:          1
Version:        1.5
Release:        49%{?dist}
Summary:        Simple regular expressions API
License:        Apache-2.0
URL:            http://jakarta.apache.org/%{name}/
BuildArch:      noarch
#ExclusiveArch:  %{java_arches} noarch

Source0:        http://archive.apache.org/dist/jakarta/%{name}/jakarta-%{name}-%{version}.tar.gz
Source2:        jakarta-%{name}-osgi-manifest.MF
Patch0:         jakarta-%{name}-attach-osgi-manifest.patch

BuildRequires:  ant
BuildRequires:  javapackages-local

Requires:       java-headless
Provides:       deprecated()

%description
Regexp is a 100% Pure Java Regular Expression package that was
graciously donated to the Apache Software Foundation by Jonathan Locke.
He originally wrote this software back in 1996 and it has stood up quite
well to the test of time.
It includes complete Javadoc documentation as well as a simple Applet
for visual debugging and testing suite for compatibility.

%package javadoc
Summary:        Javadoc for %{name}
Provides:       deprecated()

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n jakarta-%{name}-%{version}
%patch 0
cp -p %{SOURCE2} MANIFEST.MF
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

cat > pom.xml << EOF
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>jakarta-%{name}</groupId>
  <artifactId>jakarta-%{name}</artifactId>
  <version>%{version}</version>
</project>
EOF

%mvn_file : %{name}

%mvn_alias jakarta-%{name}:jakarta-%{name} %{name}:%{name}

%build
mkdir lib
%ant -Djakarta-site2.dir=. -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8 jar javadocs

%mvn_artifact pom.xml build/*.jar

%install
%mvn_install -J docs/api

%check
%ant -Djakarta-site2.dir=. test

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Wed Jul 24 2024 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.5-49
- Install license files in licensedir instead of docdir

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1:1.5-47
- Rebuilt for java-21-openjdk as system jdk

* Sat Feb 24 2024 Marian Koncek <mkoncek@redhat.com> - 1:1.5-46
- Update Java source/target to 1.8

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 01 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.5-43
- Convert License tag to SPDX format

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug 05 2022 Marian Koncek <mkoncek@redhat.com> - 1:1.5-40
- Explicitly specify JVM source and target version

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1:1.5-38
- Rebuilt for java-17-openjdk as system jdk

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.5-35
- Workaround for RPM bug #646523 - can't change symlink to directory

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1:1.5-32
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.5-28
- Mass rebuild for javapackages-tools 201902

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.5-27
- Mass rebuild for javapackages-tools 201901

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.5-28
- Mark package as deprecated

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 25 2016 Michael Simacek <msimacek@redhat.com> - 1:1.5-23
- Install with XMVn and add minimal pom

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.5-21
- Add OSGi manifest

* Tue Jul 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.5-20
- Add build-requires on javapackages-local

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jul  9 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.5-18
- Bump epoch as workaround for koji-shadow limitation

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun  2 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-16
- Fix dist tag

* Mon May 12 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-15
- Update to current packaging guidelines
- Resolves: rhbz#976723

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.5-14
- Use Requires: java-headless rebuild (#1067528)

* Fri Jul 26 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.5-13
- Rebuild for #988462

* Tue Jul 23 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.5-12
- Enable testsuite

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.5-11
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 31 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.5-9
- Install LICENSE file with javadoc package
- Add maven POM file
- Update to current packaging guidelines
- Convert versioned JAR to unversioned

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 6 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.5-5
- Drop gcj support.

* Fri Jan 08 2010 Andrew Overholt <overholt@redhat.com> 1.5-4.3
- Remove javadoc ghost symlinking.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.5-4.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.5-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.5-2.2
- drop repotag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0:1.5-2jpp.1
- Autorebuild for GCC 4.3

* Sat Feb 9 2008 Devrim GUNDUZ <devrim@commandprompt.com> 0:1.5-1jpp.1
- Update to 1.5
- Fix license
- Cosmetic cleanup

* Thu Feb 8 2007 Vivek Lakshmanan <vivekl at redhat.com> 0:1.4-3jpp.1.fc7
- Resync with JPP
- Use the upstream tar ball as JPP does since they clean it off jars anyway
- Use JPackage exception compliant naming scheme
- Remove section definition
- Install unversioned symlink
- Add missing ghost for unversioned link
- Add requires on java

* Fri Aug 4 2006 Vivek Lakshmanan <vivekl@redhat.com> 0:1.4-2jpp.2
- Rebuild.

* Fri Aug 4 2006 Vivek Lakshmanan <vivekl@redhat.com> 0:1.4-2jpp.1
- Merge with latest from JPP.
- Remove prebuilt jars from new source tar ball.

* Sat Jul 22 2006 Jakub Jelinek <jakub@redhat.com> - 0:1.3-2jpp_9fc
- Rebuilt

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0:1.3-2jpp_8fc
- rebuild

* Mon Mar  6 2006 Jeremy Katz <katzj@redhat.com> - 0:1.3-2jpp_7fc
- stop scriptlet spew

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0:1.3-2jpp_6fc
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0:1.3-2jpp_5fc
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Dec 21 2005 Jesse Keating <jkeating@redhat.com> 0:1.2-2jpp_4fc
- rebuilt again

* Tue Dec 13 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Jul 15 2005 Gary Benson <gbenson@redhat.com> 0:1.3-2jpp_3fc
- Build on ia64, ppc64, s390 and s390x.
- Switch to aot-compile-rpm.

* Tue Jun 14 2005 Gary Benson <gbenson@redhat.com> 0:1.3-2jpp_2fc
- Remove jarfile from the tarball.

* Thu May 26 2005 Gary Benson <gbenson@redhat.com> 0:1.3-2jpp_1fc
- Upgrade to 1.3-2jpp.
- Rearrange how BC-compiled stuff is built and installed.

* Mon May 23 2005 Gary Benson <gbenson@redhat.com> 0:1.3-1jpp_6fc
- Add alpha to the list of build architectures (#157522).
- Use absolute paths for rebuild-gcj-db.

* Thu May  5 2005 Gary Benson <gbenson@redhat.com> 0:1.3-1jpp_5fc
- BC-compile.

* Tue Jan 11 2005 Gary Benson <gbenson@redhat.com> 0:1.3-1jpp_4fc
- Sync with RHAPS.

* Thu Nov  4 2004 Gary Benson <gbenson@redhat.com> 0:1.3-1jpp_3fc
- Build into Fedora.

* Fri Oct  1 2004 Andrew Overholt <overholt@redhat.com> 0:1.3-1jpp_3rh
- add coreutils BuildRequires

* Wed Aug 25 2004 Fernando Nasser <fnasser@redhat.com> 0:1.3-2jpp
- Require Ant > 1.6
- Rebuild with Ant 1.6.2

* Fri Mar 26 2004 Frank Ch. Eigler <fche@redhat.com> 0:1.3-1jpp_2rh
- add RHUG upgrade cleanup

* Thu Mar  3 2004 Frank Ch. Eigler <fche@redhat.com> 0:1.3-1jpp_1rh
- RH vacuuming

* Thu Oct 09 2003 Henri Gomez <hgomez at users.sourceforge.net> 0:1.3-1jpp
- regexp 1.3

* Fri May 09 2003 David Walluck <david@anti-microsoft.org> 0:1.2-14jpp
- update for JPackage 1.5

* Fri Mar 23 2003 Nicolas Mailhot <Nicolas.Mailhot (at) JPackage.org> 1.2-13jpp
- for jpackage-utils 1.5

* Tue Jul 02 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.2-11jpp
- section marcro
- removed additional symlink

* Mon Jun 24 2002 Henri Gomez <hgomez@slib.fr> 1.2-10jpp
- add official jakarta jarname (jakarta-regexp-1.2.jar) symlink to real
  jarname

* Mon Jun 10 2002 Henri Gomez <hgomez@slib.fr> 1.2-9jpp
- use sed instead of bash 2.x extension in link area to make spec compatible
  with distro using bash 1.1x
- use official tarball

* Fri Jan 18 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.2-8jpp 
- versioned dir for javadoc
- no dependencies javadoc package

* Sat Dec 1 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.2-7jpp
- javadoc in javadoc package
- official summary

* Wed Nov 21 2001 Christian Zoffoli <czoffoli@littlepenguin.org> 1.2-5jpp
- removed packager tag
- new jpp extension

* Sun Sep 30 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.2-5jpp
- first unified release
- s/jPackage/JPackage

* Sun Aug 26 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.2-4mdk
- vendor tag
- packager tag
- s/Copyright/License/
- truncated description to 72 columns in spec
- spec cleanup
- used versioned jar
- used new source packaging policy

* Sat Feb 17 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.2-3mdk
- spec cleanup
- changelog correction

* Sun Feb 04 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.2-2mdk
- merged with Henri Gomez <hgomez@slib.fr> specs:
- changed name to regexp
-  changed javadir to /usr/share/java
-  dropped jdk & jre requirement
-  added Jikes support
- changed jar name to regexp.jar
- corrected doc

* Sun Jan 14 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.2-1mdk
- first Mandrake release
