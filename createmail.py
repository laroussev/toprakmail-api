import requests
import json
def generate_mail():
    url="https://toprakmail.com"
    response = requests.get(url, )
    return response.cookies["ci_session"]
def mail_adress(cookie):
    url="https://toprakmail.com/getEmailAddress"
    headers={
        "cookie": "ci_session="+cookie
    }
    response = requests.post(url, headers=headers, data="")
    return json.loads(response.text)

def mail_inbox(cookie):
    url="https://toprakmail.com/getInbox"
    headers={
        "cookie": "ci_session="+cookie
    }
    response = requests.post(url, headers=headers, data="")
    return json.loads(response.text)

cookies=generate_mail()
mail=mail_adress(cookies)["address"]
recover_key=mail_adress(cookies)["recover_key"]
mailinbox=mail_inbox(cookies)
