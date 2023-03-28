from django.shortcuts import render


def blog_view(request, name):
    template_name = f'blog/{name}.html'
    context = {'name': name}
    return render(request, template_name, context)



