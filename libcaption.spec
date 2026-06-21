#
# Conditional build:
%bcond_without	apidocs		# API documentation
#
Summary:	Free open-source CEA608 / CEA708 closed-caption encoder/decoder
Summary(pl.UTF-8):	Wolnodostępny koder/dekoder napisów CEA608/CEA708 o otwartych źródłach
Name:		libcaption
Version:	0.8
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/szatmary/libcaption/releases
Source0:	https://github.com/szatmary/libcaption/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	44e9f042653abf2333ae94f58bdc0a61
URL:		https://github.com/szatmary/libcaption
BuildRequires:	cmake >= 2.8
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcaption is a library written in C to aid in the creating and
parsing of closed caption data, open sourced under the MIT license to
use within community developed broadcast tools. To maintain
consistency across platforms libcaption aims to implement a subset of
EIA608, CEA708 as supported by the Apple iOS platform.

%description -l pl.UTF-8
libcaption to napisana w C biblioteka, pomagająca przy tworzeniu i
analizie danych napisów, wydana z otwartymi źródłami na licencji MIT z
myślą o użyciu w narzędziach nadawczych rozwijanych przez społeczność.
Aby zapewnić spójność między platformami, libcaption ma na celu
implementację podzbioru EIA608, CEA708, obsługiwanego przez platformę
Apple iOS.

%package devel
Summary:	Header files for libcaption library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcaption
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libcaption library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcaption.

%package apidocs
Summary:	API documentation for libcaption library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libcaption
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for libcaption library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libcaption.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%if %{with apidocs}
%{__make} doc
cd ..
# remove empty dirs
rmdir docs/html/d?/d?? || :
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.md
%attr(755,root,root) %{_bindir}/flv+scc
%attr(755,root,root) %{_bindir}/flv+srt
%attr(755,root,root) %{_bindir}/flv2srt
%attr(755,root,root) %{_bindir}/party
%attr(755,root,root) %{_bindir}/rollup
%attr(755,root,root) %{_bindir}/scc2srt
%attr(755,root,root) %{_bindir}/scc2vtt
%attr(755,root,root) %{_bindir}/sccdump
%attr(755,root,root) %{_bindir}/srt2vtt
%attr(755,root,root) %{_bindir}/srtdump
%attr(755,root,root) %{_bindir}/ts2srt
%attr(755,root,root) %{_bindir}/vttdump
%attr(755,root,root) %{_bindir}/vttsegmenter
%{_libdir}/libcaption.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/caption

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc docs/html/*
%endif
