from accounts.models import Teacher, MyUser


def check_using_user(user_id):
    is_teacher = Teacher.objects.filter(user_id=user_id).exists()
    if  is_teacher:
        pass
    else:
        not_used_user = MyUser.objects.get(id=user_id)
        not_used_user.delete()

def delete_not_used():
    all_users = MyUser.objects.all()
    for user in all_users:
        check_using_user(user.id)

