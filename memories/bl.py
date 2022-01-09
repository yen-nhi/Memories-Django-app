from geopy.geocoders import Nominatim
from .models import Memory, Profile

#API

def get_avatar(user):
    return Profile.objects.get(user=user).avatar

def create_memory(user, memo_name, comment, lat, long):
    if user.is_authenticated:

        #Use geopy to find the city, country from latitude and longtitude
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.reverse(lat + "," + long, language='en')
        if location is not None:
            place = location.raw['address']
            address = []
            try:
                country = place['country']
                try:
                    state = place['state']
                    address.append(state)
                except KeyError:
                    try:
                        city = place['city']
                        address.append(city)
                    except KeyError:
                        pass
                address.append(country)
            except KeyError:
                address = 'Unknown'

            Memory.objects.create(
                user=user, 
                name=memo_name, 
                comment=comment, 
                location=", ".join(address)
            )
            return True
    return False

def fetch_memories(user):
    if user.is_authenticated:
        memories = Memory.objects.filter(user=user).order_by('-time')
        return memories
    return None