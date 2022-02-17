# skyblock-bazaar-info

1) .env:
    API_KEY
2) mysql_db folder


```
1) centos 8 image
2) dnf -y update
3) dnf install 'dnf-command(config-manager)' && dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo
4) dnf install docker-ce --nobest
5) curl -L https://github.com/docker/compose/releases/download/1.25.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
6) chmod +x /usr/local/bin/docker-compose
7) /etc/pve/lxc :
lxc.apparmor.profile: unconfined
lxc.cgroup.devices.allow: a
lxc.cap.drop:
8) dnf install epel-release -y
9) dnf install screen -y
10) /usr/bin/dockerd -H unix://
11) dnf install -y git
12) yum -y install openssh-server && service sshd start
```