%define __cmake_in_source_build 1
%global rocm_release 6.2
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}
Name:           hsakmt
Version:        1.0.6
Release:        45.rocm%{rocm_version}%{?dist}
Summary:        AMD HSA thunk library

License:        MIT
URL:            https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface
Source0:        https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/archive/rocm-%{rocm_version}.tar.gz#/%{name}-rocm-%{rocm_version}.tar.gz
# https://github.com/ROCm/ROCT-Thunk-Interface/pull/108
Patch1:         0001-Improve-finding-rocm-smi.patch

# Fedora builds AMD HSA kernel support for these 64bit targets:
ExclusiveArch: x86_64 aarch64 ppc64le
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires: rocm-llvm-devel
BuildRequires: rocm-compilersupport-macros
BuildRequires: cmake
BuildRequires: pciutils-devel
BuildRequires: libdrm-devel
BuildRequires: numactl-devel

%if 0%{?epel} == 7
# We still the original cmake package on epel, because it provides the
# %%cmake macro.
BuildRequires: cmake3
%global __cmake %{_bindir}/cmake3
%endif

%description
This package includes the libhsakmt (HSA thunk) libraries for AMD KFD

%package -n kfdtest
Summary: Test suite for ROCm's KFD kernel module
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: rocm-smi

%description -n kfdtest
This package includes ROCm's KFD kernel module test suite (kfdtest), the list of
excluded tests for each ASIC, and a convenience script to run the test suite.

%package devel
Summary: AMD HSA thunk library development package
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: hsakmt(rocm) = %{rocm_release}

%description devel
Development library for the libhsakmt (HSA thunk) libraries for AMD KFD

%prep
%autosetup -n  ROCT-Thunk-Interface-rocm-%{rocm_version} -p1

# Allow us to build kfdtest at the same time as hsakmt using LIBHSAKMT_PATH
# The CMake logic assumes hsakmt is an installed library
sed -i "s/{HSAKMT_LIBRARY_DIRS}/{LIBHSAKMT_PATH}/" tests/kfdtest/CMakeLists.txt
# Fix kfdtest install permission
sed -i "s/GROUP_WRITE//" tests/kfdtest/CMakeLists.txt

%build
LLVM_CMAKEDIR=`llvm-config-%{rocmllvm_version} --cmakedir`
if [ ! -d ${LLVM_CMAKEDIR} ]; then
    echo "Something wrong with llvm-config"
    false
fi

mkdir build build-kfdtest
cd build

%cmake .. -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build
export LIBHSAKMT_PATH=$(pwd)

cd ../build-kfdtest
%cmake ../tests/kfdtest -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_SKIP_RPATH=ON -DLLVM_DIR=${LLVM_CMAKEDIR}
%cmake_build

%install
cd build
%cmake_install

cd ../build-kfdtest
%cmake_install

# We install this via license macro instead:
rm %{buildroot}%{_docdir}/hsakmt/LICENSE.md

%ldconfig_scriptlets

%files
%doc README.md
%license LICENSE.md
%{_libdir}/libhsakmt.so.%{version}
%{_libdir}/libhsakmt.so.1

%files -n kfdtest
%doc tests/kfdtest/README.txt
%license tests/kfdtest/LICENSE.kfdtest
%{_bindir}/kfdtest
%{_bindir}/run_kfdtest.sh
%{_datadir}/kfdtest

%files devel
%{_libdir}/libhsakmt.so
%{_includedir}/hsakmt
%{_libdir}/cmake/hsakmt/
%{_libdir}/pkgconfig/libhsakmt.pc
# Fedora doesn't want static libs:
%exclude %{_libdir}/libhsakmt-staticdrm.a

%changelog
* Mon Oct 7 2024 Tom Rix <Tom.Rix@amd.com> - 1.0.6-45.rocm6.2.0
- Need some help to find llvm

* Mon Sep 23 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-44.rocm6.2.0
- Update to ROCm 6.2.1

* Fri Aug 30 2024 Tom Rix <Tom.Rix@amd.com> - 1.0.6-43.rocm6.2.0
- Improve finding rocm-smi for kfdtest

* Thu Aug 29 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-42.rocm6.2.0
- Add kfdtest package

* Fri Aug 09 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-41.rocm6.2.0
- Fix 6.2 issue with non-static hsakmt

