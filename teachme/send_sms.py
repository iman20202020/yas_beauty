
import math, random
from kavenegar import *




def send_sms_stu(mobile_number,token):

    try:
        api = KavenegarAPI('4C446667424F455A36304C484E7A4B466633597532372F594D4C514F3356457162524C793056523168626F3D',)
        params = {
            'receptor': mobile_number,
            'template': 'student',
            'token': token,

            'type': 'sms',#sms vs call
        }
        response = list(api.verify_lookup(params))

        return response
    except APIException as e:
      return (e)
    except HTTPException as e:
      return (e)