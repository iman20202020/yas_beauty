import os

from django.shortcuts import get_object_or_404


def page_create(blog):
    path = "blog/templates/blog/"
    file_name = f"{blog.title}.html"
    with open(os.path.join(path, file_name), 'w', encoding='utf-8') as fp:
        fp.truncate(0)
        # lines_list = []
        lines = ["{% extends 'forum/base.html' %}",
            "{% block title %}" f"{blog.persian_main_title}","{% endblock %}\n",
            "{% block contents %} \n",
                "<div class='text-right'>\n" 
                "<h1 >""{{blog.persian_main_title}}""</h1>\n",
                "<h2>A <u>CS</u> Portal for Everyone</h2>\n" 
                "<p>{{blog.text1}}</p>"
                "</div>"
            "{% endblock %}\n"]
        fp.writelines(lines)
        fp.close()


    # html_file = open(f"{title}.html", "w")
    #     fp.write("Hello There\n")
