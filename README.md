# chatBot_api_with_payment_integration

Build a simple Flask-based API that simulates a chatbot interaction and includes a payment flow using Stripe.

# Create the env

### create environment command for window system is as below:

`python -m venv env_name`

### activate the env:

`.\env_name\Scripts\activate`

# Install the requirements

`pip install -r .\requirements.txt`

# SET up the env secrets in .env file as per .env-example file

`STRIPE_SECRET_KEY=your_stripe_secret_key_here

# run python flask app:

`python app.py or python run.py `

# Endpoints:

##### 1. POST /chat: Send a JSON payload with a message for the chatbot.

`Request_body: { "message": "hello" }`

`Expected_response: { "response": "Hi there!" }`



##### 2. POST /chat: Send a JSON payload with a message for the chatbot.

`Request_body: {}`

`Expected_response: { "checkout_url": "checkout_url_from_stripe" }`
