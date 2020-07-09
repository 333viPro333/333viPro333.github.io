from os import system, popen
from work_conf_file import *


def install():
    system("clear")
    if popen("vsftpd -v").read().strip() == "vsftpd: version 3.0.2":
        print("FTP Встановлено")
    else:
        system("yum install vsftpd;"
               "systemctl enable vsftpd;"
               "systemctl restart vsftpd;"
               "systemctl status vsftpd")
        if popen("vsftpd -v").read().strip() == "vsftpd: version 3.0.2":
            print("FTP Встановлено")
        else:
            print("Помилка встановлення")


def conf():
    while True:
        system("clear")
        if popen("vsftpd -v").read().strip() == "vsftpd: version 3.0.2":
            print("--------Налаштування--------\n")
            if find("/etc/vsftpd/vsftpd.conf", 11) == "anonymous_enable=NO":
                print("1 - Підключення: Авторизоване")
            else:
                print("1 - Підключення: Анонімне")

            if find("/etc/vsftpd/vsftpd.conf", 18) == "write_enable=YES":
                print("2 - Записування: Дозволено")
            else:
                print("2 - Записування: Заборонено")

            print("3 - Вимкнути/Увімкнути FTP\n"
                  "0 - Вихід в меню")
            system("systemctl status vsftpd | grep -w Active")

            enter = input(": ")
            if enter == "1":
                en = input("--------Підключення--------\n"
                           "a - Анонімне, u - Авторизоване\n"
                           ": ")
                if en == "u":
                    change("/etc/vsftpd/vsftpd.conf", 11, "anonymous_enable=NO")
                elif en == "a":
                    change("/etc/vsftpd/vsftpd.conf", 11, "anonymous_enable=YES")
                else:
                    print("Не вірне значення")
                system("systemctl restart vsftpd")

            elif enter == "2":
                en = input("--------Підключення--------\n"
                           "y - Дозволено, n - Заборонено\n"
                           ": ")
                if en == "y":
                    change("/etc/vsftpd/vsftpd.conf", 18, "write_enable=YES")
                elif en == "n":
                    change("/etc/vsftpd/vsftpd.conf", 18, "write_enable=NO")
                else:
                    print("Не вірне значення")
                system("systemctl restart vsftpd")

            elif enter == "3":
                en = input("on - Увімкнути, off - Вимкнути\n"
                           ": ")

                if en == "on":
                    system("systemctl start vsftpd")
                elif en == "off":
                    system("systemctl stop vsftpd")

            elif enter == "0":
                menu()

            else:
                print("")

        else:
            install()


def dell():
    system("clear")
    enter = input("--------Ви дійсно хочете видалити FTP?--------\n"
                  "y - ТАК; n - НІ\n"
                  ": ")
    if enter == "y":
        system("yum remove vsftpd;"
               "sudo rm -r /etc/vsftpd")
    elif enter == "n":
        menu()

def menu():
    while True:
        system("clear")
        enter = input("--------MЕНЮ FTP--------\n"
                      "1 - Встановити FTP\n"
                      "2 - Налаштування\n"
                      "3 - Видалити\n"
                      "0 - Вихід\n"
                      "------------------------\n"
                      ": ")

        if enter == "1":
            install()
        elif enter == "2":
            conf()
        elif enter == "3":
            dell()
        elif enter == "0":
            system("clear")
            exit()
        else:
            print("")


menu()


