from accounts.models import MyUser


def get_phone():
    user_phones = []
    all_users = MyUser.objects.all()
    for user in all_users:
        user_phones.append((user.id, user.phone_number))
        return user_phones


