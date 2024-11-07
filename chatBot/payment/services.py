from flask import jsonify, url_for
import stripe
from config import Config

def pay_payment_for_chat_subscription(request):
    try:
        stripe.api_key = Config.STRIPE_SECRET_KEY
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
            success_url=url_for('payment.payment_success', _external=True),
            cancel_url=url_for('payment.payment_cancel', _external=True),
        )
        
        return jsonify({'checkout_url': checkout_session.url})

    except Exception as e:
            return jsonify(error=str(e)), 400
