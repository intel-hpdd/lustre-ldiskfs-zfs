srpm:
	mkdir -p /tmp/_topdir/{SOURCES,SPECS}
	cp -r ./* /tmp/_topdir/SOURCES
	rpmbuild -bs --define "_topdir /tmp/_topdir" lustre-ldiskfs-zfs.spec
	cp -r /tmp/_topdir/SRPMS/* $(outdir)