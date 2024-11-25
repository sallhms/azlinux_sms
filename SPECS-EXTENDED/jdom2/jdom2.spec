%bcond_with bootstrap

Name:          jdom2
Version:       2.0.6.1
Release:       9%{?dist}
Summary:       Java manipulation of XML made easy
License:       Saxpath
URL:           http://www.jdom.org/
# ./generate-tarball.sh
Source0:       %{name}-%{version}.tar.gz
# Bnd tool configuration
Source3:       bnd.properties
# Remove bundled jars that might not have clear licensing
Source4:       generate-tarball.sh
# Use system libraries
# Disable gpg signatures
# Process contrib and junit pom files
Patch0:        0001-Adapt-build.patch

%if %{with bootstrap}
BuildRequires: javapackages-bootstrap
%else
BuildRequires: javapackages-local
BuildRequires: ant
BuildRequires: ant-junit
%endif

BuildArch:     noarch
#ExclusiveArch: %{java_arches} noarch

%description
JDOM is a Java-oriented object model which models XML documents.
It provides a Java-centric means of generating and manipulating
XML documents. While JDOM inter-operates well with existing
standards such as the Simple API for XML (SAX) and the Document
Object Model (DOM), it is not an abstraction layer or
enhancement to those APIs. Rather, it seeks to provide a robust,
light-weight means of reading and writing XML data without the
complex and memory-consumptive options that current API
offerings provide.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n jdom-JDOM-%{version}

%patch 0 -p1

sed -i 's/\r//' LICENSE.txt

# Unable to run coverage: use log4j12 but switch to log4j 2.x
sed -i.coverage "s|coverage, jars|jars|" build.xml

# XPath functionality is not needed
rm -rf core/src/java/org/jdom2/xpath/
sed -i '/import org.jdom2.xpath.XPathFactory/d' core/src/java/org/jdom2/JDOMConstants.java

%build
mkdir lib
%ant -Dversion=%{version} -Dcompile.source=1.8 -Dcompile.target=1.8 -Dj2se.apidoc=%{_javadocdir}/java maven

# Make jar into an OSGi bundle
# XXX disabled until BND is fixed
#bnd wrap --output build/package/jdom-%{version}.bar --properties %{SOURCE3} \
#         --version %{version} build/package/jdom-%{version}.jar
#mv build/package/jdom-%{version}.bar build/package/jdom-%{version}.jar

%install
%mvn_artifact build/maven/core/%{name}-%{version}.pom build/package/jdom-%{version}.jar
%mvn_install -J build/apidocs

%files -f .mfiles
%doc CHANGES.txt COMMITTERS.txt README.md TODO.txt
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 29 2024 Jiri Vanek <jvanek@redhat.com> - 2.0.6.1-8
- bump of release for for java-21-openjdk as system jdk

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 2.0.6.1-7
- Rebuilt for java-21-openjdk as system jdk

* Tue Feb 20 2024 Marian Koncek <mkoncek@redhat.com> - 2.0.6.1-6
- Update Java source/target to 1.8

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 08 2022 Marian Koncek <mkoncek@redhat.com> - 2.0.6.1-1
- Update to upstream version 2.0.6.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.0.6-27
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 02 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.0.6-25
- Bump Java compiler source/target levels to 1.7

* Thu Oct 14 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.0.6-24
- Add patches to address DoS security vulnerability
- Resolves: CVE-2021-33813

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.0.6-22
- Bootstrap build
- Non-bootstrap build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 10 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.6-20
- Drop log4j12 dependency and switch junit module to log4j 1.2 API shim.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 19 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.6-18
- Set javac source and target to 1.8 to fix Java 11 builds.

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.0.6-17
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu May 07 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.6-16
- Drop optional isorelax verifier support from contrib.

* Mon Apr 20 2020 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.0.6-15
- Disable contrib module

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.0.6-14
- Mass rebuild for javapackages-tools 201902

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.0.6-13
- Mass rebuild for javapackages-tools 201901

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Michael Simacek <msimacek@redhat.com> - 2.0.6-12
- Repack tarball without bundled jars
- The repacked jar contains slightly different source (force push by upstream?)
- Correct license tag

* Tue Jul 17 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.0.6-11
- Remove unneeded buildrequires

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Michael Simacek <msimacek@redhat.com> - 2.0.6-7
- Avoid hardcoded jar paths

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr 14 2016 Mat Booth <mat.booth@redhat.com> - 2.0.6-6
- Add OSGi metadata to main jar
- Fix file listed twice warning

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 24 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.0.6-3
- Remove unneeded BR on cobertura

* Fri Feb 06 2015 gil cattaneo <puntogil@libero.it> 2.0.6-2
- introduce license macro

* Tue Oct 21 2014 gil cattaneo <puntogil@libero.it> 2.0.6-1
- update to 2.0.6 (rhbz#1118627)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 2.0.5-3
- Use Requires: java-headless rebuild (#1067528)

* Thu Nov 14 2013 gil cattaneo <puntogil@libero.it> 2.0.5-2
- use objectweb-asm3

* Thu Sep 12 2013 gil cattaneo <puntogil@libero.it> 2.0.5-1
- initial rpm
