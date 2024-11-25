%define	_bindir	/bin

Summary: A utility for configuring serial ports
Name: setserial
Version: 2.17
Release: 61%{?dist}
Source: https://sourceforge.net/projects/setserial/files/setserial/%{version}/%{name}-%{version}.tar.gz
Patch0: setserial-2.17-fhs.patch
Patch1: setserial-2.17-rc.patch
Patch2: setserial-2.17-readme.patch
Patch3: setserial-2.17-spelling.patch
Patch4: setserial-hayesesp.patch
Patch5: setserial-aarch64.patch
Patch6: setserial-configure-c99.patch
Patch7: setserial-c99.patch
License: GPL-1.0-or-later
URL: http://setserial.sourceforge.net/
ExcludeArch: s390 s390x

BuildRequires: make
BuildRequires: gcc
BuildRequires: groff

%description
Setserial is a basic system utility for displaying or setting serial
port information. Setserial can reveal and allow you to alter the I/O
port and IRQ that a particular serial device is using, and more.

%prep
%setup -q
# Use FHS directory layout.
%patch -P0 -p1 -b .fhs

# Fixed initscript.
%patch -P1 -p1 -b .rc

# Corrected readme file.
%patch -P2 -p1 -b .readme

# Fixed spelling in help output.
%patch -P3 -p1 -b .spelling

# Don't require hayesesp.h (bug #564947).
%patch -P4 -p1 -b .hayesesp
rm -f config.cache

# Support aarch64 (bug #926522).
%patch -P5 -p1 -b .aarch64
%patch -P6 -p1
%patch -P7 -p1

%build
%set_build_flags
# Makefile expects CFLAGS to contain linker flags.
CFLAGS="$CFLAGS $LDFLAGS"
%configure
make %{?_smp_mflags}

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}/%{_mandir}/man8
make install DESTDIR=${RPM_BUILD_ROOT}

%files
%doc README rc.serial
%{_bindir}/setserial
%{_mandir}/man*/*

%changelog
* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 08 2024 Than Ngo <than@redhat.com> - 2.17-60
- Migrate to SPDX license

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 13 2023 Florian Weimer <fweimer@redhat.com> - 2.17-57
- Port to C99

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Tim Waugh <twaugh@redhat.com> - 2.17-47
- Build requires gcc (bug #1606335).

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 05 2018 Than Ngo <than@redhat.com> - 2.17-45
- fixed typo

* Thu Jul 05 2018 Than Ngo <than@redhat.com> - 2.17-44
- fixed source url

* Sun Feb 25 2018 Florian Weimer <fweimer@redhat.com> - 2.17-43
- Use LDFLAGS from redhat-rpm-config

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Tim Waugh <twaugh@redhat.com> 2.17-33
- Support aarch64 (bug #926522).

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep 21 2012 Tim Waugh <twaugh@redhat.com> 2.17-31
- Fixed source URL.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Mar  3 2010 Tim Waugh <twaugh@redhat.com> 2.17-26
- Added comments for all patches.

* Mon Feb 15 2010 Tim Waugh <twaugh@redhat.com> 2.17-25
- Don't require hayesesp.h (bug #564947).

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 11 2008 Tim Waugh <twaugh@redhat.com> 2.17-22
- Rebuild for GCC 4.3.

* Wed Aug 29 2007 Tim Waugh <twaugh@redhat.com> 2.17-21
- More specific license tag.

* Wed Feb  7 2007 Tim Waugh <twaugh@redhat.com> 2.17-20
- Fixed mandir in fhs patch (bug #226411).
- Don't run strip (bug #226411).
- Fixed readme patch to talk about Fedora not Red Hat Linux (bug #226411).
- Fixed build root tag (bug #226411).
- Use SMP make flags (bug #226411).
- Avoid %%makeinstall (bug #226411).
- Fixed summary (bug #226411).

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.17-19.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.17-19.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.17-19.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar  2 2005 Tim Waugh <twaugh@redhat.com> 2.17-19
- Rebuild for new GCC.

* Wed Feb  9 2005 Tim Waugh <twaugh@redhat.com> 2.17-18
- Rebuilt.

* Mon Oct 11 2004 Tim Waugh <twaugh@redhat.com> 2.17-17
- Spec file tidying by Robert Scheck (bug #135182).

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Nov 27 2003 Tim Waugh <twaugh@redhat.com> 2.17-14
- Build requires groff (bug #111088).

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Jan 10 2003 Tim Waugh <twaugh@redhat.com> 2.17-11
- Fix spelling mistake (bug #80896).

* Wed Nov 20 2002 Tim Powers <timp@redhat.com> 2.17-10
- rebuild in current collinst

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Apr 22 2002 Tim Waugh <twaugh@redhat.com> 2.17-7
- Don't strip binaries explicitly (bug #62566).

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Sep 11 2001 Tim Waugh <twaugh@redhat.com> 2.17-5
- Fix init script (bug #52862).
- Avoid temporary file vulnerability in init script.
- Update README: it's --add, not -add.

* Tue Jun 19 2001 Florian La Roche <Florian.LaRoche@redhat.de> 2.17-4
- add ExcludeArch: s390 s390x

* Wed May 30 2001 Tim Waugh <twaugh@redhat.com> 2.17-3
- Sync description with specspo.

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com> 2.17-2
- automatic rebuild

* Wed Jun 14 2000 Jeff Johnson <jbj@redhat.com>
- update to 2.17.
- FHS packaging.

* Mon Feb  7 2000 Jeff Johnson <jbj@redhat.com>
- compress man pages.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Thu Feb 11 1999 Michael Maher <mike@redhat.com>
- fixed bug #363

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Sat Jun 20 1998 Jeff Johnson <jbj@redhat.com>
- upgraded to 2.1.14

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- pulled into distribution
- used setserial-2.12_CTI.tgz instead of setserial-2.12.tar.gz (former is
  all that sunsite has) - not sure what the difference is.

* Thu Sep 25 1997 Christian 'Dr. Disk' Hechelmann <drdisk@ds9.au.s.shuttle.de>
- added %%attr's
- added sanity check for RPM_BUILD_ROOT
- setserial is now installed into /bin, where util-linux puts it and all
  startup scripts expect it.
