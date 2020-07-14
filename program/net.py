from work_conf_file import *
from os import system
# change("vsftpd", 3, "BOOTPROTO")
ip = input("IP: ")
mask = input("prefix: ")
gateway = input("gateway: ")

mask_p = "PREFIX0=" + mask
ip_a = "IPADDR0=" + ip
gateway_a = "GATEWAY0=" + gateway



# find("trash/vsftpd.conf", 0)
with open("trash/ifcfg-enp0s3", "r") as conf_file:
    file = conf_file.readlines()
    cnt = len(file)

if cnt > 14:
    change("trash/ifcfg-enp0s3", 15, ip_a)
    change("trash/ifcfg-enp0s3", 16, mask_p)
    change("trash/ifcfg-enp0s3", 17, gateway_a)

else:
    system("echo " + ip_a + "  >> trash/ifcfg-enp0s3")
    system("echo " + mask_p + "  >> trash/ifcfg-enp0s3")
    system("echo " + gateway_a + "  >> trash/ifcfg-enp0s3")


