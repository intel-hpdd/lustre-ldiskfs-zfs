%{?systemd_requires}
BuildRequires: systemd

Name:	lustre-ldiskfs-zfs
Version:	1
Release:	4%{?dist}
Summary:	Package to install a Lustre storage server with both ldiskfs and ZFS support

License:	MIT
URL:	https://github.com/intel-hpdd/%{name}
Source0:	%{name}-%{version}.tgz

Requires:	lustre
Requires:	lustre-dkms
Requires:	kmod-lustre-osd-ldiskfs
Requires:	zfs

%description
This is a package you can install if you want to create a Lustre storage
server capable of creating both ldiskfs and ZFS targets.

%prep

%build

%install

%post
%systemd_post zfs-import-none.service

%files
%{_unitdir}/zfs-import-none.service

%changelog
* Fri Mar 2 2018 Joe Grund <joe.grund@intel.com> 1-4
- Add unit to start ZFS services post install.

* Tue Aug 22 2017 Brian J. Murrell <brian.murrell@intel.com> 1-3
- Remove LU-9745 hack now that that is fixed upstream

* Tue Jul 11 2017 Brian J. Murrell <brian.murrell@intel.com> 1-2
- Add %post to work around LU-9745 by removing the autoinstalled
  lustre module and re-installing it

* Fri Jul  7 2017 Brian J. Murrell <brian.murrell@intel.com> 1-1
- Initial package
