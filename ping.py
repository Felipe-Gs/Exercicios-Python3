import os #importa o modo ou biblioteca OS (integra os programas e recursosdo sistema operacional)
import time
'''ip_ou_host = input('digite o ip ou hopst a ser verificado: ')

os.system('ping -n 6 {}'.format(ip_ou_host))'''


#Pings multiplos
with open('hosts.txt') as file:
    dump = file.read()#le o arquivo e joga na variavel
    dump = dump.splitlines()

    for ip in dump:
        print('verificando o ip: ', ip)
        print('-' * 60)
        os.system('ping -n 2 {}'.format(ip))
        print('-' * 60)
        time.sleep(3)
