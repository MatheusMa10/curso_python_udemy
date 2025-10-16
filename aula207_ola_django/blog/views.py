from django.http import HttpRequest, Http404
from django.shortcuts import render
from blog.data import posts
from typing import Any
# from django.http import HttpResponse
# Create your views here.
def blog(request):
    print('Blog')

    context = {
        # 'text': 'Estamos no blog',
        'title': 'Esta é uma pagina de blog - ',
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context
    )


def post(request: HttpRequest , post_id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post == None:
        raise Http404('Post não existe')

    context = {
        # 'text': 'Estamos no blog',
        'post': found_post,
        'title': found_post['title'] + '- ',
    }
    return render(
        request,
        'blog/post.html',
        context
    )


def exemplo(request):
    print('Exemplo')

    context = {
        'text': 'Estamos no exemplo',
        'title': 'Esta é uma pagina de exemplo - '
    }
    
    return render(
        request,
        'blog/exemplo.html',
        context
    )