* Fri Aug 02 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-40.rocm6.2.0
- Update to ROCm 6.2

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-40.rocm6.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May 09 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-39.rocm6.1.1
- Update to ROCm 6.1.1

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-38.rocm6.0.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-37.rocm6.0.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 19 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-36.rocm6.0.0
- Add symbol patch to fix dynamic linking

* Thu Dec 14 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-35.rocm6.0.0
- Update to ROCm 6.0

* Tue Oct 03 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-34.rocm5.7.0
- Re-enable LTO, it looks like it wasn't the issue
- Cherry-pick patch from archlinux to fix 5.7 issue

* Tue Sep 19 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-33.rocm5.7.0
- Disable LTO, as it causes a few symbols to get stripped in 5.7

* Sun Sep 17 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-32.rocm5.7.0
- Update to 5.7

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-31.rocm5.6.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-30.rocm5.6.0
- Update to 5.6

* Mon May 01 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-29.rocm5.5.0
- Update to 5.5

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-28.rocm5.4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 18 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-27.rocm5.4.1
- Update to 5.4.1

* Mon Oct 03 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-26.rocm5.3.0
- Update to 5.3.0

* Sun Jul 24 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-25.rocm5.2.1
- Update to 5.2.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-24.rocm5.2.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 03 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-23.rocm5.2.0
- Update to 5.2.0

* Sat Apr 09 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-22.rocm5.1.1
- Update to ROCm version 5.1.1

* Tue Apr 05 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-21.rocm5.1.0
- Enable ppc64le

* Thu Mar 31 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-20.rocm5.1.0
- Update to ROCm version 5.1.0

* Fri Feb 11 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-19.rocm5.0.0
- Update to ROCm version 5.0.0
- General improvements to spec file

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-18.rocm3.9.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-17.rocm3.9.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-16.rocm3.9.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Philipp Knechtges <philipp-dev@knechtges.com> - 1.0.6-15.rocm3.9.0
- Update to ROCm version 3.9.0

* Wed Sep 23 2020 Jeff Law <law@redhat.com> - 1.0.6-14.rocm3.5.0
- Use cmake_in_source_build to fix FTBFS due to recent cmake macro changes

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-13.rocm3.5.0
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-12.rocm3.5.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Tom Stellard <tstellar@redhat.com> - 1.0.6-11.rocm3.5.0
- ROCm 3.5.0 Release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-10.rocm2.0.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-9.rocm2.0.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-8.rocm2.0.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Tom Stellard <tstellar@redhat.com> - 1.0.6-7.rocm2.0.0
- ROCm 2.0.0 Release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-6.20171026git172d101
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 23 2018 Tom Stellard <tstellar@redhat.com> - 1.0.6-5.20171026git172d101
- Fix build for epel7

* Mon Feb 12 2018 Tom Stellard <tstellar@redhat.com> - 1.0.6-4.20171026git172d101
- Fix build flag injection
- rhbz#1543787

* Fri Feb 09 2018 Tom Stellard <tstellar@redhat.com> - 1.0.6-3.20171026git172d101
- Build for aarch64

* Mon Feb 05 2018 Tom Stellard <tstellar@redhat.com> - 1.0.6-2.20171026git172d101
- Fix build with gcc 8

* Thu Oct 26 2017 Tom Stellard <tstellar@redhat.com> - 1.0.6-1.20171026git172d101
- Update with latest code from https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 13 2015 Oded Gabbay <oded.gabbay@gmail.com> 1.0.0-5
- Don't build for arm and i686

* Fri Nov 13 2015 Oded Gabbay <oded.gabbay@gmail.com> 1.0.0-4
- Rename package back to hsakmt

* Sun Nov 1 2015 Oded Gabbay <oded.gabbay@gmail.com> 1.0.0-3
- Rename package to libhsakmt

* Thu Oct 29 2015 Oded Gabbay <oded.gabbay@gmail.com> 1.0.0-2
- Changed doc to license
- Added GPLv2 to license
- Changed RPM_BUILD_ROOT to {buildroot}

* Sat Oct 24 2015 Oded Gabbay <oded.gabbay@gmail.com> 1.0.0-1
- Initial release of hsakmt, ver. 1.0.0

