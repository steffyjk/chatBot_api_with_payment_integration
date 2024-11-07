from flask import request
from flask.views import MethodView

from chatBot.chat import services

class chatCommunicationView(MethodView):

    def post(self):
        """Get Chat Response as per Provided request.message
        Returns:
            _type_: Json [ reply of question ]
        """
        return services.get_chat_response(request)
    