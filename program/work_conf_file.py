import re

def change(conf_file, index, change):
    with open(conf_file, "r") as ftp:
       position = ftp.readlines()[int(index)].strip()

    data = open(conf_file).read()
    u = open(conf_file, 'w')
    u.write(re.sub(position,change, data))
    u.close()

def find(conf_file, index):
    with open(conf_file, "r") as ftp:
       position = ftp.readlines()[int(index)].strip()
       return position