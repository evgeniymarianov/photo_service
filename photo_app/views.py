from django.shortcuts import render
from photo_app.models import Picture
from django.http import HttpResponseRedirect

def user_page(request):
    if request.method == 'GET':
        pictures = Picture.objects.all()
        return render(request, 'user_page.html', {'pictures': pictures})
    if request.method == 'POST':
        picture = Picture(
            description = request.POST['description'],
            file = request.FILES['picture']
        )
        picture.save()
        return HttpResponseRedirect('/user')