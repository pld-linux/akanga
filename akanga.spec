Summary:	Akanga shell
Summary(pl):	Akanga shell
Name:		akanga
Version:	1.0.5
Release:	1
Copyright:	GPL
Group:		Shells
Group(pl):	Pow³oki
#site:
#path:
Source:		%name-%version.tar.gz
Patch:		%name-config.patch
Buildroot: /tmp/%{name}-%{version}-root

%define	_prefix	/
%define	_mandir	/usr/share/man

%description
Rc based shell with additions for file locking, temporary files, reading standard input, 
expr and let builtin.

description -l pl
Prosta pow³oka z blokowaniem plików, plikami tymczasowymi i wyra¿eniami.

%prep
%setup -q

%patch -p1

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

bzip2 -9 src/*.1 samples/*.1 src/{CHANGES,EXAMPLES,FAQ,README*}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install -s bin/akanga $RPM_BUILD_ROOT%{_bindir}

install src/*.1.bz2 $RPM_BUILD_ROOT%{_mandir}/man1/

install samples/*.1.bz2 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc src/{CHANGES,EXAMPLES,FAQ,README*}.bz2 samples/{fileuser,lp,man2html,man2html.cgi,mancc,netuser,which}
%attr(755,root,root) %{_bindir}/akanga
%attr(644,root,root) %{_mandir}/man1/*.bz2

%changelog
* Fri Jul 30 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
  [1.0.5-1]
- build rpm.
