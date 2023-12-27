Summary:	Parsing Expression Grammar Template Library
Name:		PEGTL
Version:	3.2.7
Release:	1
License:	Boost v1.0
Group:		Libraries
Source0:	https://github.com/taocpp/PEGTL/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	31b14660c883bc0489ddcdfbd29199c9
URL:		https://github.com/taocpp/PEGTL
BuildRequires:	cmake >= 3.8
BuildRequires:	libstdc++-devel >= 6:8
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Parsing Expression Grammar Template Library (PEGTL) is a
zero-dependency C++ header-only parser combinator library for creating
parsers according to a Parsing Expression Grammar (PEG).

%package devel
Summary:	Parsing Expression Grammar Template Library
Group:		Development/Libraries
Requires:	libstdc++-devel >= 6:8
BuildArch:	noarch

%description devel
The Parsing Expression Grammar Template Library (PEGTL) is a
zero-dependency C++ header-only parser combinator library for creating
parsers according to a Parsing Expression Grammar (PEG).

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DPEGTL_INSTALL_INCLUDE_DIR:PATH="%{_includedir}" \
	-DPEGTL_INSTALL_CMAKE_DIR:PATH="%{_datadir}/cmake/pegtl" \
	-DPEGTL_BUILD_EXAMPLES:BOOL=OFF \
	-DPEGTL_BUILD_TESTS:BOOL=OFF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc LICENSE README.md
%{_includedir}/tao
%{_datadir}/cmake/pegtl
