Summary:	Converts between mac and unix fonts
Summary(pl):	R�ne narz�dzia do operowania na fontach Type 1 i 2
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
fondu allows you to convert a mac font into a unix one. ufond converts
a unix font into a mac one.

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
