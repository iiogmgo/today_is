from django.shortcuts import render


def index(request):
    days = ['어제', '오늘', '내일']
    return render(request, 'weather/index.html', {'days': days})
