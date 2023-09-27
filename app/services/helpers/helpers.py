import calendar
import datetime

import jwt
from creditcard import CreditCard
from cryptography.fernet import Fernet

# Key for jwt
SECRET_KEY = 'maistodos'

# Create a unique encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Function to encrypt credit card number


def encrypt_credit_card_number(number):
    encrypted_number = cipher_suite.encrypt(number.encode())
    return encrypted_number

# Function to decrypt credit card number


def decrypt_credit_card_number(encrypted_number):
    decrypted_number = cipher_suite.decrypt(encrypted_number).decode()
    return decrypted_number

# function to validate the card expiration date


def validate_exp_date(exp_date):
    try:
        exp_date = datetime.datetime.strptime(exp_date, '%m/%Y')
        return exp_date >= datetime.datetime.now()
    except ValueError:
        return False

# function to validate card holder length


def validate_holder(holder):
    return len(holder) >= 2

# function to validate if credit card number is valid


def validate_credit_card_number(number):
    card = CreditCard(number)
    return card.is_valid()

# Formats the expiration date of a credit card.


def format_exp_date(exp_date):
    date_obj = datetime.datetime.strptime(exp_date, '%m/%Y')
    last_day_of_month = calendar.monthrange(date_obj.year, date_obj.month)[1]
    return f"{date_obj.year}-{date_obj.month:02d}-{last_day_of_month}"

# Retrieves the brand of a credit card based on its number.


def get_card_brand(number):
    card = CreditCard(number)
    return card.get_brand()

# Create Token Function


def create_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expira em 1 hora
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token
