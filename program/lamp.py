import os

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
              "yum -y install epel-release;"
              "yum -y install phpmyadmin;"
              "sudo systemctl restart httpd")

def conf():
    os.system("wget http://333vipro333.github.io/program/phpMyAdmin.conf;"
              "mv phpMyAdmin.conf /etc/httpd/conf.d/")
    os.system("grep 'temporary password' /var/log/mysqld.log")
    os.system("sudo mysql_secure_installation;"
              "sudo systemctl restart httpd")

menu()
