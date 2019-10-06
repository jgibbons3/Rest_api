from django.shortcuts import render
import requests

#def Github(request):
#    user = {}
#    if 'username' in request.GET:
#        username = request.GET['username']
#        url = 'https://api.github.com/users/%s' % username
#        response = requests.get(url)
#        user = response.json()
#    return render(request, 'Rest_api/github.html', {'user': user})


def Github(request):
    vehicle = {}
    if 'vehicle' in request.GET:
        id = request.GET['vehicle']
        url = 'https://swapi.co/api/vehicles/%s/' % id
        response = requests.get(url)
        vehicle = response.json()
    return render(request, 'Rest_api/github.html', {'vehicle': vehicle})
