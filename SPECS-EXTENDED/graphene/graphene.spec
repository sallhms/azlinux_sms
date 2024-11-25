Name:           graphene
Version:        1.10.6
Release:        9%{?dist}
Summary:        Thin layer of types for graphic libraries

License:        MIT
URL:            https://github.com/ebassi/graphene
Source:         %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
# https://github.com/ebassi/graphene/commit/3b3e316908e4fb15056d10fb9d5271eed6f65051
# https://github.com/ebassi/graphene/commit/fbfbdad5a3f38ddbe543ee8c236b4315bba111b9
Patch0:         graphene-1.10.6-perf-aarch64.patch
# https://github.com/ebassi/graphene/commit/3b3e316908e4fb15056d10fb9d5271eed6f65051
Patch1:         graphene-1.10.6-perf.patch

BuildRequires:  gcc
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson >= 0.50.1
BuildRequires:  pkgconfig(gobject-2.0) >= 2.30.0

%description
Graphene provides a small set of mathematical types needed to implement graphic
libraries that deal with 2D and 3D transformations and projections.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tests
Summary:        Tests for the %{name} package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%prep
%autosetup -p1

%build
# Disable neon
# https://github.com/ebassi/graphene/issues/215
%meson -Dgtk_doc=true \
%ifarch %{arm}
  -Darm_neon=false \
%endif

%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE.txt
%doc README.md
%{_libdir}/girepository-1.0/
%{_libdir}/libgraphene-1.0.so.0*

%files devel
%{_includedir}/graphene-1.0/
%dir %{_libdir}/graphene-1.0
%{_libdir}/graphene-1.0/include/
%{_libdir}/libgraphene-1.0.so
%{_libdir}/pkgconfig/graphene-1.0.pc
%{_libdir}/pkgconfig/graphene-gobject-1.0.pc
%{_datadir}/gir-1.0/
%{_datadir}/gtk-doc/

%files tests
%{_libexecdir}/installed-tests/
%{_datadir}/installed-tests/

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Dan Horák <dan[at]danny.cz> - 1.10.6-2
- upstream perfomance fixes for non-x86 arches

* Tue Apr 06 2021 Kalev Lember <klember@redhat.com> - 1.10.6-1
- Update to 1.10.6

* Tue Mar 09 2021 Nicolas Chauvet <kwizart@gmail.com> - 1.10.4-2
- Disable neon for graphene on armv7hl
- Add meson_test

* Wed Feb 10 2021 Kalev Lember <klember@redhat.com> - 1.10.4-1
- Update to 1.10.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 28 2020 Jeff Law <law@redhat.com> - 1.10.2-5
- Re-enable LTO as upstream GCC target/96939 has been fixed

* Mon Aug 10 2020 Jeff Law <law@redhat.com> - 1.10.2-4
- Disable LTO for now

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Kalev Lember <klember@redhat.com> - 1.10.2-1
- Update to 1.10.2
- Enable gtk-doc support

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 08 2019 Kalev Lember <klember@redhat.com> - 1.10.0-1
- Update to 1.10.0

* Tue Aug 13 10:06:51 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.6-1
- Update to 1.9.6

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Kalev Lember <klember@redhat.com> - 1.9.4-1
- Update to 1.9.4

* Tue May 14 2019 Kalev Lember <klember@redhat.com> - 1.9.2-1
- Update to 1.9.2

* Tue May 07 2019 Kalev Lember <klember@redhat.com> - 1.9.1-0.1.git5a4531b
- Update to 1.9.1 git snapshot

* Tue Mar 05 2019 Kalev Lember <klember@redhat.com> - 1.8.6-1
- Update to 1.8.6

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.8.4-1
- Update to 1.8.4

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Kalev Lember <klember@redhat.com> - 1.8.2-1
- Update to 1.8.2

* Fri Feb 23 2018 Kalev Lember <klember@redhat.com> - 1.8.0-1
- Update to 1.8.0
- Drop ldconfig scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 02 2017 Kalev Lember <klember@redhat.com> - 1.6.0-1
- Update to 1.6.0

* Mon Feb 27 2017 Kalev Lember <klember@redhat.com> - 1.5.4-3
- Build for ppc64 again now that gcc ICE is fixed

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Kalev Lember <klember@redhat.com> - 1.5.4-1
- Update to 1.5.4

* Mon Jan 02 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.5.2-1
- Update to 1.5.2

* Tue Nov 22 2016 Kalev Lember <klember@redhat.com> - 1.5.1-0.2.git8a7a4a3
- Install installed tests to libexecdir (#1397317)

* Tue Nov 22 2016 Kalev Lember <klember@redhat.com> - 1.5.1-0.1.git8a7a4a3
- Initial Fedora packaging
