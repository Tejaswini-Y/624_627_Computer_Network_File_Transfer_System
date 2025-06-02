import socket
import ssl

IP = "10.1.20.235"
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
    """ Starting a TCP socket with SSL/TLS support. """
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_cert_chain(certfile="client.crt", keyfile="client.key")  # Client's cert and key
    context.load_verify_locations(cafile="server.crt")  # Used to verify the server's cert

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_client = context.wrap_socket(client, server_hostname=IP)


    """ Connecting to the server using SSL/TLS. """
    ssl_client.connect(ADDR)

    """ Opening and reading the file data. """
    file = open("hello.txt", "r")
    data = file.read()

    """ Sending the filename to the server. """
    ssl_client.send("yt.txt".encode(FORMAT))
    msg = ssl_client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    """ Sending the file data to the server. """
    ssl_client.send(data.encode(FORMAT))
    msg = ssl_client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    """ Closing the file. """
    file.close()

    """ Closing the connection from the server. """
    ssl_client.close()

if __name__ == "__main__":
    main()
