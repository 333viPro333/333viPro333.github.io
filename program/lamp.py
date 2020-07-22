import os

def menu():
    while True:
        os.system("clear")
        enter = input("-------МЕНЮ--------\n"
                      "1 - Встановити LAMP\n"
                      "2 - Налаштування БД\n"
                      "0 - Вмйти\n"
                      ": ")
        if enter == "1":
           install()
        elif enter == "2":
            conf()
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
              "sudo systemctl restart httpd.service")

def conf():
    os.system("grep 'temporary password' /var/log/mysqld.log")
    os.system("sudo mysql_secure_installation")

menu()
