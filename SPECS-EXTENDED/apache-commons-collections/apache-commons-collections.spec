%bcond_with bootstrap

Name:           apache-commons-collections
Version:        3.2.2
Release:        37%{?dist}
Summary:        Provides new interfaces, implementations and utilities for Java Collections
License:        Apache-2.0
URL:            http://commons.apache.org/collections/
BuildArch:      noarch
#ExclusiveArch:  %{java_arches} noarch

Source0:        http://www.apache.org/dist/commons/collections/source/commons-collections-%{version}-src.tar.gz

Patch0:         0001-Port-to-Java-8.patch
Patch1:         0002-Port-to-OpenJDK-11.patch
Patch2:         0003-Port-to-OpenJDK-21.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
%endif

%description
The introduction of the Collections API by Sun in JDK 1.2 has been a
boon to quick and effective Java programming. Ready access to powerful
data structures has accelerated development by reducing the need for
custom container classes around each core object. Most Java2 APIs are
significantly easier to use because of the Collections API.
However, there are certain holes left unfilled by Sun's
implementations, and the Jakarta-Commons Collections Component strives
to fulfill them. Among the features of this package are:
- special-purpose implementations of Lists and Maps for fast access
- adapter classes from Java1-style containers (arrays, enumerations) to
Java2-style collections.
- methods to test or create typical set-theory properties of collections
such as union, intersection, and closure.

%package testframework
Summary:        Testframework for %{name}
Requires:       %{name} = %{version}-%{release}

%description testframework
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
%{summary}.

%prep
%setup -q -n commons-collections-%{version}-src

# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
find . -name "*.class" -exec rm -f {} \;

%patch 0 -p1
%patch 1 -p1
%patch 2 -p1

# Port to maven-antrun-plugin 3.0.0
sed -i s/tasks/target/ pom.xml

# Fix file eof
sed -i 's/\r//' LICENSE.txt PROPOSAL.html README.txt NOTICE.txt

%mvn_package :commons-collections-testframework testframework
%mvn_file ':commons-collections{,-testframework}' %{name}@1 commons-collections@1

%build
%mvn_build -- -Dcommons.packageId=collections

%install
%mvn_artifact commons-collections:commons-collections-testframework:%{version} target/commons-collections-testframework-%{version}.jar
%mvn_install

%files -f .mfiles
%doc PROPOSAL.html README.txt
%license LICENSE.txt NOTICE.txt

%files testframework -f .mfiles-testframework

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 3.2.2-36
- Rebuilt for java-21-openjdk as system jdk

* Tue Feb 20 2024 Marian Koncek <mkoncek@redhat.com> - 3.2.2-35
- Port to OpenJDK 21

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 04 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.2-32
- Port to apache-commons-parent 65

* Fri Sep 01 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.2-31
- Convert License tag to SPDX format

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.2.2-27
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 02 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.2-25
- Bump Java compiler source/target levels to 1.7

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.2-23
- Bootstrap build
- Non-bootstrap build

* Fri Mar 05 2021 Mat Booth <mat.booth@redhat.com> - 3.2.2-22
- Backport fix to build with maven-antrun-plugin 3.0.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 3.2.2-19
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Jun 26 2020 Alexander Kurtakov <akurtako@redhat.com> 3.2.2-18
- Rebuild to verify xmvn/maven switch to jakarta-annotations.

* Thu Jun 25 2020 Roland Grunberg <rgrunber@redhat.com> - 3.2.2-17
- Fix ambiguous reference in AbstractTestCollection to build on Java 11.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Fabio Valentini <decathorpe@gmail.com> - 3.2.2-15
- Adapt build and install scriptlets to fix issues in dependencies.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 3.2.2-14
- Really actually skip tests to fix builds with xmvn 3.1.0.

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.2-13
- Mass rebuild for javapackages-tools 201902

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.2-12
- Enable tests

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.2-11
- Mass rebuild for javapackages-tools 201901

* Fri Feb 08 2019 Mat Booth <mat.booth@redhat.com> - 3.2.2-12
- Rebuild to regenerate OSGi metadata

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.2-9
- Remove workaround for symlink->directory rpm bug

* Tue Apr 24 2018 Mat Booth <mat.booth@redhat.com> - 3.2.2-8
- Allow testframework to still be built even with tests disabled, which is
  needed by other packages

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 18 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.2-6
- Temporarly disable running tests

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 23 2016 Michael Simacek <msimacek@redhat.com> - 3.2.2-3
- Add workaround for symlink->directory rpm bug

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Michael Simacek <msimacek@redhat.com> - 3.2.2-1
- Update to upstream version 3.2.2
- Merge two javadoc subpackages
- Install with XMVn
- Specfile cleanup

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 23 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.1-25
- Remove requires on apache-commons-parent

* Fri Oct 17 2014 Timothy St. Clair <tstclair@redhat.com> - 3.2.1-24
- Fix broken Java 8 build

* Tue Oct 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.1-23
- Remove legacy Obsoletes/Provides for jakarta-commons

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.1-21
- Use .mfiles generated during build

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.2.1-20
- Use Requires: java-headless rebuild (#1067528)

* Mon Aug 12 2013 Mat Booth <fedora@matbooth.co.uk> - 3.2.1-19
- Fix FTBFS rhbz #991965

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.1-17
- Remove unneeded BR: maven-idea-plugin

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 3.2.1-15
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 08 2012 Jaromir Capik <jcapik@redhat.com> 3.2.1-13
- saxon dependency removed - not needed
- minor spec file changes according to the latest guidelines

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 6 2011 Chris Spike <spike@fedoraproject.org> 3.2.1-11
- Added *-testframework depmap entries.

* Wed Mar 16 2011 Alexander Kurtakov <akurtako@redhat.com> 3.2.1-10
- Drop tomcat5 subpackage.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 8 2010 Alexander Kurtakov <akurtako@redhat.com> 3.2.1-8
- Add commons-collections:commons-collections depmap.

* Mon Oct 4 2010 Alexander Kurtakov <akurtako@redhat.com> 3.2.1-7
- Fix pom name.
- Use newer maven plugins names.

* Tue Aug 31 2010 Carl Green <carlgreen at gmail.com> - 3.2.1-6
- Change package to own files in directories, not the directories

* Mon Aug 30 2010 Carl Green <carlgreen at gmail.com> - 3.2.1-5
- Remove source and patches no longer needed for Maven
- Fix non-standard groups and remove empty sections
- Fix file permissions

* Sat Aug 28 2010 Carl Green <carlgreen at gmail.com> - 3.2.1-4
- Renamed from jakarta-commons-collections
- Updated to use maven2
- Replaced saxon:group instruction with xsl:for-each-group in pom-maven2jpp-newdepmap.xsl
