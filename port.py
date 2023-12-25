import socket

Host = input("\n" + "Please Enter Your Target To Scan Open Ports: ")

def Scan(Host, Port):

    Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:

        Sock.settimeout(2)
        Sock.connect((Host, Port))
        print("\n" + "[+] * Port {} is Open".format(Port))

    except:
        pass

for Port in range(1,1001):
    Scan(Host, Port)