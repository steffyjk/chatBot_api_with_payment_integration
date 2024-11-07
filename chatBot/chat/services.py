from flask import jsonify
from chatBot.chat.constants import chatbot_responses, error_responses

def get_chat_response(request):
    user_message = request.json.get('message', '').lower()
    response = chatbot_responses.get(user_message, error_responses.get('DID_NOT_UNDERSTAND'))
    return jsonify({'response': response})
