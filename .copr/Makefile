BUILDROOT:=$(shell [ -d "/build" ] && echo "/build" || echo ".")
TMPDIR:=$(shell mktemp -d)

srpm:
	mkdir -p ${TMPDIR}/_topdir/{SOURCES,SPECS}
	rm -rf ${BUILDROOT}/_topdir
	cp -r ./* ${TMPDIR}/_topdir/SOURCES
	cp lustre-ldiskfs-zfs.spec ${TMPDIR}/_topdir/SPECS/
	rpmbuild -bs -D "_topdir ${TMPDIR}/_topdir" ${TMPDIR}/_topdir/SPECS/lustre-ldiskfs-zfs.spec
	cp -rf ${TMPDIR}/_topdir ${BUILDROOT}/
	cp -f _topdir/SRPMS/*.rpm $(outdir)