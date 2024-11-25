%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-fr
Summary: French hunspell dictionaries
Version: 6.2
Release: 17%{?dist}
Source: http://www.dicollecte.org/download/fr/hunspell-french-dictionaries-v%{version}.zip
URL: http://www.dicollecte.org/home.php?prj=fr
License: MPL-2.0
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-fr)

%description
French (France, Belgium, etc.) hunspell dictionaries.

%prep
%setup -q -c -n hunspell-fr

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p fr-toutesvariantes.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/fr_FR.dic
cp -p fr-toutesvariantes.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/fr_FR.aff

pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
fr_FR_aliases="fr_BE fr_CA fr_CH fr_LU fr_MC"
for lang in $fr_FR_aliases; do
	ln -s fr_FR.aff $lang.aff
	ln -s fr_FR.dic $lang.dic
done
popd


%files
%doc README_dict_fr.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 22 2023 Caolán McNamara <caolanm@redhat.com> - 6.0.2-13
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Mar 22 2022 Parag Nemade <pnemade AT redhat DOT com> - 6.2-10
- Add conditional for new hunspell dir path and update to Requires:
  hunspell-filesystem

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb  7 2018 Remi Collet <remi@fedoraproject.org> - 6.2-1
- update to 6.2

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 Caolán McNamara <caolanm@redhat.com> - 6.0.2-1
- latest version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 19 2016 Parag Nemade <pnemade AT redhat DOT com> - 4.6-8
- Add Supplements: tag for langpacks naming guidelines
- Clean the specfile to follow current packaging guidelines

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 02 2012 Caolán McNamara <caolanm@redhat.com> - 4.6-2
- licences is mplv2.0 now

* Wed Sep 12 2012 Caolán McNamara <caolanm@redhat.com> - 4.6-1
- latest version

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 14 2012 Caolán McNamara <caolanm@redhat.com> - 4.5-1
- latest version

* Fri Mar 09 2012 Caolán McNamara <caolanm@redhat.com> - 4.4.1-1
- latest version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Caolán McNamara <caolanm@redhat.com> - 4.3-1
- latest version

* Fri Apr 08 2011 Caolán McNamara <caolanm@redhat.com> - 4.2-1
- latest version

* Sat Apr 02 2011 Caolán McNamara <caolanm@redhat.com> - 4.1-1
- latest version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 20 2011 Caolán McNamara <caolanm@redhat.com> - 4.0.1-1
- latest version

* Sun Jan 09 2011 Caolán McNamara <caolanm@redhat.com> - 4.0-1
- latest version

* Mon Aug 09 2010 Caolán McNamara <caolanm@redhat.com> - 3.8-1
- latest version

* Wed May 05 2010 Caolán McNamara <caolanm@redhat.com> - 3.7-1
- latest version

* Tue Jan 26 2010 Caolán McNamara <caolanm@redhat.com> - 3.5-1
- latest version

* Thu Oct 01 2009 Caolán McNamara <caolanm@redhat.com> - 3.4.1-1
- latest version

* Fri Sep 11 2009 Caolán McNamara <caolanm@redhat.com> - 3.4-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Caolán McNamara <caolanm@redhat.com> - 3.2-1
- latest version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 02 2008 Caolán McNamara <caolanm@redhat.com> - 2.3.2-1
- latest version

* Tue Apr 22 2008 Caolán McNamara <caolanm@redhat.com> - 2.3.1-1
- latest version

* Mon Mar 10 2008 Caolán McNamara <caolanm@redhat.com> - 2.2.0-1
- latest version

* Thu Feb 07 2008 Caolán McNamara <caolanm@redhat.com> - 2.1.0-1
- latest version

* Fri Dec 21 2007 Caolán McNamara <caolanm@redhat.com> - 2.0.5-1
- project moved to http://dico.savant.free.fr and a new release

* Fri Aug 03 2007 Caolán McNamara <caolanm@redhat.com> - 0.20060915-2
- clarify license version

* Thu Dec 07 2006 Caolán McNamara <caolanm@redhat.com> - 0.20060915-1
- initial version
