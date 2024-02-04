import socket

def port_scan(target_ip, target_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(0.5)
    try:
        client_socket.connect((target_ip, target_port))
        print(f"Port {target_port} is open")
    except socket.error:
        print(f"Port {target_port} is closed")
    finally:
        client_socket.close()

if __name__ == "__main__":
    target_ip = input("Enter the target IP: ")
    target_port = int(input("Enter the port number"))
    port_scan(target_ip, target_port)
    print("Port scan finish.")