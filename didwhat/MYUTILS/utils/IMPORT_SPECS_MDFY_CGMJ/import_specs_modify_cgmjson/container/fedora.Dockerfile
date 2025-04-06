FROM fedora:41
RUN dnf install -y yum-utils rpm-build cpio
COPY [ "./download_packages.sh", "/"]

ENTRYPOINT [ "/download_packages.sh" ]
