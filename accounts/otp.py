
import math, random
from kavenegar import *


def generateOTP():
    digits = "0123456789"
    otp = ""
    for i in range(4):
        otp += digits[math.floor(random.random() * 10)]

    return otp


def send_otp(mobile_number):
    otp_code = generateOTP()
    try:
        api = KavenegarAPI('4C446667424F455A36304C484E7A4B466633597532372F594D4C514F3356457162524C793056523168626F3D',)
        params = {
            'receptor': mobile_number,
            'template': 'otp1',
            'token': otp_code,
            'type': 'sms',#sms vs call
        }
        response = list(api.verify_lookup(params))
        response_with_otp = response.append(otp_code)
        return response
    except APIException as e:
      return (e)
    except HTTPException as e:
      return (e)

def send_sms_teacher_edit(mobile_number,token,token2,token3):

    try:
        api = KavenegarAPI('4C446667424F455A36304C484E7A4B466633597532372F594D4C514F3356457162524C793056523168626F3D',)
        params = {
            'receptor': mobile_number,
            'template': 'teacheredit',
            'token': token,
            'token2': token2,
            'token3': token3,
            'type': 'sms',#sms vs call
        }
        response = list(api.verify_lookup(params))

        return response
    except APIException as e:
      return (e)
    except HTTPException as e:
      return (e)