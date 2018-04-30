NAME            := lustre-ldiskfs-zfs
PACKAGE_VERSION := 2
DIST_VERSION    := $(PACKAGE_VERSION)
PACKAGE_RELEASE := 2

include ./include/rpm.mk

$(NAME)-$(PACKAGE_VERSION).tgz: iml-zfs-import-none.service
	mkdir $(NAME)-$(PACKAGE_VERSION)/
	cp $< $(NAME)-$(PACKAGE_VERSION)/
	tar czvf $@ $(NAME)-$(PACKAGE_VERSION)/
	rm -rf $(NAME)-$(PACKAGE_VERSION)/

dist: $(NAME)-$(PACKAGE_VERSION).tgz