FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    bash \
    openssh-server
RUN mkdir /var/run/sshd && echo 'root:rootpassword' | chpasswd
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

