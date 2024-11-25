%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-et
Summary: Estonian hunspell dictionaries
%global upstreamid 20030606
Version: 0.%{upstreamid}
Release: 35%{?dist}
Source: http://www.meso.ee/~jjpp/speller/ispell-et_%{upstreamid}.tar.gz
URL: http://www.meso.ee/~jjpp/speller/
License: LGPL-2.1-or-later AND LPPL-1.3a
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-et)
Provides: hunspell-ee = 0.20030606-4
Obsoletes: hunspell-ee < 0.20030606-4

%description
Estonian hunspell dictionaries.

%package -n hyphen-et
Requires: hyphen
Summary: Estonian hyphenation rules
Supplements: (hyphen and langpacks-et)

%description -n hyphen-et
Estonian hyphenation rules.

%prep
%setup -q -n ispell-et-%{upstreamid}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p latin-1/et_EE.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_et.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_et_EE.dic


%files
%doc README COPYRIGHT ChangeLog
%{_datadir}/%{dict_dirname}/*

%files -n hyphen-et
%doc README COPYRIGHT ChangeLog
%{_datadir}/hyphen/*

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20030606-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20030606-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20030606-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20030606-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 22 2023 Caolán McNamara <caolanm@redhat.com> - 0.20030606-31
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20030606-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20030606-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Mar 22 2022 Parag Nemade <pnemade AT redhat DOT com> - 0.20030606-28
- Add conditional for new hunspell dir path and update to Requires:
  hunspell-filesystem

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20030606-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20030606-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20030606-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20030606-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20030606-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20030606-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20030606-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20030606-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.20030606-19
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20030606-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20030606-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20030606-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 19 2016 Parag Nemade <pnemade AT redhat DOT com> - 0.20030606-15
- Add Supplements: tag for langpacks naming guidelines
- Clean the specfile to follow current packaging guidelines

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.20030606-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20030606-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20030606-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20030606-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20030606-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20030606-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20030606-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20030606-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 08 2010 Caolán McNamara <caolanm@redhat.com> - 0.20030606-6
- add Changelog to %%doc

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20030606-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 30 2009 Caolán McNamara <caolanm@redhat.com> - 0.20030606-4
- erroneously imported as hunspell-ee, rename as hunspell-et

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20030606-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 23 2007 Caolán McNamara <caolanm@redhat.com> - 0.20030606-2
- package hyphenation rules

* Fri Nov 23 2007 Caolán McNamara <caolanm@redhat.com> - 0.20030606-1
- canonical upstream tarball

* Thu Aug 09 2007 Caolán McNamara <caolanm@redhat.com> - 0.20030602-2
- clarify license

* Thu Dec 07 2006 Caolán McNamara <caolanm@redhat.com> - 0.20030602-1
- initial version
