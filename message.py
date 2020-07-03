#!/usr/bin/env python3
import os
import re
import ftplib

def autor():
    #Авторизація користувача та налаштування конфігураційних файлів
    while True:
        user_message = os.popen("cat /etc/message/message.conf | grep 'user_message'").read().rstrip()
        if user_message == "user_message = yes":
            os.system("clear")
        else:
            os.system("adduser message")
            os.system("yum install nano;"
                      "passwd message")
            os.system("mkdir /etc/message;"
                      "echo 'user_message = yes' > /etc/message/message.conf")

        user_name = os.popen("cat /etc/message/message.conf | grep user_name").read().rstrip()
        if user_name == "user_name = yes":
            menu_rh()
        else:
            os.system("clear")
            your_name = input("ВАШЕ ІМ'Я: ")
            os.system("echo " + your_name + " > /etc/message/user.conf")
            os.system("echo 'user_name = yes' >> /etc/message/message.conf")


# def menu_os():
#     # ВИБІР ОС
#     while True:
#         os.system("clear")
#         enter = input("--------ВАША ОПЕРАЦІЙНА СИСТЕМА--------\n"
#                       "1 - \"RED HAT\" ПОДІБНА\n"
#                       # "2 - DEBIAN AND OTHER\n"
#                       "0 - ВИХІД\n"
#                       "ВВЕДІТЬ НОМЕР НОМЕР>> ")
#         if enter == "1":
#             menu_rh()
#         # elif enter == "2":
#         #     menu_deb()
#         elif enter == "0":
#             os.system("clear")
#             print("---------------\n"
#                   "| ДОПОБАЧЕННЯ |\n"
#                   "---------------")
#             exit()
#         else:
#             print("ПОМИЛКОВЕ ВВЕДЕННЯ", '"' + enter + '"')


def menu_rh():

    while True:
        os.system("clear")
        enter = input("--------MESSAGE SERVER--------\n"
                      "1 - ВІДПРАВИТИ ПОВІДОМЛЕННЯ\n"
                      "2 - ПРИЙНЯТИ ПОВІДОМЛЕННЯ\n"
                      "3 - ВХІДНІ ПОВІДОМЛЕННЯ\n"
                      "0 - ВИХІД\n"
                      "ВВЕДІТЬ НОМЕР>> ")
        if enter == "1":
            create_message_rh()
        elif enter == "2":
            take_message_rh()
        elif enter == "3":
            my_message_rh()
        elif enter == "0":
            os.system("clear")
            exit()
        else:
            print("ПОМИЛКОВЕ ВВЕДЕННЯ", '"' + enter + '"')


# def menu_deb():
#     os.system("apt install vsftpd;"
#               "systemctl enable vsftpd;"
#               "systemctl start vsftpd;")
#     data = open('/etc/vsftpd.conf').read()
#     u = open('/etc/vsftpd.conf', 'w')
#     u.write(re.sub('anonymous_enable=YES', 'anonymous_enable=NO', data)) #поміняти на writen
#     u.close()
#     os.system("systemctl restart vsftpd")
#
#     while True:
#         enter = input("--------DEBIAN--------\n"
#                       "1 - CREAT MESSAGE\n"
#                       "2 - MY MESSAGE\n"
#                       "0 - EXIT\n"
#                       "ENTER NUMBER>> ")
#         if enter == "1":
#             create_message_deb()
#         elif enter == "2":
#             my_message_deb()
#         elif enter == "0":
#             menu_os()
#         else:
#             print("WARNING TEXT", '"' + enter + '"')


def create_message_rh():
    while True:
        os.system("clear")
        enter = input("--------ВІДПРАВИТИ ПОВІДОМЛЕННЯ--------\n"
                      "1 - ВІДПРАВИТИ ФАЙЛ\n"
                      "2 - ВІДПРАВИТИ ТЕКСТ\n"
                      "0 - НАЗАД\n"
                      "ВВЕДІТЬ НОМЕР>> ")
        if enter == "1":
            message_file_rh()
        elif enter == "2":
            message_text_rh()
        elif enter == "0":
            menu_rh()
        else:
            print("ПОМИЛКОВЕ ВВЕДЕННЯ", '"' + enter + '"')


