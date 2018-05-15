__author__ = 'rafeg'

TOKEN_TELEGRAM = '522486484:AAEjqk7h6EYC2Q7LZPXsJigFIxW2nosomnk'
import requests


def send_text(text, chat_id):
    text = """
    *bold text*
_italic text_
[inline URL](http://www.google.com/)
[inline mention of a user](tg://user?id=159062336)
`inline fixed-width code`
```block_language
pre-formatted fixed-width code block
```
"""

    url = 'https://api.telegram.org/bot{}/sendMessage'.format(TOKEN_TELEGRAM)
    data = {'chat_id': chat_id, 'text': text, 'parse_mode':'markdown'}
    response = requests.post(url, data=data)
    print(response.content)

#https://api.telegram.org/botToken/sendMessage?chat_id=-1&text=Choose&reply_markup={"keyboard":[["Yes"],["No"]]}


def send_button(text, chat_id):
    url = 'https://api.telegram.org/bot{}/sendMessage'.format(TOKEN_TELEGRAM)
    import json

    reply_markup={'keyboard':[['clima em sampa', '/grupo UNO - STUCK ORDER rer rere huyh jujujuuj'],['Time1', 'time2'], ['Time1', 'time2'], ['Time1', 'time2'], ['Time1', 'time2'],
                              ['Time1', 'time2'],['Time1', 'time2'], ['Time1', 'time2'], ['Time1', 'time2'], ['Time1', 'time2'],
                              ['Time1', 'time2'],['Time1', 'time2'], ['Time1', 'time2'], ['Time1', 'time2'], ['Time1', 'time2'],
                              ['Time1', 'time2'],['Time1', 'time2'], ['Time1', 'time2'], ['Time1', 'time2'], ['Time1', 'time2']], 'resize_keyboard':True}

    reply_markup={'keyboard':[[{'text':'troca senha sig', 'callback_data':'aew'}],['/grupo UNO - STUCK ORDER rer rere huyh jujujuuj'],['Time1'], ['Time1'], ['Time1']], 'resize_keyboard':True,
                               'one_time_keyboard':True}

    reply_markup={'inline_keyboard':[[{'text':'troca senha sig','callback_data':'troca senha sig aew'}, {'text':'troca senha erp','callback_data':'troca senha erp aew'}]]}
    #reply_markup = inlineButton


    data = {'chat_id': chat_id, 'text': text, 'reply_markup':reply_markup}
    print(data)
    response = requests.post(url, json=data)
    print(response.content)

def send_button2(text, chat_id):
    url = 'https://api.telegram.org/bot{}/sendMessage'.format(TOKEN_TELEGRAM)
    import json

    reply_markup={'keyboard':[['time1, time2'],['No'],['aew'], ['aew2', 'aew3']]}

    data = {'chat_id': chat_id, 'text': text, 'reply_markup':reply_markup}
    print(data)
    response = requests.post(url, json=data)
    print(response.content)

def edit_message(text, chat_id, message_id):
    url = 'https://api.telegram.org/bot{}/editMessageText'.format(TOKEN_TELEGRAM)
    import json

    #reply_markup={'keyboard':[['time1, time2'],['No'],['aew'], ['aew2', 'aew3']]}

    #data = {'chat_id': chat_id, 'text': text, 'message_id':message_id, 'inline_message_id':inline_message_id}
    data = {'chat_id': chat_id, 'text': text, 'message_id':message_id}
    print(data)
    response = requests.post(url, json=data)
    print(response.content)



if __name__ == '__main__':
    text = 'trocado'
    chat_id = '159062336'
    message_id = '1049'
    inline_message_id = ''
    #edit_message(text, chat_id, message_id)
    #send_button(text, '159062336')
    send_button2(text, chat_id)

