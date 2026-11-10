#!/bin/sh
set -eu
backup="/root/l1-network-backup-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$backup/active-yaml"
cp -a /etc/netplan "$backup/netplan"
cp -a /etc/cloud/cloud.cfg.d "$backup/cloud.cfg.d"
mv /etc/netplan/*.yaml "$backup/active-yaml/"
cat > /etc/netplan/01-l1.yaml <<'YAML'
network:
  version: 2
  renderer: networkd
  ethernets:
    eth0:
      dhcp4: false
      addresses:
        - 192.168.50.10/24
YAML
chmod 600 /etc/netplan/01-l1.yaml
printf 'network: {config: disabled}\n' > /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg
netplan generate
netplan apply
printf '\nBackup: %s\n' "$backup"
ip -4 -br addr
networkctl status eth0 --no-pager
