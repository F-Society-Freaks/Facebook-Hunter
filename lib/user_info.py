import io
import os
import sys
import json
import requests
from clear_screen import clear
from datetime import datetime
from lib.colors import style


# Dump all available user information from Facebook
def dump_info():
    clear()
    date = datetime.now().strftime("%H:%M:%S")
    time = datetime.now().strftime("%d/%m/%Y")
    print("     --- Dump Friend Information ---")
    print('        --- Author: @Proxy07 ---\n')
    try:
        with open('lib/cache/facebook_token.txt', 'r') as file:
            token = file.read()
    except:
        print(style.RED('\n[!]') + style.RESET(' You must generate an access token first, exiting...'))
        sys.exit(0)
    try:
        print(style.YELLOW('[*]') + style.RESET(' Note: User profile name is case sensetive.'))
        friend_id = str(input(style.GREEN('[+]') + style.RESET(' Enter friend Facebook profile name or ID: ')))
    except KeyboardInterrupt:
        print(style.RED('\n[!]') + style.RESET(' User exit, exiting...'))
        sys.exit(0)
    try:
        i = 0
        while os.path.exists(f"Logs/{friend_id} - %s.txt" % i):
            i += 1
        req1 = requests.get(f'https://graph.facebook.com/me/friends?access_token={token}')
        data1 = json.loads(req1.text)

        with io.open(f"Logs/{friend_id} - %s.txt" % i, 'w', encoding = 'UTF-8') as f:
            for x in data1['data']:
                if friend_id in x['name'] or friend_id in x['id']:
                    req2 = requests.get(f'https://graph.facebook.com/{x["id"]}?access_token={token}')
                    data2 = json.loads(req2.text)

                    print(style.GREEN('\n[+]') + style.RESET(f' Getting Information on {data2["username"]}'))
                    f.write(f'Getting Information on {data2["username"]}\n')
                    try:
                        print(style.YELLOW('    [-]') + style.RESET(f' ID : {x["id"]}'))
                        f.write(f' ID : {x["id"]}\n')
                    except KeyError:
                        pass
                    try:
                        print(style.YELLOW('    [-]') + style.RESET(f' Username : {data2["username"]}'))
                        f.write(f' Username : {data2["username"]}\n')
                    except KeyError:
                        pass
                    try:
                        print(style.YELLOW('    [-]') + style.RESET(f' Email : {data2["email"]}'))
                        f.write(f' Email : {data2["email"]}\n')
                    except KeyError:
                        pass
                    try:
                        print(style.YELLOW('    [-]') + style.RESET(f' Mobile Phone : {data2["mobile_phone"]}'))
                        f.write(f' Mobile Phone : {data2["mobile_phone"]}\n')
                    except KeyError:
                        pass
                    try:
                        print(style.YELLOW('    [-]') + style.RESET(f' Name : {data2["name"]}'))
                        f.write(f' Name : {data2["name"]}\n')
                    except KeyError:
                        pass
                    try:
                        print(style.YELLOW('    [-]') + style.RESET(f' First Name : {data2["first_name"]}'))
                        f.write(f' First Name : {data2["first_name"]}\n')
                    except KeyError:
                        pass
                    try:
                        print(style.YELLOW('    [-]') + style.RESET(f' Middle Name : {data2["middle_name"]}'))
                        f.write(f' Middle Name : {data2["middle_name"]}\n')
                    except KeyError:
                        pass
                    try:
                        print(style.YELLOW('    [-]') + style.RESET(f' Last Name : {data2["last_name"]}'))
                        f.write(f' Last Name : {data2["last_name"]}\n')
                    except KeyError:
                        pass
                    try:
                        print(style.YELLOW('    [-]') + style.RESET(f' Locale : {data2["locale"]}'))
                        f.write(f' Locale : {data2["locale"]}\n')
                    except KeyError:
                        pass
                    try:
                        print(style.YELLOW('    [-]') + style.RESET(f' Location : {data2["location"]["name"]}'))
                        f.write(f' Location : {data2["location"]["name"]}\n')
                    except KeyError:
                        pass
                    try:
                        print(style.YELLOW('    [-]') + style.RESET(f' Hometown : {data2["hometown"]["name"]}'))
                        f.write(f' Hometown : {data2["hometown"]["name"]}')
                    except KeyError:
                        pass
                    try:
                        print(style.YELLOW('    [-]') + style.RESET(f' Gender : {data2["gender"]}'))
                        f.write(f' Gender : {data2["gender"]}')
                    except KeyError:
                        pass
                    try:
                        print(style.YELLOW('    [-]') + style.RESET(f' Religion : {data2["religion"]}'))
                        f.write(f' Religion : {data2["religion"]}\n')
                    except KeyError:
                        pass
                    try:
                        print(style.YELLOW('    [-]') + style.RESET(f' Relationship Status : {data2["relationship_status"]}'))
                        f.write(f' Relationship Status : {data2["relationship_status"]}\n')
                    except KeyError:
                        pass
                    try:
                        print(style.YELLOW('    [-]') + style.RESET(f' Political : {data2["political"]}'))
                        f.write(f' Political : {data2["political"]}\n')
                    except KeyError:
                        pass
                    try:
                        print(style.YELLOW('    [-]') + style.RESET(f' Work :'))
                        f.write(' Work :\n')
                        for w in data2['work']:
                            try:
                                print(style.YELLOW('           [-]') + style.RESET(f' Position : {w["position"]["name"]}'))
                                f.write(f'   Position : {w["position"]["name"]}\n')
                            except KeyError:
                                pass
                            try:
                                print(style.YELLOW('           [-]') + style.RESET(f' Employer : {w["employer"]["name"]}'))
                                f.write(f'   Employer : {w["employer"]["name"]}\n')
                            except KeyError:
                                pass
                            try:
                                if w['start_date'] == "0000-00":
                                    print(style.YELLOW('           [-]') + style.RESET(f' Start work date is not found.'))
                                    f.write(f'   Start work date is not found.\n')
                                else:
                                    print(style.YELLOW('           [-]') + style.RESET(f' Started Working : {w["start_date"]}'))
                                    f.write(f'   Started Working : {w["start_date"]}\n')
                            except KeyError:
                                pass
                            try:
                                if w['end_date'] == "0000-00":
                                    print(style.YELLOW('           [-]') + style.RESET(f' End work date is not found.'))
                                    f.write(f'   End work date is not found.\n')
                                else:
                                    print(style.YELLOW('           [-]') + style.RESET(f' Stopped Working : {w["end_date"]}'))
                                    f.write(f'   Stopped Working : {w["end_date"]}\n')
                            except KeyError:
                                pass
                            try:
                                print(style.YELLOW('           [-]') + style.RESET(f' Work Location : {w["location"]["name"]}'))
                                f.write(f'   Work Location : {w["location"]["name"]}\n')
                            except KeyError:
                                pass
                    except KeyError:
                        pass
                    try:
                        print(style.YELLOW('    [-]') + style.RESET(f' Updated Time : {data2["updated_time"][:10]} {data2["updated_time"][11:19]}'))
                        f.write(f' Updated Time : {data2["updated_time"][:10]} {data2["updated_time"][11:19]}\n')
                    except KeyError:
                        pass
                    try:
                        print(style.YELLOW('    [-]') + style.RESET(f' Languages :'))
                        f.write(f' Languages :')

                        for l in data2['languages']:
                            try:
                                print(style.YELLOW('           [-]') + style.RESET(f' {l["name"]}'))
                                f.write(f'   {l["name"]}\n')
                            except KeyError:
                                pass
                    except KeyError:
                        pass
                    try:
                        print(style.YELLOW('    [-]') + style.RESET(f' Bio : {data2["bio"]}'))
                        f.write(f' Bio : {data2["bio"]}\n')
                    except KeyError:
                        pass

                    try:
                        print(style.YELLOW('    [-]') + style.RESET(f' Quotes : {data2["quotes"]}'))
                        f.write(f' Quotes : {data2["quotes"]}\n')
                    except KeyError:
                        pass

                    try:
                        print(style.YELLOW('    [-]') + style.RESET(f' Birthday : {data2["birthday"]}'))
                        f.write(f' Birthday : {data2["birthday"]}\n')
                    except KeyError:
                        pass
                    try:
                        print(style.YELLOW('    [-]') + style.RESET(f' Link : {data2["link"]}'))
                        f.write(f' Link : {data2["link"]}\n')
                    except KeyError:
                        pass

                    try:
                        print(style.YELLOW('    [-]') + style.RESET(f' Fvourite Teams :'))
                        f.write(' Fvourite Teams: \n')

                        for f in data2['favorite_teams']:
                            try:
                                print(style.YELLOW('           [-]') + style.RESET(f' {data2["name"]}'))
                                f.write(f'   {data2["name"]}\n')
                            except KeyError:
                                pass
                    except KeyError:
                        pass
                    try:
                        print(style.YELLOW('    [-]') + style.RESET(f' Education :'))
                        f.write(f' Education :\n')

                        for e in data2['education']:
                            try:
                                print(style.YELLOW('           [-]') + style.RESET(f' {e["school"]["name"]}'))
                                f.write(f'   {e["school"]["name"]}')
                            except KeyError:
                                pass
                    except KeyError:
                        pass

            print(style.GREEN('\n[+]') + style.RESET(f" Saved ID's successfuly in Logs/{f'Logs/{friend_id} - %s.txt' % i}"))
    except KeyError:
        pass
    except KeyboardInterrupt:
        print(style.RED('\n[!]') + style.RESET(' User exit, exiting...'))
        sys.exit(0)
    except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
        print(style.RED('\n[!]') + style.RESET(" Failed to get user's information due to connection error."))
        sys.exit(0)
