from django.shortcuts import render

posts = [
    {
        'title': 'Post 1',
        'date_posted': '1 diciembre 2019',
        'author': 'Ianr',
        'content': 'Content of the post number 1'
    },
    {
        'title': 'Post 2',
        'date_posted': '2 diciembre 2019',
        'author': 'RIan2',
        'content': 'Content of the post number 2'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
