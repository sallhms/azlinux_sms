FROM mcr.microsoft.com/mirror/docker/library/centos:8
RUN dnf --disablerepo '*' --enablerepo=extras swap -y centos-linux-repos centos-stream-repos && dnf distro-sync -y
RUN dnf install -y yum-utils rpm-build cpio
COPY [ "./download_packages.sh", "/"]

ENTRYPOINT [ "/download_packages.sh" ]