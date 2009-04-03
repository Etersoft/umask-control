Name: umask-control
Version: 0.1
Release: alt1

Summary: Facilities control for umask helpers
License: GPL
Group: System/Servers
BuildArch: noarch
Packager: Konstantin Baev <kipruss@altlinux.org>

PreReq: control

Source0: %name-%version.tar

%description
This package contains control rules for umask helpers.

%prep
%setup

%install
install -pD -m755 umask.sh %buildroot%_sysconfdir/profile.d
install -pD -m755 umask.control %buildroot%_controldir/umask

%files
%config %_controldir/umask
%config %_sysconfdir/profile.d/umask.sh

%changelog
* Fri Apr 03 2009 Konstantin Baev <kipruss@altlinux.org> 0.1-alt1
- Initial release.
