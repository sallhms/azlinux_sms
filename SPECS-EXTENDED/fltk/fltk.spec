# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

# MinGW is enabled by default (except for RHEL), to disable use '--without mingw'
%if 0%{?rhel} || 0%{?flatpak}
%bcond_with mingw
%else
%bcond_without mingw
%endif

Name:		    fltk
Version:	    1.3.8
Release:	    10%{?dist}
Summary:	    C++ user interface toolkit

# see COPYING (or http://www.fltk.org/COPYING.php ) for exceptions details
License:	    LGPL-2.0-or-later with exceptions	
URL:            http://www.fltk.org/

Source0:        http://fltk.org/pub/%{name}/%{version}/%{name}-%{version}-source.tar.gz
Source1:        fltk-config.sh

Patch0:         fltk-cmake.patch
# add lib64 support, drop extraneous libs (bug #708185) and ldflags (#1112930)
Patch1:         fltk-1.3.4-fltk_config.patch
# Fix cmake install location for MinGW build
Patch2:         mingw-fltk-cmake.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
# For MinGW builds
#BuildRequires:  fltk-fluid
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  texlive-latex
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(gl) pkgconfig(glu) 
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm) 
BuildRequires:  pkgconfig(xext) pkgconfig(xinerama) pkgconfig(xft) pkgconfig(xt) pkgconfig(x11) 
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(zlib)

%if %{with mingw}
# MinGW
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-zlib
# Libraries
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-libjpeg

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-zlib
# Libraries
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-libjpeg
%endif


%global _description \
FLTK (pronounced "fulltick") is a cross-platform C++ GUI toolkit. \
It provides modern GUI functionality without the bloat, and supports \
3D graphics via OpenGL and its built-in GLUT emulation.

%description
%{_description}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libstdc++-devel
Requires:       pkgconfig(fontconfig)
Requires:       pkgconfig(gl) pkgconfig(glu)
Requires:       pkgconfig(ice) pkgconfig(sm)
Requires:       pkgconfig(xft) pkgconfig(xt) pkgconfig(x11)
Requires:       pkgconfig(libjpeg)
Requires:       pkgconfig(libpng)
Requires:       pkgconfig(zlib)
%description devel
%{summary}.

%package static
Summary:        Static libraries for %{name}
Requires:       %{name}-devel = %{version}-%{release}
%description static
%{summary}.

%package fluid
Summary:        Fast Light User Interface Designer
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel
%description fluid
%{summary}, an interactive GUI designer for %{name}. 

%if %{with mingw}
%package -n mingw32-fltk
Summary:       %{summary}
 
%description -n mingw32-fltk
%{_description}
 
# Win64
%package -n mingw64-fltk
Summary:       MinGW compiled fltk for the Win64 target
 
%description -n mingw64-fltk
%{_description}
 
%package -n mingw32-fltk-static
Summary:       %{summary}
 
%description -n mingw32-fltk-static
%{_description}
 
# Win64
%package -n mingw64-fltk-static
Summary:       MinGW compiled fltk for the Win64 target
 
%description -n mingw64-fltk-static
%{_description}
 
%{?mingw_debug_package}
%endif


%prep
%autosetup -p1


%build
%cmake -DFLTK_CONFIG_PATH:PATH=%{_libdir}/cmake/fltk \
       -DOpenGL_GL_PREFERENCE=GLVND \
       -DOPTION_BUILD_HTML_DOCUMENTATION:BOOL=ON \
       -DOPTION_BUILD_PDF_DOCUMENTATION:BOOL=OFF \
       -DOPTION_BUILD_SHARED_LIBS:BOOL=ON

%cmake_build

make docs -C %{_vpath_builddir}

%if %{with mingw}
%mingw_cmake -DOPTION_BUILD_SHARED_LIBS=TRUE
%mingw_make_build
%endif


%install
%cmake_install

# Deal with license file of same name
mv src/xutf8/COPYING ./COPYING.xutf8

# we only apply this hack to multilib arch's
%ifarch x86_64 %{ix86}
%global arch %(uname -m 2>/dev/null || echo undefined)
mv $RPM_BUILD_ROOT%{_bindir}/fltk-config \
   $RPM_BUILD_ROOT%{_bindir}/fltk-config-%{arch}
install -p -m755 -D %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/fltk-config
%endif

%if %{with mingw}
%mingw_make_install
%mingw_debug_install_post
%endif


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/fluid.desktop


%ldconfig_scriptlets


%files
%doc ANNOUNCEMENT CHANGES CREDITS README
%license COPYING COPYING.xutf8
%{_libdir}/libfltk.so.1.3*
%{_libdir}/libfltk_forms.so.1.3*
%{_libdir}/libfltk_gl.so.1.3*
%{_libdir}/libfltk_images.so.1.3*

