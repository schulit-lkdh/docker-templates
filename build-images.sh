#!/bin/bash
cd /root

rm -r docker-telegraf-node-snmp
git clone https://github.com/schulit-lkdh/docker-telegraf-node-snmp.git 
cd docker-telegraf-node-snmp
docker build .
