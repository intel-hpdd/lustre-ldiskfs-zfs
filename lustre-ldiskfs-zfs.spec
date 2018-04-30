%{?systemd_requires}
BuildRequires: systemd

%define unit_name iml-zfs-import-none.service

Name:      lustre-ldiskfs-zfs
Version:   2
Release:   1%{?dist}
Summary:   Package to install a Lustre storage server with both ldiskfs and ZFS support

License:   MIT
URL:       https://github.com/intel-hpdd/%{name}
Source0:   %{name}-%{version}.tgz

Requires:  lustre
Requires:  lustre-dkms
Requires:  kmod-lustre-osd-ldiskfs
Requires:  zfs

%description
This is a package you can install if you want to create a Lustre storage
server capable of creating both ldiskfs and ZFS targets.

%prep
%setup

%build

%install
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_presetdir}
cp %{unit_name} %{buildroot}%{_unitdir}
cp 00-zfs-import-none.preset %{buildroot}%{_presetdir}

%post
systemctl preset zfs-import-scan.service
systemctl stop zfs-import-scan.service
systemctl preset zfs-import-cache.service
systemctl stop zfs-import-cache.service
systemctl preset zfs-mount.service
systemctl stop zfs-mount.service
%systemd_post %{unit_name}
%systemd_post zfs.target
systemctl start zfs.target

%files
%{_unitdir}/%{unit_name}
%{_presetdir}/00-zfs-import-none.preset

%preun
%systemd_preun %{unit_name}
systemctl enable zfs-import-scan.service
systemctl enable zfs-import-cache.service
systemct enable zfs-mount.service

%changelog
* Fri Mar 2 2018 Joe Grund <joe.grund@intel.com> 2-1
- Add unit to start ZFS services post install.
- Fixup spec to enable / disable correct units.

* Tue Aug 22 2017 Brian J. Murrell <brian.murrell@intel.com> 1-3
- Remove LU-9745 hack now that that is fixed upstream

* Tue Jul 11 2017 Brian J. Murrell <brian.murrell@intel.com> 1-2
- Add post to work around LU-9745 by removing the autoinstalled
  lustre module and re-installing it

* Fri Jul  7 2017 Brian J. Murrell <brian.murrell@intel.com> 1-1
- Initial package
