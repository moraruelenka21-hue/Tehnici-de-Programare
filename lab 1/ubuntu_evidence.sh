#!/bin/sh
export TERM=linux
clear
set -x
hostname
ip -4 -br addr
ip route
ping -c 4 192.168.50.20
set +x
echo
echo 'Configuratia persistenta Netplan:'
cat /etc/netplan/01-l1.yaml
sleep 600
