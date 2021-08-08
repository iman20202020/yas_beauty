from django.shortcuts import render
from ghasedak import ghasedak


def send_sms(request):
    sms = ghasedak.Ghasedak("YinKFOOXSXkFH/Q7kUrhKKr1Ce4Igqh/8EARgAvebXw")

    sms.send({'message': 'hello, world!', 'receptor': '09123164819', 'linenumber': '11', 'senddate': 'senddate',
              'checkid': 'checkid'})

    # sms.bulk1({'message':'hello, world!', 'receptor' : '09xxxxxxxxx,09xxxxxxxxx,09xxxxxxxxx', 'linenumber': 'xxxx', 'senddate': '', 'checkid': ''})


