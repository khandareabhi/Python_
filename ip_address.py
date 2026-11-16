import socket

website=input("Enter the website: ")

ip=socket.gethostbyname(website)

print("Ip address: ",website ,": ",ip)