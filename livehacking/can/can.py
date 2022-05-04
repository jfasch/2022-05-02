import socket
import struct


def create_can_socket(ifacename):
    s = socket.socket(socket.PF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
    s.bind((ifacename,))
    return s

def format_temperature(temp_millicelsius):
    return struct.pack("!i", temp_millicelsius)

def send_frame(s, can_id, payload):
    frame = struct.pack("=IB3x8s", can_id, len(payload), payload)
    s.send(frame)
