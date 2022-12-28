#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-cachecontrol
Version  : 0.12.12
Release  : 18
URL      : https://files.pythonhosted.org/packages/06/80/1f8ba1ced5f29514d8621003b2b0fb404ed88996e963dbca7f519ecc82ca/CacheControl-0.12.12.tar.gz
Source0  : https://files.pythonhosted.org/packages/06/80/1f8ba1ced5f29514d8621003b2b0fb404ed88996e963dbca7f519ecc82ca/CacheControl-0.12.12.tar.gz
Summary  : httplib2 caching for requests
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-cachecontrol-bin = %{version}-%{release}
Requires: pypi-cachecontrol-license = %{version}-%{release}
Requires: pypi-cachecontrol-python = %{version}-%{release}
Requires: pypi-cachecontrol-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(msgpack)
BuildRequires : pypi(requests)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
..
SPDX-License-Identifier: Apache-2.0
==============
CacheControl
==============

%package bin
Summary: bin components for the pypi-cachecontrol package.
Group: Binaries
Requires: pypi-cachecontrol-license = %{version}-%{release}

%description bin
bin components for the pypi-cachecontrol package.


%package license
Summary: license components for the pypi-cachecontrol package.
Group: Default

%description license
license components for the pypi-cachecontrol package.


%package python
Summary: python components for the pypi-cachecontrol package.
Group: Default
Requires: pypi-cachecontrol-python3 = %{version}-%{release}

%description python
python components for the pypi-cachecontrol package.


%package python3
Summary: python3 components for the pypi-cachecontrol package.
Group: Default
Requires: python3-core
Provides: pypi(cachecontrol)
Requires: pypi(msgpack)
Requires: pypi(requests)

%description python3
python3 components for the pypi-cachecontrol package.


%prep
%setup -q -n CacheControl-0.12.12
cd %{_builddir}/CacheControl-0.12.12
pushd ..
cp -a CacheControl-0.12.12 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672261224
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cachecontrol
cp %{_builddir}/CacheControl-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-cachecontrol/29bee62daa11fe00707573e32779de8b2dc12cb5 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
## Remove excluded files
rm -f %{buildroot}*/usr/lib/python3*/site-packages/tests/*/*
## install_append content
rm -rf %{buildroot}/usr/lib/python*/site-packages/tests/
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/doesitcache

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cachecontrol/29bee62daa11fe00707573e32779de8b2dc12cb5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
