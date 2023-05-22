from accounts.models import Teacher
import xlsxwriter

def teacher_urls_query():
    teachers = Teacher.objects.all()
    teachers_message_list = []

    for teacher in teachers:
        teacher_phone_number = teacher.user.username
        teacher_url = f"{teacher.slug}/"+ f"https://ostadbaz.com/course/{teacher.id}"
        teacher_last_name = teacher.last_name
        teacher_message1 = f" استادباز سامانه معرفی هنرجو- استاد گرامی {teacher_last_name}- لطفا از طریق لینک https://ostadbaz.com وارد سایت شده از طریق بخش (ثبت نام/ورود)  به صفحه خود رفته تغییرات لازم در مورد قیمت و نمونه کارها و ... را اعمال بفرمایید . در ضمن می توانید از شاگردان خود  بخواهید که نظر خود را در صفحه شما ثبت کنند،چون که در جذب هنرجو بسیار موثر است:"


        teachers_message_list.append([teacher_phone_number, teacher_message1,])
        print(teachers_message_list)
        with xlsxwriter.Workbook('teachers.xlsx') as workbook:
            worksheet = workbook.add_worksheet()

            for row_num, data in enumerate(teachers_message_list):
                worksheet.write_row(row_num, 0, data)
        # break

