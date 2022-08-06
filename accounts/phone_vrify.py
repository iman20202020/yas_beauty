from accounts.otp import send_otp


def code_send(user_mobile_number):
    if len(user_mobile_number) == 10:
        user_mobile_number = '0' + user_mobile_number
    response = send_otp(user_mobile_number)
    if response[0]['status'] == 5:
        # code_sent = True
        otp_code = response[1]
    else:
        otp_code = None

    return otp_code


def code_otp_check(otp_sent, otp_user):
    if otp_sent == otp_user:
        return True
    else:
        return False
