Summary:	Akanga shell
Summary(pl):	Akanga shell
Name:		akanga
Version:	1.0.7
Release:	1
License:	GPL
Group:		Applications/Shells
Source0:	ftp://metalab.unc.edu/pub/Linux/system/shells/%{name}-%{version}.tar.gz
Patch0:		%{name}-config.patch
Patch1:		%{name}-opt.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/
%define	_mandir	/usr/share/man

%description
Rc based shell with additions for file locking, temporary files,
reading standard input, expr and let builtin.

%description -l pl
Prosta pow³oka z blokowaniem plików, plikami tymczasowymi i
wyra¿eniami.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install bin/akanga $RPM_BUILD_ROOT%{_bindir}

install src/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install samples/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc src/{CHANGES,EXAMPLES,FAQ,README*} samples/{fileuser,lp,man2html,man2html.cgi,mancc,netuser,which}
%attr(755,root,root) %{_bindir}/akanga
%attr(644,root,root) %{_mandir}/man1/*
