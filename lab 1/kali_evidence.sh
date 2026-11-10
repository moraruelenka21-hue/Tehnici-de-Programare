#!/bin/sh
export TERM=linux PAGER=cat
setfont /usr/share/consolefonts/Lat15-TerminusBold24x12.psf.gz
clear
set -x
hostname
ip -4 -br addr
ip route
ping -c 4 192.168.50.10
nmcli --colors no -f NAME,TYPE,DEVICE connection show --active
set +x
echo
sleep 600
