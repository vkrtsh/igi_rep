import random
import requests
from django.shortcuts import render


def facts_about_cats(request):
    page = random.randint(1, 34)
    response = requests.get(f"https://catfact.ninja/facts?page={page}")
    response_data = response.json()
    data = response_data['data']
    facts = [item['fact'] for item in data]
    return render(request, 'cats_facts.html', {'facts': facts})


def images_dogs(request):
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    response_data = response.json()
    image = response_data['message']
    return render(request, 'dogs_images.html', {'image': image})
