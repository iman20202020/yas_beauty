from kavenegar import *
from time import sleep
from python_acts.teacher_number_list import *

def send_list():

    response_list =[]
    teachers_list = generate_teachers_list()
    for i in range(len(teachers_list)):

        mobile_number = teachers_list[i][1]
        token = teachers_list[i][0]
        # token2 = ''
        # token3 = ''
        # sleep(5)
        define_sms(mobile_number,token)

        response_list.append((mobile_number,token))
    return teachers_list



def define_sms(mobile_number,token):
    try:
        api = KavenegarAPI('4C446667424F455A36304C484E7A4B466633597532372F594D4C514F3356457162524C793056523168626F3D',)
        params = {
            'receptor': mobile_number,
            'template': 'likerequest',
            'token': token,
            # 'token2': '',
            # 'token3': '',
            'type': 'sms',#sms vs call
        }
        response = list(api.verify_lookup(params))

        return response
    except APIException as e:
      return (e)
    except HTTPException as e:
      return (e)