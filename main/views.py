import urllib.request
import json
from django.shortcuts import render
from datetime import datetime

@csrf_exempt
def index(request):

    if request.method == 'POST':
        
        lat = request.POST.get('latitude')
        lon = request.POST.get('longitude')
        x=round(float(lat), 2)
        y=round(float(lon), 2)
        print(lat,lon)
        fi={}
        try:

            
            al_dat=[]


            dat = urllib.request.urlopen(f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units=imperial&exclude=minutely,hourly,alerts&appid=yourAPIid').read()
            
            all_inf = json.loads(dat)

            data = {
                "Timezone": str(all_inf['timezone']),
                
                'time':str(datetime.utcfromtimestamp(all_inf['current']['dt']).strftime('%Y-%m-%d %H:%M:%S')),

                "temperature": str(all_inf['current']['temp']) + ' °F',
                "pressure": str(all_inf['current']['pressure']),
                "humidity": str(all_inf['current']['humidity']),
                'forecast': str(all_inf['current']['weather'][0]['main']),
                'information': str(all_inf['current']['weather'][0]['description']),
                'icon': all_inf['current']['weather'][0]['icon'],

            }
            if all_inf['current']['weather'][0]['main']== "Smoke":
                data.__setitem__("image","smoke.jpeg")
            elif all_inf['current']['weather'][0]['main']== "Haze":
                data.__setitem__("image","haze.jpeg")
            elif all_inf['current']['weather'][0]['main']== "Rain":
                data.__setitem__("image","rainy.jpeg")
            else:
                data.__setitem__("image","bgimage1.jpeg")
            xx=all_inf['daily'][1:]




            


            
            jump={
                'temp_min':00,
                'temp_max':00,
                'humidity':00,
                'date':"time",
                'pressure':00,
                'description':"some_des",
                'icon':'icon'
                
            }
            final=[]
            final.append(data)
            for i in xx:
                jump['temp_min']=i['temp']['min']
                jump['temp_max']=i['temp']['max']
                jump['humidity']=i['humidity']
                jump['date']=datetime.utcfromtimestamp(i['dt']).strftime('%Y-%m-%d %H:%M:%S')
                jump['pressure']=i['pressure']
                jump['description']=i['weather'][0]['description']
                jump['icon']=i['weather'][0]['icon']
                final.append(jump)
                fi.__setitem__("data",final)
            print(data)
            
        
            return render(request, "main/index.html",fi )
        except Exception as e:
            print(e)

            fi = {"city":"please check the city you typed"}
            return render(request, "main/index.html", fi)
        




        
    else:
        data = {}

    return render(request, "main/index.html", data)
