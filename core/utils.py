__author__ = 'galleani'

from .choices import ACTION_CHOICES
from actions.action import Action


def action(user, output, action_name):
    action = dict(([item for item in ACTION_CHOICES if action_name in item]))
    if action:
        function = action[action_name]
        action_class = Action(user, output)
        func = getattr(action_class, function)
        response = func()
    else:
        response = None
    return response
