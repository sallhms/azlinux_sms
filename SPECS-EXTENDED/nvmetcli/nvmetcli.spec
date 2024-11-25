Name:           nvmetcli
License:        Apache-2.0
Summary:        An adminstration shell for NVMe storage targets
Version:        0.7
Release:        15%{?dist}
URL:            ftp://ftp.infradead.org/pub/nvmetcli/
Source:         ftp://ftp.infradead.org/pub/nvmetcli/%{name}-%{version}.tar.gz
Patch00:        0001-nvmetcli-don-t-remove-ANA-Group-1-on-clear.patch
Patch01:        0002-README-Update-URL-for-configshell-fb.patch
Patch02:        0003-nvmetcli-Improve-IOError-handling-on-restore.patch
Patch03:        0004-nvme.py-Explicit-close-is-redundant.patch
Patch04:        0005-nvme.py-Sync-the-containing-directory.patch
Patch05:        0006-nvme.py-Make-modprobe-work-for-kmod-lib-too.patch
Patch06:        0007-test_nvmet.py-test_invalid_input-fails-for-py3.patch
Patch07:        0008-nvmetcli-Report-save-name-correctly.patch
Patch08:        0009-nvmetcli-Allow-different-devices-for-make-test.patch
Patch09:        0010-nvmetcli-Correct-xrange-usage-for-py3.patch
Patch10:        0011-nvmetcli-add-a-tcp-example-json.patch
Patch11:        0012-Documentation-fix-typo.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  python3-devel python3-setuptools systemd-units asciidoc xmlto
Requires:       python3-configshell python3-kmod
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
This package contains the command line interface to the NVMe over Fabrics
nvmet in the Linux kernel.  It allows configuring the nvmet interactively
as well as saving / restoring the configuration to / from a json file.

%prep
%autosetup -p1

%build
%{__python3} setup.py build
cd Documentation
make
gzip --stdout nvmetcli.8 > nvmetcli.8.gz

%install
%{__python3} setup.py install --skip-build --root %{buildroot}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/nvmet
install -m 644 nvmet.service %{buildroot}%{_unitdir}/nvmet.service
mkdir -p %{buildroot}%{_mandir}/man8/
install -m 644 Documentation/nvmetcli.8.gz %{buildroot}%{_mandir}/man8/

%post
%systemd_post nvmet.service

%preun
%systemd_preun nvmet.service

%postun
%systemd_postun_with_restart nvmet.service

%files
%{python3_sitelib}/*
%dir %{_sysconfdir}/nvmet
%{_sbindir}/nvmetcli
%{_unitdir}/nvmet.service
%doc README
%license COPYING
%{_mandir}/man8/nvmetcli.8.gz

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.7-14
- Rebuilt for Python 3.13

* Tue Feb 13 2024 Maurizio Lombardi <mlombard@redhat.com> - 0.7-13
- Migrate to SPDX License

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.7-9
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.7-6
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.7-3
- Rebuilt for Python 3.10

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Thu Feb 11 2021 Maurizio Lombardi <mlombard@redhat.com> - 0.7-1
- Rebase to the latest version (git commit id 297f40aef117875d98303b0535fb076626b91a19)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4-11
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4-8
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4-4
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 9 2017 Andy Grover <agrover@redhat.com> - 0.4-1
- Update for new upstream release
- Remove fix-setup.patch

* Tue Feb 21 2017 Andy Grover <agrover@redhat.com> - 0.3-1
- Update for new upstream release

* Wed Oct 12 2016 Andy Grover <agrover@redhat.com> - 0.2-1
- Initial packaging
