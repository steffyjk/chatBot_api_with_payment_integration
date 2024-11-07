from flask import Blueprint
from chatBot.chat.resources import chatCommunicationView

chat = Blueprint('chat', __name__)

chat.add_url_rule('/chat', view_func=chatCommunicationView.as_view('chat_view'))