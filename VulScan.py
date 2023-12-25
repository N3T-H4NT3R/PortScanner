import Port_Scanner

Host = input("[+] * Enter Targer To Scan For Vulnerable Open Ports: ")
Port_Number = int(input("[+] * Enter Target To Scan For Vulnerable Open Ports: "))
Vul_file = input("[+] * Enter Path: ")
print("\n")

Port_Scanner.scan(Host)