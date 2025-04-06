# DisableDockerDetector "Internal tooling, not used in pipelines, no MCR option for openSUSE."
FROM opensuse/tumbleweed
RUN zypper install -y yum-utils rpm-build cpio
RUN mkdir -p /etc/yum && cp -r /etc/zypp/repos.d /etc/yum/repos.d
RUN dnf config-manager --set-enabled repo-source
COPY [ "./download_packages.sh", "/"]

ENTRYPOINT [ "/download_packages.sh" ]