Summary:	Display stack trace of a running process
Summary(pl):	Wy¶wietla stos ¶ledzeñ uruchomionego procesu
Name:		pstack
Version:	1.2
Release:	1
License:	GPL
Group:		Development/Debuggers
Source0:	%{name}-%{version}.tar.gz
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pstack dumps a stack trace for a process, given the pid of that
process. If the process named is part of a thread group, then all the
threads in the group are traced.

%description -l pl
pstack wyrzuca stos ¶ledzeñ podanego przez pid procesu. Je¿eli proces
jest czê¶ci± grupy w±tków, wtedy wszystkie w±tki w grupie s± ¶ledzone.

%prep
%setup -q

%build
%{__make} \
	CC=%{__cc} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README VERSION
%attr(755,root,root) %{_bindir}/pstack
%{_mandir}/man1/*
