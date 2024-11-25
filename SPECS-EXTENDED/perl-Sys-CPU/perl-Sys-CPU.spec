Name:           perl-Sys-CPU
Version:        0.61
Release:        38%{?dist}
Summary:        Getting CPU information

# Some code was copied from Unix::Processors, which is LGPL-3.0-only OR Artistic-2.0
# The rest of the code is under the standard Perl license (GPL-1.0-or-later OR Artistic-1.0-Perl).
# See <https://bugzilla.redhat.com/show_bug.cgi?id=585336>.
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND (LGPL-3.0-only OR Artistic-2.0)
URL:            https://metacpan.org/release/Sys-CPU
Source0:        https://cpan.metacpan.org/authors/id/M/MZ/MZSANFORD/Sys-CPU-%{version}.tar.gz
# Support cpu_type on ARM and AArch64, bug #1093266, CPAN RT#95400
Patch0:         Sys-CPU-0.61-Add-support-for-cpu_type-on-ARM-and-AArch64-Linux-pl.patch
# Accept undefined cpu_clock on ARM and AArch64, bug #1093266, CPAN RT#95400
Patch1:         Sys-CPU-0.61-cpu_clock-can-be-undefined-on-an-ARM.patch
# Add support for RISC-V 64-bit (RV64GC) aka riscv64
Patch2:         add-support-riscv64.patch
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)

%{?perl_default_filter}

%description
Perl extension for getting CPU information. 
Currently only number of CPU's supported.

%prep
%setup -q -n Sys-CPU-%{version}
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
sed -i 's/\r//' Changes README

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test TEST_VERBOSE=1

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name CPU.bs -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Sys/*
%{_mandir}/man3/*.3*


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.61-37
- Perl 5.40 rebuild

* Wed Feb 21 2024 David Abdurachmanov <davidlt@rivosinc.com> - 0.61-36
- Add support for riscv64

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.61-32
- Perl 5.38 rebuild

* Thu Jun 01 2023 Michal Josef Špaček <mspacek@redhat.com> - 0.61-31
- Fix %patch macro
- Update license to SPDX format

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.61-28
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.61-25
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.61-22
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.61-19
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.61-16
- Perl 5.28 rebuild

* Sun Mar 11 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.61-15
- Add missing build-requirements

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.61-11
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.61-9
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.61-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.61-6
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.61-5
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.61-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Petr Pisar <ppisar@redhat.com> - 0.61-3
- Support cpu_type on ARM and AArch64 (bug #1093266)
- Accept undefined cpu_clock on ARM and AArch64 (bug #1093266)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.61-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 23 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.61-1
- Update to 0.61
- Drop unneeded macros
- Fix incorrect dates in changelog
- Disable test 3 (which fails on arm)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.54-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.54-4
- Perl 5.18 rebuild

* Fri Apr 19 2013 Shakthi Kannan <shakthimaan@fedoraproject.org> - 0.54-3
- Disable cpu_type test

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Petr Pisar <ppisar@redhat.com> - 0.54-1
- 0.54 bump

* Mon Nov 05 2012 Petr Pisar <ppisar@redhat.com> - 0.52-2
- Add support for s390 (CPAN RT #80633)

* Fri Nov 02 2012 Petr Pisar <ppisar@redhat.com> - 0.52-1
- 0.52 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.51-9
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 05 2011 Shakthi Kannan <shakthimaan@fedoraproject.org> - 0.51-7
- Used perl_vendorarch/auto, perl_vendorarch/Sys in files section.

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.51-6
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.51-4
- 661697 rebuild for fixing problems with vendorach/lib

* Sun Jun 27 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.51-3
- Rebuild for perl-5.12.1.

* Mon May 03 2010 Shakthi Kannan <shakthimaan [AT] gmail dot com> 0.51-2
- Updated license to (GPL+ or Artistic) and (LGPLv3 or Artistic 2.0)

* Fri Apr 23 2010 Shakthi Kannan <shakthimaan [AT] gmail dot com> 0.51-1
- Initial Fedora RPM version
