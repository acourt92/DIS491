from scapy.all import *
from scapy.layers.inet import *
import socket
import os
import time

### FINAL FINISHED COPY - DO NOT EDIT ###

"""Combination of Scapy to craft packets and socket programming (raw socket)
to establish connection with server for sending packet. A 3-way handshake
will be completed for each packet since each packet will be
sent from a different client and the socket closes after each
packet is sent."""

# Wi-Fi Network SSID and Passwords
chosen_wifi_network = "WIFIpeople1195"
wifi_network_password = "EastToWest0905"

second_network = "iPhone"
second_network_password = "slno4o0bb4rs6"

# command scan that will display all available Wi-Fi networks
# os.system("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport scan")

# Generate a random source port
port = RandNum(1024, 65535)

# Counter to be used to switch networks on even/odd numbers AND to
# print out when the packet has been sent out over the network
count = 0

try:
    document = open("TestFile.txt", 'r')
    for line in document:
        line = line.strip("\n")

        if count % 2 == 0:
            # switch to first Wi-Fi network
            os.system(f"networksetup -setairportnetwork en0 '{chosen_wifi_network}' '{wifi_network_password}'")
            time.sleep(20)

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("52.21.138.227", 22))
            my_packet = IP(dst="52.21.138.227") / TCP(sport=port, dport=22) / line
            s.send(bytes(my_packet))
            count += 1

        else:
            # switch to second Wi-Fi network
            os.system(f"networksetup -setairportnetwork en0 '{second_network}' '{second_network_password}'")
            # os.system(f"networksetup -setairportnetwork en0 '{second_network}'")
            time.sleep(20)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("52.21.138.227", 22))
            my_packet = IP(dst="52.21.138.227") / TCP(sport=port, dport=22) / line
            s.send(bytes(my_packet))
            count += 1

    document.close()
    print("Task completed.")

except Exception as error:
    raise error
