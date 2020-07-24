# netscan

A simple Python network scanner. Scans an IP or IP range and returns alive hosts and their corresponding MAC address.

`usage: netscan.py [-h] -t TARGET`

Example:

```plain
$ python3 netscan.py -t 192.168.222.0/24
IP Address              MAC Address
192.168.222.2           00:50:56:e5:8f:28
192.168.222.1           00:50:56:c0:00:08
192.168.222.254         00:50:56:eb:f4:b4
```