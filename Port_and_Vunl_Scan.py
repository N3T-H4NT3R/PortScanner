import socket
from IPy import IP


class PortScan():
    banner = []
    Open_Ports = []
    def __init__(self, target, Port_Num):
        self.target = target
        self.Port_Num = Port_Num


    def scan(self):
        for port in range(1,1024):
            self.scan_port(port)

    def check_ip(self):
        try:
            IP(self.target)
            return(self.target)
        except ValueError:
            return socket.gethostbyname(self.target)

    def get_banner(self):
        return s.recv(1024)


    def scan_port(self, port):
        try:
            converted_ip = self.check_ip()
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((converted_ip, port))
            self.Open_Ports.append(port)
            try:
                banner = sock.recv(1024).decode().strip("\n").strip("\r")
                self.banner.append(banner)
            except:
                self.banner.append(" ")
                sock.close()
        except:
            pass

if __name__ == "__main__":
    targets = input('[+] Enter Target/s To Scan Port: ')
    Port_Num = input("Enter Number of Ports That You Want To Scan: ")
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(''))
    else:
        scan(targets)