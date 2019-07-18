
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="maripy")
location = geolocator.geocode("175 5th Avenue NYC")
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="specify_your_app_name_here",
format_string="%s, Cleveland OH")
address, (latitude, longitude) = geolocator.geocode("11111 Euclid Ave")
print(address, latitude, longitude)


from geopy.distance import geodesic
newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)
print(geodesic(newport_ri, cleveland_oh).miles)


