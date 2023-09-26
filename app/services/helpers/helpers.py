import datetime, calendar
from creditcard import CreditCard
from cryptography.fernet import Fernet

# Crie uma chave de encriptação única
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Função para encriptar o número do cartão de crédito
def encrypt_credit_card_number(number):
    encrypted_number = cipher_suite.encrypt(number.encode())
    return encrypted_number

# Função para desencriptar o número do cartão de crédito
def decrypt_credit_card_number(encrypted_number):
    decrypted_number = cipher_suite.decrypt(encrypted_number).decode()
    return decrypted_number

def validate_exp_date(exp_date):
    try:
        exp_date = datetime.datetime.strptime(exp_date, '%m/%Y')
        return exp_date >= datetime.datetime.now()
    except ValueError:
        return False

def validate_holder(holder):
    return len(holder) >= 2

def validate_credit_card_number(number):
    card = CreditCard(number)
    return card.is_valid()

def format_exp_date(exp_date):
    date_obj = datetime.datetime.strptime(exp_date, '%m/%Y')
    last_day_of_month = calendar.monthrange(date_obj.year, date_obj.month)[1]
    return f"{date_obj.year}-{date_obj.month:02d}-{last_day_of_month}"

def get_card_brand(number):
    card = CreditCard(number)
    return card.get_brand()
