Summary:	Akanga shell
Summary(pl.UTF-8):	Powłoka Akanga
Name:		akanga
Version:	1.0.21
Release:	1
License:	GPL
Group:		Applications/Shells
Source0:	http://www.ibiblio.org/pub/linux/system/shells/%{name}-%{version}.tar.gz
# Source0-md5:	2b9d823323921f1a525622c52a3bd7bb
Patch0:		%{name}-config.patch
Patch1:		%{name}-opt.patch
Patch2:		%{name}-va_copy.patch
BuildRequires:	bison
BuildRequires:	ctags
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/bin

%description
Rc based shell with additions for file locking, temporary files,
reading standard input, expr and let builtin.

%description -l pl.UTF-8
Prosta powłoka z dodatkami do blokowania plików, plików tymczasowych,
czytania standardowego wejścia oraz wbudowanymi expr i let.

%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p0
%patch -P2 -p1

%build
%{__make} OPTFLAGS="%{rpmcflags}"

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
%{_mandir}/man1/*
