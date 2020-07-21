from work_conf_file import *
from os import system

def conf_dhcp():
    system("clear")
    change("/etc/sysconfig/network-scripts/ifcfg-enp0s3", 15, '#')
    change("/etc/sysconfig/network-scripts/ifcfg-enp0s3", 16, '#')
    change("/etc/sysconfig/network-scripts/ifcfg-enp0s3", 17, '#')
    change("/etc/sysconfig/network-scripts/ifcfg-enp0s3", 3, "BOOTPROTO=\"dhcp\"")
    change_static("/etc/sysconfig/network-scripts/ifcfg-enp0s3", "#", "")
    system("systemctl restart network")
    menu()


def conf_static():
    # system("clear")
    # ip = input("IP: ")
    # mask = input("prefix: ")
    # gateway = input("gateway: ")

    # mask_p = "PREFIX0=" + mask
    # ip_a = "IPADDR0=" + ip
    # gateway_a = "GATEWAY0=" + gateway
    change("trash/ifcfg-enp0s3", 3, "BOOTPROTO=\"none\"")
    p = open("trash/ifcfg-enp0s3", "r")
    p.strip()
    line =  p.readlines()
    cnt = len(line)
    p.close()
    print(cnt)
    # if cnt <= 15:
    #     end("trash/ifcfg-enp0s3", ip_a)
    #     end("trash/ifcfg-enp0s3", ip_a)
    #     end("trash/ifcfg-enp0s3", ip_a)

    # end("trash/ifcfg-enp0s3", "#")
    # end("trash/ifcfg-enp0s3", "#")
    # end("trash/ifcfg-enp0s3", "#")
    # change("trash/ifcfg-enp0s3", 15, ip_a)
    # change("trash/ifcfg-enp0s3", 16, mask_p)
    # change("trash/ifcfg-enp0s3", 17, gateway_a)
    # system("systemctl restart network")
    # menu()


def menu():
    system("clear")
    dynamic = find("/etc/sysconfig/network-scripts/ifcfg-enp0s3", 3)
    if dynamic == "BOOTPROTO=\"dhcp\"":
        print("--------DHCP--------")
    else:
        print("--------СТАТИЧНЕ IP--------")

    enter = input("--------MY NETWORK--------\n"
                  "1 - СТАТИЧНЕ IP\n"
                  "2 - ДИНАМІЧНЕ IP\n"
                  "0 - ВИХІД\n"
                  ": ")

    if enter == "1":
        conf_static()
    elif enter == "2":
        conf_dhcp()
    elif enter == "0":
        system("clear")
        exit()
    else:
        print("")

conf_static()

