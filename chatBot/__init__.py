from flask import Flask
from config import Config


def create_app(app_name='chatBot_with_paymentIntegration', **kwargs):
    app = Flask(app_name)

    app.config.from_object(Config)

    with app.app_context():
        from chatBot.chat.routes import chat
        from chatBot.payment.routes import payment

        app.register_blueprint(chat)
        app.register_blueprint(payment)

        return app