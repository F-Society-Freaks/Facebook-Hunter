import io
import os
import sys
import json
import requests
from clear_screen import clear
from datetime import datetime
from lib.colors import style


#Dump all email addressess
def dump_emails():
    clear()
    date = datetime.now().strftime("%H:%M:%S")
    time = datetime.now().strftime("%d/%m/%Y")
    print("     --- Dump All Friends Emails ---")
    print('         --- Author: @Proxy07 ---\n')
    try:
        with open('lib/cache/facebook_token.txt', 'r') as file:
            token = file.read()
    except:
        print(style.RED('\n[!]') + style.RESET(' You must generate an access token first, exiting...'))
        sys.exit(0)
    try:
        print_emails = str(input(style.GREEN('[+]') + style.RESET(' Do you want to print all emails on screen (y/n): ')))
    except KeyboardInterrupt:
        print(style.RED('\n[!]') + style.RESET(' User exit, exiting...'))
        sys.exit(0)
    try:
        i = 0
        while os.path.exists("Logs/emails - %s.txt" % i):
            i += 1
        req1 = requests.get(f'https://graph.facebook.com/me/friends?access_token={token}')
        data1 = json.loads(req1.text)
        with io.open("Logs/emails - %s.txt" % i, 'w', encoding = 'UTF-8') as f:
            for i in data1['data']:
                req2 = requests.get(f'https://graph.facebook.com/{i["id"]}?access_token={token}')
                data2 = json.loads(req2.text)

                try:
                    f.write(f'{data2["name"]} : {data2["email"]}\n')
                    if print_emails == "y":
                        print(style.YELLOW(' [-]') + style.RESET(f'{data2["name"]} : {data2["email"]}'))
                    else:
                        None
                except KeyError:
                    pass
                except KeyboardInterrupt:
                    print(style.RED('\n[!]') + style.RESET(' User exit, exiting...'))
                    sys.exit(0)
            print(style.GREEN('\n[+]') + style.RESET(f" Saved ID's successfuly in Logs/{'Logs/IDs - %s.txt' % i}"))
            print(style.RED('\n[!]') + style.RESET(' Thank you for using FacebookHunter, exiting...'))
            sys.exit(0)
    except KeyboardInterrupt:
        print(style.RED('\n[!]') + style.RESET(' User exit, exiting...'))
        sys.exit(0)
    except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
        print(style.RED('\n[!]') + style.RESET(' Failed to get emails due to connection error.'))
        sys.exit(0)
