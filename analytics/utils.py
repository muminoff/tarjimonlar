import socket
import struct


def ip2long(ip_addr):
    packed_ip = socket.inet_aton(ip_addr)
    return struct.unpack("!L", packed_ip)[0]

def long2ip(longint):
    return socket.inet_ntoa(struct.pack('!L', longint))
