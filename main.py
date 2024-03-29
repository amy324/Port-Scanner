import pyfiglet
import sys
import socket
from datetime import datetime


def scan_ports(target):
    print("-" * 50)
    print("Scanning Target: " + target)
    print("Scan started at: " + str(datetime.now()))
    print("-" * 50)

    try:
        for port in range(1, 65536):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.1)
                result = s.connect_ex((target, port))
                if result == 0:
                    print("Port {} is available".format(port))

    except KeyboardInterrupt:
        print("\n Exiting Program")
        sys.exit()
    except socket.gaierror:
        print("\n Hostname Could Not Be Resolved")
        sys.exit()
    except socket.error:
        print("\n Server Is Not Responding")
        sys.exit()


def main():
    ascii_banner = pyfiglet.figlet_format("SCANNING...")
    print(ascii_banner)
    print("Welcome to your port scanner!\nScanning for available ports")


    if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1])
        scan_ports(target)
    else:
        print("Invalid Argument - please enter the IP address")
        sys.exit()


if __name__ == "__main__":
    main()
