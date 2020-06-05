import requests

def get_text():
    url = 'https://api.telegram.org/bot749321154:AAEPuNa5kYoXMwJyfvC3Y6hzHHChuOzvD0k/getUpdates'
    text = requests.get(url).json()['result'][-1]['message']['text']
    return text

def get_name():
	url = 'https://api.telegram.org/bot749321154:AAEPuNa5kYoXMwJyfvC3Y6hzHHChuOzvD0k/getUpdates'
	name = requests.get(url).json()['result'][-1]['message']['from']['first_name']
	return name

def get_id():
	url = 'https://api.telegram.org/bot749321154:AAEPuNa5kYoXMwJyfvC3Y6hzHHChuOzvD0k/getUpdates'
	chat_id = requests.get(url).json()['result'][-1]['message']['from']['id']
	return chat_id

def get_date():
    url = 'https://api.telegram.org/bot749321154:AAEPuNa5kYoXMwJyfvC3Y6hzHHChuOzvD0k/getUpdates'
    date = requests.get(url).json()['result'][-1]['message']['date']
    return date

def send_text(chat_id, text):
    url = 'https://api.telegram.org/bot749321154:AAEPuNa5kYoXMwJyfvC3Y6hzHHChuOzvD0k/sendMessage?chat_id={}&text={}'.format(chat_id, text)
    requests.post(url)

date = get_date()

print("Hi! now launching!")

while True:

    if ((('Hello' or 'hi' or 'Hi' or 'hello') == get_text()) and (get_date() > date)):
        print("{} said Hi !".format(get_name()))
        date = get_date()
        send_text(get_id(), "Hello there {}".format(get_name()))
        
    else:
        print("New response from {} . ".format(get_name()), "But Not the message we wanted!")
        pass
