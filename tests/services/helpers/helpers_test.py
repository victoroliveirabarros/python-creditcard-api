
from faker import Faker
from app.services.helpers import (encrypt_credit_card_number, decrypt_credit_card_number,
                         validate_exp_date, validate_holder, validate_credit_card_number,
                         format_exp_date, get_card_brand, create_token, validate_date_format)

mock = Faker()

def test_encrypt_decrypt_credit_card_number():
    card_number = mock.credit_card_number(card_type='mastercard')
    encrypted_number = encrypt_credit_card_number(card_number)
    decrypted_number = decrypt_credit_card_number(encrypted_number)
    assert decrypted_number == card_number

def test_validate_exp_date():
    valid_date = mock.future_date(end_date='+10y', tzinfo=None).strftime('%m/%Y')
    assert validate_exp_date(valid_date) == True
    invalid_date = mock.past_date(start_date='-10y', tzinfo=None).strftime('%m/%Y')
    assert validate_exp_date(invalid_date) == False

def test_validate_holder():
    valid_holder = mock.name()
    assert validate_holder(valid_holder) == True
    invalid_holder = ''
    assert validate_holder(invalid_holder) == False

def test_validate_credit_card_number():
    valid_card_number = mock.credit_card_number(card_type='mastercard')
    assert validate_credit_card_number(valid_card_number) == True
    invalid_card_number = '12345'
    assert validate_credit_card_number(invalid_card_number) == False

def test_format_exp_date():
    mock_date = mock.future_date(end_date='+10y', tzinfo=None).strftime('%m/%Y')
    formatted_date = format_exp_date(mock_date)
    print(formatted_date)
    assert validate_date_format(formatted_date) == True

def test_get_card_brand():
    card_number = mock.credit_card_number(card_type='mastercard')
    brand = get_card_brand(card_number)
    assert brand == 'master'

def test_create_token():
    user_id = mock.random_int(min=1, max=1000)
    token = create_token(user_id)
    assert isinstance(token, str)
    