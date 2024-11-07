from flask import request
from flask.views import MethodView

from chatBot.chat import services

class chatCommunicationView(MethodView):

    def post(self):
        return services.get_chat_response(request)
    