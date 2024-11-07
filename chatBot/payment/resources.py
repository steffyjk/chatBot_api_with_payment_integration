from flask import request
from flask.views import MethodView
from chatBot.payment.constants import success_response, failure_response

from chatBot.payment import services


class paymentView(MethodView):

    def post(self):
        return services.pay_payment_for_chat_subscription(request)


class paymentSuccessProcessView(MethodView):

    def get(self):
        return success_response.get("PAYMENT_SUCCESSFULL")


class paymentFailureProcessView(MethodView):

    def get(self):
        return failure_response.get("PAYMENT_CANCEL")
