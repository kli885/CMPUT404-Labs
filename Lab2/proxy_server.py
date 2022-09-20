#!/usr/bin/env python3
import socket
import time

# define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

# create a tcp socket
def create_tcp_socket():
    print("Creating socket")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except (socket.error, msg):
        print(
            f"Failed to create socket. Error code: {str(msg[0])} , Error message : {msg[1]}"
        )
        sys.exit()
    print("Socket created successfully")
    return s


# get host information
def get_remote_ip(host):
    print(f"Getting IP for {host}")
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
        sys.exit()

    print(f"Ip address of {host} is {remote_ip}")
    return remote_ip


# send data to server
def send_data(serversocket, payload):
    print("Sending payload")
    try:
        serversocket.sendall(payload.encode())
    except socket.error:
        print("Send failed")
        sys.exit()
    print("Payload sent successfully")


def main():
    proxy_host = "www.google.com"
    proxy_port = 80

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        # QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # bind socket to address
        s.bind((HOST, PORT))
        # set to listening mode
        s.listen(2)

        # continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)

            # Create a new socket
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_socket:
                remote_ip = get_remote_ip(proxy_host)

                # Connect to proxy socket
                proxy_socket.connect((remote_ip, proxy_port))

                # Send received data
                full_data = conn.recv(BUFFER_SIZE)
                time.sleep(0.5)
                proxy_socket.sendall(full_data)

                # Shutdown
                proxy_socket.shutdown(socket.SHUT_WR)

                # continue accepting data until no more left
                full_data = b""
                while True:
                    data = proxy_socket.recv(BUFFER_SIZE)
                    if not data:
                        break
                    full_data += data
                print(full_data)
                conn.send(full_data)

            conn.close()


if __name__ == "__main__":
    main()
