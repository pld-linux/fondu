Summary:	Converts between Mac and Unix fonts
Summary(pl.UTF-8):   Różne narzędzia do operowania na fontach Type 1 i 2
Name:		fondu
Version:	060102
Release:	1
License:	BSD
Group:		Applications/File
Source0:	http://fondu.sourceforge.net/%{name}_src-%{version}.tgz
# Source0-md5:	e20861beacddc1ab392bef7813641bf8
URL:		http://fondu.sourceforge.net/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fondu allows you to convert a Mac font into a Unix one. ufond converts
a Unix font into a Mac one.

%description -l pl.UTF-8
fondu pozwala konwertować fonty macowe na uniksowe. ufond konwertuje
fonty uniksowe na macowe.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install *.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
