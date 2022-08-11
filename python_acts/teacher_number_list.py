from accounts.models import Teacher, MyUser


def generate_teachers_list():
    list1 = []
    final_list = []
    teachers = Teacher.objects.filter(is_confirmed=True, )[163:173]
    for teacher in teachers:
        list1.append((teacher.last_name,teacher.user_id),)
    for i in range(len(list1)):
        user_id = list1[i][1]
        teacher_last_name = list1[i][0]
        user = MyUser.objects.get(id=user_id)
        username = user.username
        phone_number = user.phone_number

        final_list.append((teacher_last_name,phone_number,username))
    return final_list

