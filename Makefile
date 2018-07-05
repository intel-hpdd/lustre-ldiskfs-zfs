NAME            := lustre-ldiskfs-zfs
PACKAGE_VERSION := 3
PACKAGE_RELEASE := 1

ifeq ($(UNPUBLISHED),true)
  SCM_COMMIT_NUMBER	:= $(shell git rev-list HEAD | wc -l)
  PACKAGE_RELEASE := $(SCM_COMMIT_NUMBER).$(PACKAGE_RELEASE)
endif

include ./include/rpm.mk
