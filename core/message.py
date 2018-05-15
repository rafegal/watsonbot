__author__ = 'galleani'

from .constants import USER_NAME_WATSON, PASSWORD_WATSON, VERSION_WATSON, TOKEN_TELEGRAM, WORKSPACE_WATSON
from watson_developer_cloud import ConversationV1
from .models import LastUserContext
from .utils import action
import requests
import ast
import datetime


def process(text, user):
    conversation = ConversationV1(
        username=USER_NAME_WATSON,
        password=PASSWORD_WATSON,
        version=VERSION_WATSON)

    last_user_context = LastUserContext.objects.filter(user=user)
    context = None
    if last_user_context:
        last_user_context = last_user_context.get()
        if not last_user_context.updated < datetime.datetime.now() - datetime.timedelta(minutes=1):
            context = last_user_context.context
            context = ast.literal_eval(context)

    response = conversation.message(workspace_id=WORKSPACE_WATSON, input={'text': text}, context=context)
    output = response.get('output')
    new_context = response.get('context')

    if last_user_context:
        last_user_context.context = new_context
        last_user_context.save()
    else:
        LastUserContext.objects.create(user=user, context=new_context)

    action_name = output.get('action')
    if action_name:
        response_action = action(user, response, action_name)
        if response_action:
            for i in response_action:
                if i['type'] == 'text':
                    send_text(i['text'], user.chat_id)
                elif i['type'] == 'image':
                    send_photo(i['image'], user.chat_id)
        else:
            return output.get('text')[0]
    else:
        send_text(output.get('text')[0], user.chat_id)


def send_text(text, chat_id):
    url = 'https://api.telegram.org/bot{}/sendMessage'.format(TOKEN_TELEGRAM)
    data = {'chat_id': chat_id, 'text': text}
    requests.post(url, data=data)


def send_photo(image, chat_id):
    url = 'https://api.telegram.org/bot{}/sendPhoto'.format(TOKEN_TELEGRAM)
    data = {'chat_id': chat_id}
    files = {'photo': image}
    requests.post(url, files=files, data=data)
