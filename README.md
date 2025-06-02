### Secure File Transfer Using SSL/TLS
* This project demonstrates a simple file transfer system between a client and a server systems. The server accepts connections over SSL/TLS, receives a file name and content from the client side and writes it to a file. The client securely sends a file (hello.txt) to the server which is then saved as yt.txt on the server's side.
* The SSL certificates used in this project are:
    * server.crt (Server certificate)
    * server.key (Server private key)
    * client.crt (Client certificate used for verification)
    * client.key (Client private key)
* To run code
    * First run server.py in one system -- python server.py
    * Then make a hello.txt file on client system and write the content that needs to be transferred
    * Run the client -- python client.py (multiple clients can run)



