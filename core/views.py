__author__ = 'galleani'


from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import message
from .models import UserTelegram, Message
import json
import logging

logger = logging.getLogger(__name__)


@csrf_exempt
def event(requests):
    try:
        json_request = json.loads(requests.body)
        chat_id = json_request['message']['chat']['id']
        message_id = json_request['message']['message_id']
        text = json_request['message']['text']
        user = UserTelegram.objects.filter(chat_id=chat_id)
        if user:
            user = user.get()
        else:
            first_name = json_request['message']['chat']['first_name']
            last_name = json_request['message']['chat']['last_name']
            user = UserTelegram.objects.create(chat_id=chat_id, first_name=first_name, last_name=last_name)
        Message.objects.create(id=message_id, user=user, text=text)
        if user.active:
            message.process(text, user)
    except Exception as ex:
        logger.error(ex)
    return HttpResponse()
