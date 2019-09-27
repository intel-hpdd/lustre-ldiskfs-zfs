%define unit_name iml-zfs-import-none.service
%define lustre_version 2.12
%define zfs_version 0.7.13

Name:      lustre-ldiskfs
Version:   5.0.0
# Release Start
Release:    1%{?dist}
# Release End
Summary:   Package to install a Lustre storage server with just ldiskfs support
License:   MIT
URL:       https://github.com/whamcloud/%{name}
Source0:   %{unit_name}
Source1:   00-zfs-import-none.preset

Requires:  lustre > %{lustre_version}
Requires:  kmod-lustre-osd-ldiskfs > %{lustre_version}

BuildRequires: systemd

%description
This is a package you can install if you want to create a Lustre storage
server capable of creating just ldiskfs targets.


%package zfs
Summary:   Package to install a Lustre storage server with both ldiskfs and ZFS support

Requires:  lustre > %{lustre_version}
Requires:  lustre-zfs-dkms > %{lustre_version}
Requires:  kmod-lustre-osd-ldiskfs > %{lustre_version}
Requires:  zfs >= %{zfs_version}

%{?systemd_requires}

%description zfs
This is a package you can install if you want to create a Lustre storage
server capable of creating both ldiskfs and ZFS targets.

%package -n lustre-zfs
Summary: Package to install zfs and lustre (no ldiskfs)

Requires: lustre-osd-zfs-mount > %{lustre_version}
Requires: lustre > %{lustre_version}
Requires: lustre-zfs-dkms > %{lustre_version}
Requires: zfs >= %{zfs_version}

%{?systemd_requires}

%description -n lustre-zfs
This is a package you can install if you want to create a Lustre storage
server capable of creating just zfs targets.

%package zfs-patchless
Summary:   Package to install a Lustre storage server with both patchless ldiskfs and ZFS support

PreReq:    yum-plugin-versionlock
Requires:  lustre > %{lustre_version}
Requires:  zfs >= %{zfs_version}
Requires:  kmod-lustre-osd-ldiskfs > %{lustre_version}
Requires:  kmod-lustre-osd-zfs > %{lustre_version}

%{?systemd_requires}

%description zfs-patchless
This is a package you can install if you want to create a Lustre storage
server capable of creating both patchless ldiskfs and ZFS targets.
This should use the "patchless" lustre server repository.

%prep

%build

%install
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_presetdir}
cp %{SOURCE0} %{buildroot}%{_unitdir}
cp %{SOURCE1} %{buildroot}%{_presetdir}

%files

%post zfs
systemctl preset zfs-import-scan.service
systemctl stop zfs-import-scan.service
systemctl preset zfs-import-cache.service
systemctl stop zfs-import-cache.service
systemctl preset zfs-mount.service
systemctl stop zfs-mount.service
%systemd_post %{unit_name}
%systemd_post zfs.target
systemctl start zfs.target

%files zfs
%{_unitdir}/%{unit_name}
%{_presetdir}/00-zfs-import-none.preset

%preun zfs
%systemd_preun %{unit_name}
systemctl enable zfs-import-scan.service
systemctl enable zfs-import-cache.service
systemctl enable zfs-mount.service

%pre zfs-patchless
yum versionlock exclude kmod-zfs-0.8* zfs-0.8*

%post zfs-patchless
systemctl preset zfs-import-scan.service
systemctl stop zfs-import-scan.service
systemctl preset zfs-import-cache.service
systemctl stop zfs-import-cache.service
systemctl preset zfs-mount.service
systemctl stop zfs-mount.service
%systemd_post %{unit_name}
%systemd_post zfs.target
systemctl start zfs.target

%files zfs-patchless
%{_unitdir}/%{unit_name}
%{_presetdir}/00-zfs-import-none.preset

%preun zfs-patchless
%systemd_preun %{unit_name}
systemctl enable zfs-import-scan.service
systemctl enable zfs-import-cache.service
systemctl enable zfs-mount.service

%files -n lustre-zfs

%changelog
* Fri Sep 27 2019 Joe Grund <jgrund@whamcloud.com> 5.0.0-1
- Exclude zfs 0.8 from consideration until there is official Lustre support

* Wed Apr 24 2019 Joe Grund <jgrund@whamcloud.com> 4.0.0-1
- Restrict lustre to > 2.12
- Add patchless ldiskfs zfs install

* Thu Jul 5 2018 Joe Grund <jgrund@whamcloud.com> 3-1
- create a lustre-zfs package

* Tue May 8 2018 Brian J. Murrell <brian.murrell@intel.com> 3-1
- produce both a lustre-ldiskfs and lustre-ldiskfs-zfs package

* Fri Mar 2 2018 Joe Grund <joe.grund@intel.com> 2-1
- Add unit to start ZFS services post install.
- Fixup spec to enable / disable correct units.

* Tue Aug 22 2017 Brian J. Murrell <brian.murrell@intel.com> 1-3
- Remove LU-9745 hack now that that is fixed upstream

* Tue Jul 11 2017 Brian J. Murrell <brian.murrell@intel.com> 1-2
- Add post to work around LU-9745 by removing the autoinstalled
  lustre module and re-installing it

* Fri Jul 7 2017 Brian J. Murrell <brian.murrell@intel.com> 1-1
- Initial package
