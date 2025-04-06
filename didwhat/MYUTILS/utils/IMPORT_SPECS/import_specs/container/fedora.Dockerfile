FROM mcr.microsoft.com/mirror/docker/library/fedora:37
RUN dnf install -y yum-utils rpm-build cpio
COPY [ "./download_packages.sh", "/"]

ENTRYPOINT [ "/download_packages.sh" ]