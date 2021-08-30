
import math, random

from kavenegar import *


# function to generate OTP
def generateOTP():
    digits = "0123456789"
    OTP = ""

    # length of password can be changed
    # by changing value in range
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP
#
# # Driver code
# if __name__ == "__main__":
#     print("OTP of 4 digits:", generateOTP())
def send_otp():
    otp_code = generateOTP()
    # api = KavenegarAPI('4C446667424F455A36304C484E7A4B466633597532372F594D4C514F3356457162524C793056523168626F3D')
    # params = {'sender': '10008663', 'receptor': '09123164819', 'message':  'کد تایید شما:' + otp_code }
    # response = api.sms_send(params)



    try:
        api = KavenegarAPI('4C446667424F455A36304C484E7A4B466633597532372F594D4C514F3356457162524C793056523168626F3D',)
        params = {
            'receptor': '09123164819',
            'template': 'otp1',
            'token': '1234',
            'type': 'sms',#sms vs call
        }
        response = api.verify_lookup(params)
        return response
    except APIException as e:
      return (e)
    except HTTPException as e:
      return (e)