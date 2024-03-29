

# Port Scanner


## Table of Contents
- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Notes On Usage](#notes-on-usage)
- [Example Usage](#example-usage)


## Description
This Python script is a  port scanner that allows users to scan for available ports on a specified target IP address. It utilizes the `socket` module to establish connections with ports and determine their availability.

## Features
- Scans for available ports within a specified range (1-65535).
- Displays the target IP address being scanned.
- Shows the timestamp when the scanning process started.
- Prints out available ports.

## Requirements
- Python 3.x

## Usage
1. Clone the repository or download the `main.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `main.py`.
4. Run the script with the following command:
    ```
    python main.py [target_ip_address]
    ```
   Replace `[target_ip_address]` with the IP address you want to scan.

## Notes On Usage
- Adjust the timeout value in the script (`s.settimeout()`) if you experience slow or unreliable network connections.
- This script should only be used for educational or authorized testing purposes. Scanning networks without proper authorization may be illegal or against the terms of service of your network provider. Please ensure you use either your own IP address, or that of someone who has given you explicit permission, for the `[target_ip_address]`.
- This application is intended solely for legitimate purposes. It does not facilitate or condone any illegal activities. Any misuse of this application is strictly prohibited. 
- Examples of legitimate usage for this program include:
  - **Network Troubleshooting**: Identifying network connectivity issues and misconfigured network devices.
  - **Security Auditing**: Assessing the security posture of network infrastructure and identifying vulnerabilities.
  - **Penetration Testing**: Simulating cyber attacks to identify weaknesses in systems and applications.
  - **System Monitoring**: Continuously monitoring the availability and health of network services.
  - **Software Development**: Testing network-enabled applications and services during development.

## Example Usage
**Run the script:**
```
$ python main.py 192.168.0.1
```
**Output:**
```
 ____   ____    _    _   _ _   _ ___ _   _  ____       
/ ___| / ___|  / \  | \ | | \ | |_ _| \ | |/ ___|      
\___ \| |     / _ \ |  \| |  \| || ||  \| | |  _       
 ___) | |___ / ___ \| |\  | |\  || || |\  | |_| |_ _ _
|____/ \____/_/   \_\_| \_|_| \_|___|_| \_|\____(_|_|_)


Welcome to your port scanner!
Scanning for available ports
--------------------------------------------------
Scanning Target: 192.168.0.1
Scanning started at: 2024-03-29 18:47:40.540480
--------------------------------------------------
Port 135 is available
Port 139 is available
Port 445 is available
```
**About the IP Address `192.168.0.1` in the above example:**
- The IP address `192.168.0.1` is commonly used as a default gateway address in many home and small office/home office (SOHO) networks. It's often assigned to routers or other network devices that serve as the gateway for devices on the local network to communicate with devices on other networks, such as the internet.

- In home networks, this IP address is frequently assigned to the router provided by the Internet Service Provider (ISP). The router typically handles tasks such as routing network traffic between the local network and the internet, providing network address translation (NAT) services, and assigning IP addresses to devices on the local network using DHCP (Dynamic Host Configuration Protocol).

- However, it's important to note that the specific usage of the IP address `192.168.0.1` can vary depending on the network configuration. While it's commonly used as a default gateway address, it's not a fixed standard, and other IP addresses within the private IP address range (`192.168.0.0` to `192.168.255.255`) may also be used for similar purposes. Additionally, in some cases, this IP address may be assigned to other network devices or have other functions within the network infrastructure.

- Please bear in mind that testing the port scanning application with the IP address `192.168.0.1` may not yield meaningful results in all cases. The availability of ports on this IP address depends on the specific configuration of the network and the devices connected to it. It's recommended that users replace this generic IP address with the actual target IP address they want to scan.

**Finding Your Own IP Address**

To find your own IP address:
- On Windows:
  - Open the Command Prompt and type `ipconfig`. Look for the IPv4 Address under the network adapter you're connected to.
- On macOS or Linux:
  - Open the Terminal and type `ifconfig` or `ip addr`. Look for the IP address associated with the network interface you're using.
- Alternatively, you can use online services or network configuration tools provided by your operating system or router to find your IP address.

Remember to use either your own IP address or that of someone who has given you explicit permission for the `[target_ip_address]` when running the port scanning application.



---
