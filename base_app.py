import os
import stripe
from flask import Flask, jsonify, request, url_for
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')


chatbot_responses = {
    "hello": "Hi there!",
    "bye": "Goodbye!",
    "how are you?": "I'm a bot, but I'm doing great, thank you!",
}


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').lower()

    response = chatbot_responses.get(user_message, "Sorry, I don't understand that message.")

    return jsonify({'response': response})


@app.route('/pay', methods=['POST'])
def pay():
    try:
        
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Chatbot Service',
                    },
                    'unit_amount': 500,  
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=url_for('payment_success', _external=True),
            cancel_url=url_for('payment_cancel', _external=True),
        )
        
        return jsonify({'checkout_url': checkout_session.url})

    except Exception as e:
        return jsonify(error=str(e)), 400

@app.route('/payment_success')
def payment_success():
    return "Payment successful! Thank you for your purchase."


@app.route('/payment_cancel')
def payment_cancel():
    return "Payment was canceled. Please try again."

if __name__ == '__main__':
    app.run(debug=True)