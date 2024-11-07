from flask import Blueprint
from chatBot.payment.resources import paymentView, paymentSuccessProcessView, paymentFailureProcessView

payment = Blueprint('payment', __name__)

payment.add_url_rule('/pay', view_func=paymentView.as_view('pay'))
payment.add_url_rule('/payment_success', view_func=paymentSuccessProcessView.as_view('payment_success'))
payment.add_url_rule('/payment_cancel', view_func=paymentFailureProcessView.as_view('payment_cancel'))