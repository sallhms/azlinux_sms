Name:           js-jquery
Version:        3.7.1
Release:        4%{?dist}
Summary:        JavaScript DOM manipulation, event handling, and AJAX library
BuildArch:      noarch

%global ver_x %(echo %{version} | cut -d. -f1)
%global ver_y %(echo %{version} | cut -d. -f2)
%global ver_z %(echo %{version} | cut -d. -f3)

License:        MIT
URL:            https://jquery.com/
Source0:        https://github.com/jquery/jquery/archive/%{version}/jquery-%{version}.tar.gz
# Created by ./update-sources.sh <version>
Source1:        jquery_%{version}_node_modules.tar.gz

# disable gzip-js during build
Patch1:         %{name}-disable-gzip-js.patch


BuildRequires:  web-assets-devel
BuildRequires:  nodejs-packaging
BuildRequires:  nodejs

Provides:       jquery = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}%{ver_x} = %{version}-%{release}
Provides:       %{name}%{ver_x}-static = %{version}-%{release}

Requires:       web-assets-filesystem

# Bundles sizzle (https://github.com/jquery/sizzle/) in node_modules/sizzle
# Get version from package.json
Provides:       bundled(sizzle) = 2.3.5
Provides:       bundled(js-sizzle) = 2.3.5


%description
jQuery is a fast, small, and feature-rich JavaScript library. It makes things
like HTML document traversal and manipulation, event handling, animation, and
Ajax much simpler with an easy-to-use API that works across a multitude of
browsers. With a combination of versatility and extensibility, jQuery has
changed the way that millions of people write JavaScript.

%prep
%autosetup -n jquery-%{version} -v -p1

#remove precompiled stuff
rm -rf dist/*

# Install the cached node modules
tar xf %{SOURCE1}


%build
./node_modules/grunt-cli/bin/grunt -v 'build:*:*' uglify


%check
./node_modules/grunt-cli/bin/grunt -v 'build:*:*' test:prepare test:fast


%install
%global installdir %{buildroot}%{_jsdir}/jquery

mkdir -p %{installdir}/%{version}
cp -p dist/* %{installdir}/%{version}

mkdir -p %{buildroot}%{_webassetdir}
ln -s ../javascript/jquery %{buildroot}%{_webassetdir}/jquery

ln -s %{version} %{installdir}/latest
ln -s %{version} %{installdir}/%{ver_x}
ln -s %{version} %{installdir}/%{ver_x}.%{ver_y}


%files
%{_jsdir}/jquery
%{_webassetdir}/jquery
%doc AUTHORS.txt CONTRIBUTING.md LICENSE.txt README.md


%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Sep 02 2023 Orion Poplawski <orion@nwra.com> - 3.7.1-1
- Update to 3.7.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 09 2023 Orion Poplawski <orion@nwra.com> - 3.6.4-1
- Update to 3.6.4

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 22 2022 Orion Poplawski <orion@nwra.com> - 3.6.3-1
- Update to 3.6.3

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Orion Poplawski <orion@nwra.com> - 3.6.0-1
- Update to 3.6.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 17 2020 Stephen Gallagher <sgallagh@redhat.com> - 3.5.0-3
- Add explicit dependency on nodejs

* Wed Apr 15 2020 Stephen Gallagher <sgallagh@redhat.com> - 3.5.0-2
- Add virtual Provides: for bundled sizzle

* Mon Apr 13 2020 Stephen Gallagher <sgallagh@redhat.com> - 3.5.0-1
- Update to 3.5.0
- Bundle the build dependencies in the source RPM
- Drop unneeded patches

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 18 2018 Christopher Tubbs <ctubbsii@fedoraproject.org> - 3.3.1-1
- Update to 3.3.1; fixes rhbz#1536772 rhbz#1445079 rhbz#1591846 Security fix for
  CVE-2012-6708

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 12 2017 Christopher Tubbs <ctubbsii@fedoraproject.org> - 3.2.1-1
- Update to jQuery 3.2.1

* Tue Apr 11 2017 Christopher Tubbs <ctubbsii@fedoraproject.org> - 2.2.4-3
- Update provides in prep for js-jquery package rename to js-jquery2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Christopher Tubbs <ctubbsii@fedoraproject.org> - 2.2.4-1
- Update to 2.2.4 and backport XSS patch (bz#1399550,bz#1399549)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 04 2015 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.3-1
- new upstream release 2.1.3
  http://blog.jquery.com/2014/12/18/jquery-1-11-2-and-2-1-3-released-safari-fail-safe-edition/

* Tue Oct 21 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.1-4
- drop unneccessary symlinks

* Tue Jun 03 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.1-3
- follow the github SourceURL guidelines

* Sat May 31 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.1-2
- drop sed hack now that grunt is fixed

* Fri May 30 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.1-1
- update to 2.1.1
- use system packages for build (with help from Jamie Nguyen)

* Wed Mar 19 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.0-0.1
- initial package