%files devel
%doc %{_vpath_builddir}/documentation/html
%{_bindir}/fltk-config
%{?arch:%{_bindir}/fltk-config-%{arch}}
%{_includedir}/FL/
%{_libdir}/libfltk.so
%{_libdir}/libfltk_forms.so
%{_libdir}/libfltk_gl.so
%{_libdir}/libfltk_images.so
%{_libdir}/cmake/fltk/
%{_mandir}/man1/fltk-config.1*
%{_mandir}/man3/fltk.3*
%{_mandir}/man6/*.6*

%files static
%{_libdir}/libfltk.a
%{_libdir}/libfltk_forms.a
%{_libdir}/libfltk_gl.a
%{_libdir}/libfltk_images.a

%files fluid
%{_bindir}/fluid
%{_mandir}/man1/fluid.1*
%{_datadir}/applications/fluid.desktop
%{_datadir}/mime/packages/fluid.xml
%{_datadir}/icons/hicolor/*/*/*

%if %{with mingw}
%files -n mingw32-fltk
%license COPYING COPYING.xutf8
%{mingw32_bindir}/fltk-config
%{mingw32_bindir}/libfltk.dll
%{mingw32_libdir}/libfltk.dll.a
%{mingw32_bindir}/libfltk_forms.dll
%{mingw32_libdir}/libfltk_forms.dll.a
%{mingw32_bindir}/libfltk_images.dll
%{mingw32_libdir}/libfltk_images.dll.a
%{mingw32_bindir}/libfltk_gl.dll
%{mingw32_libdir}/libfltk_gl.dll.a
%{mingw32_includedir}/FL/
%{mingw32_datadir}/cmake/fltk/
%exclude %{mingw32_datadir}/man/*

%files -n mingw64-fltk
%license COPYING COPYING.xutf8
%{mingw64_bindir}/fltk-config
%{mingw64_bindir}/libfltk.dll
%{mingw64_libdir}/libfltk.dll.a
%{mingw64_bindir}/libfltk_forms.dll
%{mingw64_libdir}/libfltk_forms.dll.a
%{mingw64_bindir}/libfltk_images.dll
%{mingw64_libdir}/libfltk_images.dll.a
%{mingw64_bindir}/libfltk_gl.dll
%{mingw64_libdir}/libfltk_gl.dll.a
%{mingw64_includedir}/FL/
%{mingw64_datadir}/cmake/fltk/
%exclude %{mingw64_datadir}/man/*

%files -n mingw32-fltk-static
%{mingw32_libdir}/libfltk.a
%{mingw32_libdir}/libfltk_forms.a
%{mingw32_libdir}/libfltk_images.a
%{mingw32_libdir}/libfltk_gl.a

%files -n mingw64-fltk-static
%{mingw64_libdir}/libfltk.a
%{mingw64_libdir}/libfltk_forms.a
%{mingw64_libdir}/libfltk_images.a
%{mingw64_libdir}/libfltk_gl.a
%endif


%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 05 2022 Richard Shaw <hobbes1069@gmail.com> - 1.3.8-5
- Fix second instance of uname -i in bash script.

* Sat Aug 27 2022 Richard Shaw <hobbes1069@gmail.com> - 1.3.8-4
- Spec file modernization and fixes:
  Update to SPDX license tag
  Clean up spec file formatting
  Remove obsolete snapshot build support
  Migrate from uname -i to uname -m

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 20 2021 Richard Shaw <hobbes1069@gmail.com> - 1.3.8-1
- Update to 1.3.8.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 27 2021 Richard Shaw <hobbes1069@gmail.com> - 1.3.6-1
- Update to 1.3.6.

* Mon Feb 22 2021 Richard Shaw <hobbes1069@gmail.com> - 1.3.5-11
- Update requires for devel package, fixes #1931645.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Adam Jackson <ajax@redhat.com> - 1.3.5-9
- Remove BuildRequires xprop entirely. If present, the configure script will call
  it looking for a property on the root window that Fedora's X server does not
  set, and which would not work anyway since there is no X server running in the
  buildroot, so we can just remove the dependency.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Adam Jackson <ajax@redhat.com> - 1.3.5-7
- BuildRequires xprop not xorg-x11-server-utils

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 14 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.3.5-5
- restore fltk_config.patch lost in last (cmake) merge

* Mon May 11 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.3.5-4
- merge cmake PR
- spec cosmetics

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 03 2019 Richard Shaw <hobbes1069@gmail.com> - 1.3.5-1
- Update to 1.3.5.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.3.4-6
- use %%make_build %%make_install %%ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.4-4
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 04 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.3.4-1
- 1.3.4 (#1385984)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 27 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.3.3-8
- fltk_config.patch: remove @LARGEFILE@ @PTHREAD_FLAGS@ too (#1350069)

* Sun Jun 26 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.3.3-7
- -devel: Requires: pkgconfig(gl) pkgconfig(glu)
- cleaner DSOFLAGS
- fltk_config.patch: imposes internal build flags on the user (#1350069)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 17 2015 Adam Jackson <ajax@redhat.com> 1.3.3-5
- For whatever reason fltk thinks it's spelled DSOFLAGS not LDFLAGS, so set
  that when building so hardening takes effect

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 06 2015 Rex Dieter <rdieter@fedoraproject.org> 1.3.3-3
- rebuild (gcc5)

* Wed Feb 18 2015 Rex Dieter <rdieter@fedoraproject.org> 1.3.3-2
- pull in upstream fixes for undefined symbols

* Fri Feb 13 2015 Rex Dieter <rdieter@fedoraproject.org> 1.3.3-1
- 1.3.3

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 25 2014 Rex Dieter <rdieter@fedoraproject.org> 1.3.2-6
- fltk-config transmits wrong ldflags (#1112930)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 24 2014 Rex Dieter <rdieter@fedoraproject.org> 1.3.2-4
- refresh clipboard patch (#920573)

* Thu Jan 23 2014 jchaloup <jchaloup@redhat.com> - 1.3.2-3
- autoconfig moved from build to prep section

* Thu Jan 16 2014 Petr Hracek <phracek@redhat.com> - 1.3.2-2
- fltk is not build properly (#1048857)

* Mon Aug 26 2013 Rex Dieter <rdieter@fedoraproject.org> 1.3.2-1
- fltk-1.3.2

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.3.0-9
- rebuild due to "jpeg8-ABI" feature drop

* Tue Dec 04 2012 Adam Tkac <atkac redhat com> - 1.3.0-8
- fix ABI breakage caused by fltk-1_v4.3.x-cursor.patch (#883026)

* Thu Nov 29 2012 Adam Tkac <atkac redhat com> - 1.3.0-7
- add xcursor BR

* Wed Aug 22 2012 Adam Tkac <atkac redhat com> - 1.3.0-6
- update to 1.3.x snap r9671
- add some not-yet-accepted patches needed by tigervnc

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 07 2011 Rex Dieter <rdieter@fedoraproject.org> 1.3.0-3
- rebuild (libpng)
- pkgconfig-style deps

* Thu Aug 25 2011 Rex Dieter <rdieter@fedoraproject.org> 1.3.0-2
- fltk-config inconsistency on ARM (#733421)

* Fri Jun 24 2011 Rex Dieter <rdieter@fedoraproject.org> 1.3.0-1
- 1.3.0 (final)
- --with-links

* Fri May 27 2011 Adam Tkac <atkac redhat com> - 1.3.0-0.2.rc5
- fltk-config: don't emit unneeded -l<library> flags (#708185)

* Wed May 25 2011 Adam Tkac <atkac redhat com> - 1.3.0-0.1.rc5
- update to 1.3.0rc5
- patches no longer needed
  - fltk-1.1.9-test.patch
  - fltk-1.1.9-rpath.patch
  - fltk-1.1.10-pkgconfig_xft.patch
  - fltk-1.1.10-fluid_target.patch
- regenerated other patches to match current source

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.1.10-5
- FTBFS fltk-1.1.10-4.fc15: ImplicitDSOLinking (#660884)

* Wed Sep 29 2010 jkeating - 1.1.10-4
- Rebuilt for gcc bug 634757

* Mon Sep 20 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.1.10-3
- verbose build output (hint from mschwendt)

* Tue Sep 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.1.10-2
- drop BR: man , fixes FTBFS (#631212)

* Sun Feb 14 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.1.10-1
- fltk-1.1.10
- FTBFS fltk-1.1.10-0.1.rc3.fc13: ImplicitDSOLinking (#564877)

* Tue Dec 08 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.1.10-0.1.rc3
- fltk-1.1.10rc3

* Mon Dec 07 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.1.9-7
- real -static subpkg (#545145)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 28 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.1.9-5
- fltk-fluid duplicate .desktop file (#508553)
- optimize scriptlets

* Wed May 13 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.1.9-4
- unbreak fltk-config --ldstaticflags (#500201)
- (another?) gcc44 patch
- -devel: +Provides: %%name-static
- fix multiarch conflicts (#341141)

* Wed Mar 04 2009 Caolán McNamara <caolanm@redhat.com> - 1.1.9-3
- fix uses of strchr wrt. constness

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Oct 01 2008 Rex Dieter <rdieter@fedoraproject.org> 1.1.9-1
- fltk-1.1.9

* Sat Mar 29 2008 Rex Dieter <rdieter@fedoraproject.org> 1.1.8-1
- fltk-1.1.8 (final)

* Tue Feb 19 2008 Rex Dieter <rdieter@fedoraproject.org> 1.1.8-0.8.r6027
- fltk-1.1.x-r6027

* Mon Feb 11 2008 Rex Dieter <rdieter@fedoraproject.org> 1.1.8-0.7.r5989 
- respin (gcc43)

* Wed Dec 12 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.1.8-0.6.r5989
- --enable-largefile
- fltk-1.1.x-r5989 snapshot (1.1.8 pre-release)

* Mon Aug 20 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.1.8-0.5.r5750
- License: LGPLv2+ with exceptions

* Sat Aug 11 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.1.8-0.4.r5750
- License: LGPLv2+ (with exceptions)

* Sun Apr 29 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.1.8-0.3.r5750
- *really* fix --rpath issue, using non-empty patch this time (#238284)

* Sun Apr 29 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.1.8-0.2.r5750
- nuke --rpath (#238284)

* Thu Apr 05 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.1.8-0.1.r5750
- fltk-1.1.x-r5750 snapshot (1.1.8 pre-release)
- --enable-xinerama
- patch for undefined symbols in libfltk_gl

* Wed Apr  4 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.1.7-9.r5555
- Always apply fltk-config patch (#199656)
- Update fltk-1.1.7-config.patch

* Wed Dec 13 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.1.7-8.r5555
- more 64bit hackage to workaround broken Makefile logic (#219348)

* Wed Dec 13 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.1.7-7.r5555
- fltk-1.1.x-r5555 snapshot, for 64bit issues (#219348)
- restore static libs (they're tightly coupled with fltk-config)
- cleanup %%description's

* Mon Dec 11 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.1.7-6
- move tests to %%check section

* Mon Dec 11 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.1.7-5
- use included icon/.desktop files
- fix up fltk-config (#199656)

* Mon Dec 11 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.1.7-3
- follow icon spec
- omit static libs

* Wed Sep 06 2006 Michael J. Knox <michael[AT]knox.net.nz> - 1.1.7-2
- rebuild for FC6

* Mon Feb 13 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.1.7-1
- Upstream update

* Thu Nov 17 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.1.6-4
- Fixed BR and -devel Requires for modular X

* Sun Nov 13 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.1.6-3
- Update BuildRequires as well

* Sun Nov 13 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.1.6-2
- Update Requires for -devel

* Thu Oct 27 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.1.6-1
- Upstream update

* Thu Aug 18 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.1.4-10
- Fixed BR/Requires for x86_64

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Nov 20 2003 Dams <anvil[AT]livna.org> 0:1.1.4-0.fdr.8
- Hopefully fixed Xft flags for rh80

* Thu Nov 20 2003 Dams <anvil[AT]livna.org> 0:1.1.4-0.fdr.7
- Fixed typo

* Thu Nov 20 2003 Dams <anvil[AT]livna.org> 0:1.1.4-0.fdr.6
- Added xft.pc build dependency
- Added BuildReq:man

* Sun Nov  9 2003 Ville Skyttä <ville.skytta@iki.fi> 0:1.1.4-0.fdr.4
- Spec file cleanup
- Enabled xft and threads

* Tue Oct 28 2003 Dams <anvil[AT]livna.org> - 0:1.1.4-0.fdr.3
- Added missing symlink in includedir

* Wed Oct  1 2003 Dams <anvil[AT]livna.org> 0:1.1.4-0.fdr.2
- Removed comment after scriptlets

* Wed Oct  1 2003 Dams <anvil[AT]livna.org> 0:1.1.4-0.fdr.1
- Updated to final 1.1.4

* Wed Sep 24 2003 Dams <anvil[AT]livna.org> 0:1.1.4-0.fdr.0.4.rc1
- Fixed documentation path in configure

* Fri Aug 29 2003 Dams <anvil[AT]livna.org> 0:1.1.4-0.fdr.0.3.rc1
- Fixed typo in desktop entry
- Added missing BuildRequires ImageMagick and desktop-file-utils

* Fri Aug 29 2003 Dams <anvil[AT]livna.org> 0:1.1.4-0.fdr.0.2.rc1
- Moved fluid to its own package
- Added missing Requires for devel package

* Sat Aug 16 2003 Dams <anvil[AT]livna.org>
- Initial build.
