from flask import request
from flask.views import MethodView

from chatBot.payment import services

class paymentView(MethodView):

    def post(self):
        return services.pay_payment_for_chat_subscription(request)
    
class paymentSuccessProcessView(MethodView):

    def get(self):
        return "Payment successful! Thank you for your purchase."
    
class paymentFailureProcessView(MethodView):

    def get(self):
        return "Payment was canceled. Please try again."
    