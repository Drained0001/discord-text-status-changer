import time
import requests

status = input("Enter your status here. The status will change once you add spaces in between the text. ")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
    'Content-Type': 'application/json',
    'Authorization': None,
}

if headers["Authorization"] is None:
    token = input("Enter your discord token here. ")
    headers["Authorization"] = Token

print("[+] Status Changer Loaded")
print("[+] If the status changer doesnt work, your token is most likely wrong.")
print("[+] Running status changer under token: {}".format(headers["Authorization"]))

request = requests.Session()
while True:
    current = []
    for a in status.split(" "):
        curstatus = None
        if len(current)%2 == 1:
            curstatus = "online"
        else:
            curstatus = "dnd"
        current.append(a)
        setting = {
            'status': curstatus,
            "custom_status": {"text": " ".join(current[-4:])}
        }
        info = request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
        if info.status_code == 401:
            print("[+] Your discord token is wrong. Exiting")
            time.sleep(5)
            exit()
        print("[+] Current discord status: {}".format(" ".join(current)))
        time.sleep(1)
