import os

conf = os.popen("cat work_conf_file.py | grep 'import'").read().strip()

if conf == "import re":
    print("")
else:
    os.system("wget http://333vipro333.github.io/program/work_conf_file.py")

from work_conf_file import *

def menu():
    while True:
        os.system("clear")
        enter = input("-------МЕНЮ--------\n"
                      "1 - Встановити LAMP\n"
                      "2 - Налаштування БД\n"
                      "3 - IP\n"
                      "4 - Вимкнути брандмауер\n"
                      "0 - Вийти\n"
                      ": ")
        if enter == "1":
           install()
        elif enter == "2":
            conf()
        elif enter == "3":
            os.system("clear;"
                      "ip a | grep -w 'inet'")
        elif enter == "4":
            os.system("systemctl stop firewalld")
        elif enter == "0":
            exit()
        else:
            print("")

def install():
    os.system("sudo yum install httpd;"
              "sudo systemctl start httpd.service;"
              "sudo systemctl enable httpd.service;"
              "sudo yum install http://dev.mysql.com/get/mysql57-community-release-el7-7.noarch.rpm;"
              "sudo yum install mysql-server;"
              "sudo systemctl start mysqld;"
              "sudo yum install php php-mysql;"
              "yum install epel-release;"
              "yum install phpmyadmin;"
              "sudo systemctl restart httpd")

def conf():
    change("/etc/httpd/conf.d/phpMyAdmin.conf", 17, "Require ip ::1\n       Require all granted")
    os.system("grep 'temporary password' /var/log/mysqld.log")
    os.system("sudo mysql_secure_installation;"
              "sudo systemctl restart httpd")

menu()
