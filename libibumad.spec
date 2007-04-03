
%define RELEASE 0.6.20070403git
%define rel %{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}

Summary: OpenIB InfiniBand Management and Diagnostic Tools
Name: libibumad
Version: 1.0.2
Release: %rel%{?dist}
License: GPL/BSD
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source: git://git.openfabrics.org/~halr/management/libibumad-git.tgz
Url: http://openfabrics.org
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires: libibcommon-devel, autoconf, libtool, automake

%description
libibumad provides the user MAD library functions which sit on top of 
the user MAD modules in the kernel. These are used by the IB diagnostic
and management tools, including OpenSM. 

%package devel
Summary: Development files for the libibumad library
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release} libibcommon-devel
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description devel
Development files for the libibumad library.

%package static
Summary: Static version of the libibumad library
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description static
Static version of the libibumad library.

%prep
%setup -q

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
make DESTDIR=${RPM_BUILD_ROOT} install
# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/libibumad*.so.*
%doc AUTHORS COPYING ChangeLog 

%files devel
%defattr(-,root,root)
%{_libdir}/libibumad.so
%{_includedir}/infiniband/*.h

%files static
%defattr(-,root,root)
%{_libdir}/libibumad.a
