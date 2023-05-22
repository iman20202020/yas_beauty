

def add_section_request(request, ):
    section = None
    path = request.path
    if path == '/blog/forum/':
        section = 'forum_posts_list'
    elif path == '/blog/blogs':
        section = 'blogs_list'

    return {'section': section}
