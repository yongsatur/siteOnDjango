from django.shortcuts import render
import json
import os


def load_personal():
    if os.path.exists('./data/personal.json'):
        with open('./data/personal.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    return []


def index(request):
    return render(request, 'index.html')


def contacts(request, header):
    return render(request, 'contacts.html', {'header': header})


def location(request, header):
    return render(request, 'location.html', {'header': header})


def price(request, header):
    return render(request, 'price.html', {'header': header})


def team(request, header):
    return render(request, 'team.html',{'header': header, 'personal': load_personal()})