def message_file_rh():
    os.system("clear")

    host = input("IP: ")
    password = input("ПАРОЛЬ: ")
    find = input("ПЕРЕГЛЯНУТИ ДИРЕКТОРІЮ З ФАЙЛОМ: ")
    os.system("clear")
    print("--------ФАЙЛИ--------")
    os.system("ls " + find)
    file = input("ФАЙЛ: ")
    try:
        con = ftplib.FTP(host, 'message', password)

        con.storbinary('STOR ' + file, open(file, 'rb'))
    except:
        input("ПОМИЛКОВЕ ВВЕДЕННЯ\n"
                      "НАТИСНІТЬ ENTER: ")


def take_message_rh():
    os.system("clear")
    ftp = os.popen("vsftpd -v").read().rstrip()

    if ftp == "vsftpd: version 3.0.2":
        data = open('/etc/vsftpd/vsftpd.conf').read()
        u = open('/etc/vsftpd/vsftpd.conf', 'w')
        u.write(re.sub('anonymous_enable=YES', 'anonymous_enable=NO', data))
        u.close()
        os.system("systemctl restart vsftpd")
    else:
        os.system("yum install vsftpd;"
              "systemctl enable vsftpd;"
              "systemctl start vsftpd;")
        data = open('/etc/vsftpd/vsftpd.conf').read()
        u = open('/etc/vsftpd/vsftpd.conf', 'w')
        u.write(re.sub('anonymous_enable=YES', 'anonymous_enable=NO', data))
        u.close()
        os.system("systemctl restart vsftpd")



    while True:
        os.system("clear")
        print("--------IP--------")
        os.system("ip a | grep inet")
        enter = input("НАТИСНІТЬ ENTER: ")
        if enter == "":
            menu_rh()
        else:
            print("ПОМИЛКОВЕ ВВЕДЕННЯ", '"' + enter + '"')


def message_text_rh():
    os.system("clear")

    host = input("IP: ")
    password = input("ПАРОЛЬ: ")
    my_name = os.popen("cat /etc/message/user.conf").read().rstrip()
    os.system("echo 'ADRESAT: " + my_name + "' >> message.txt;"
              "nano message.txt")
    os.system("clear")
    file = 'message.txt'
    try:
        con = ftplib.FTP(host, 'message', password)

        con.storbinary('STOR ' + file, open(file, 'rb'))
    except:
        input("ПОМИЛКОВЕ ВВЕДЕННЯ\n"
                      "НАТИСНІТЬ ENTER: ")


def my_message_rh():

    while True:
        os.system("clear")
        enter = input("--------ВХІДНІ ПОВІДОМЛЕННЯ--------\n"
                      "1 - ФАЙЛОВІ ПОВІДОМЛЕННЯ\n"
                      "2 - ТЕКСТОВІ ПОВІДОМЛЕННЯ\n"
                      "0 - НАЗАД\n"
                      "ВВЕДІТЬ НОМЕР>> ")
        if enter == "1":
            my_message_file_rh()
        elif enter == "2":
            my_message_text_rh()
        elif enter == "0":
            create_message_rh()
        else:
            print("ПОМИЛКОВЕ ВВЕДЕННЯ", '"' + enter + '"')


def my_message_file_rh():
    while True:
        os.system("clear")
        print("--------ВХІДНІ ФАЙЛОВІ ПОВІДОМЛЕННЯ--------")
        os.system("ls /home/message")
        enter = input("НАТИСНІТЬ ENTER")
        if enter == "":
            menu_rh()
        else:
            print("ПОМИЛКОВЕ ВВЕДЕННЯ", '"' + enter + '"')


def my_message_text_rh():
    while True:
        os.system("clear")
        print("--------ВХІДНІ ТЕКСТОВІ ПОВІДОМЛЕННЯ--------")
        os.system("cat /home/message/message.txt")
        enter = input("-------------------------------\n"
                      "НАТИСНІТЬ ENTER")
        if enter == "":
            menu_rh()
        else:
            print("ПОМИЛКОВЕ ВВЕДЕННЯ", '"' + enter + '"')


autor()
