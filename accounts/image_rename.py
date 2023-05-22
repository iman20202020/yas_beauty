import os.path


def image_rename(teacher):

    image_name = teacher.slug + '-'+ str(teacher.id)+'.jpeg'

    old_path =teacher.image.path
    # extension = teacher.image.split('.', 1)[1].lower()
    # if teacher.image:
    #     old_name = teacher.image.name
        # file_path = 'media/' + old_name
        # if os.path.exists(file_path):
        #     teacher.image.name = f"{image_name}.jpeg"
        #     new_file_path = 'media/images/' + image_name
        #     os.rename(file_path, new_file_path)


    new_path = teacher.image.path
    o = os.path.exists(new_path)
    if o :
        image_name = 'images/' + image_name
    teacher.image.name = image_name
    # os.rename(old_path, new_path)
    # teacher
    # teacher.image.instance=1
    teacher_degree_image_list = [teacher.degree_image, teacher.degree_image2, teacher.degree_image3,
                                 teacher.degree_image4, teacher.degree_image5, teacher.degree_image6, teacher.degree_image7]
    i = 0
    for degree_name in teacher_degree_image_list:
        if degree_name:
            i += 1
            degree_image_name = image_name + '-' + str(i)
            if i == 1:
                teacher.degree_image = degree_image_name
            elif i == 2:
                teacher.degree_image2 = degree_image_name
            elif i == 3:
                teacher.degree_image3 = degree_image_name
            elif i == 4:
                teacher.degree_image4 = degree_image_name
            elif i == 5:
                teacher.degree_image5 = degree_image_name
            elif i == 6:
                teacher.degree_image6 = degree_image_name
            elif i == 7:
                teacher.degree_image7 = degree_image_name

    teacher.is_confirmed = False
    return teacher
