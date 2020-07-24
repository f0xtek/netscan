#!/usr/bin/env python3

import argparse
import scapy.all as scapy


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="The target IP/IP range.", required=True)
    arguments = parser.parse_args()
    return arguments


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="FF:FF:FF:FF:FF:FF")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
    return client_list


def print_result(results_list):
    print(f"IP Address\t\tMAC Address")
    for client in results_list:
        print(f"{client['ip']}\t\t{client['mac']}")


args = get_arguments()
scan_result = scan(args.target)
print_result(scan_result)
