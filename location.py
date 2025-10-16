import phonenumbers 
import opencage
import folium
number = "+916370027529"

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,"en")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode

key = 'e6ae1f5f644e4d54953cc12645c6d493'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)
if results:
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
else:
    print("Location not found")
    exit()

print(lat,lng)

myMap = folium.Map(location=[lat, lng],zoom_start=9)
folium.Marker([lat, lng],popup=location).add_to(myMap)
myMap.save("mylocation.html")
