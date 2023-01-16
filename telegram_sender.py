import requests
import json
import time

class Sender:
    token = ""
    chat_ID = ""
    
    def __init__(self , token):
        self.token = token
        self.chat_ID = self.get_chatID()
        
        
    
    def get_chatID(self):
        chat_id = ''
        while chat_id == '':
            try:
                data = requests.get(f"https://api.telegram.org/bot{self.token}/getUpdates").json()
                if len(data["result"]) > 0:
                    chat_id =  str(data["result"][0]["message"]["from"]["id"])
                    return chat_id
                else: 
                    raise Exception
            except:
                print("CHAT_ID cannot be found. Send a message to bot. Check your internet connection.")
                time.sleep(1)
                continue
    
    def send_msg(self,text):
        url_req = ("https://api.telegram.org/bot" + self.token + "/sendMessage" + "?chat_id=" + self.chat_ID + "&text=" + text)
        results = requests.get(url_req)
        is_ok = json.loads(results.text)["ok"]
        if is_ok != True:
            raise Exception