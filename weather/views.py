import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):

    if request.method == 'POST':
        city = request.POST.get('name')
        weather_data = []
        form = CityForm()

        try:
            weather_key = '2140004b122066c33d4c3361cd2ef42b'
            url = 'https://api.openweathermap.org/data/2.5/weather'
            pam = {'appid': weather_key, 'q': city, 'units': 'Metric'}
            response = requests.get(url, params=pam)
            weather = response.json()

            city_weather = {
                'city': weather['name'],
                'temperature': weather['main']['temp'],
                'description': weather['weather'][0]['description'],
            }

            # weather_data.append(city_weather)

            context = {'city_weather': city_weather, 'form': form}
            return render(request, 'weather/weather.html', context)

        except:
            context = {'weather_data': 'Place does not exist', 'form': form}
            return render(request, 'weather/weather.html', context)

    else:
        form = CityForm()
        context = {'form': form}
        return render(request, 'weather/weather.html', context)

