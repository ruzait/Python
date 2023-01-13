import phonenumbers

ph = phonenumbers.parse("+94757864885")
print(ph)'''

'''import phonenumbers
from phonenumbers import timezone

ph = phonenumbers.parse("+94757864885")
time = timezone.time_zones_for_number(ph)
print(time)'''

'''import phonenumbers
from phonenumbers import geocoder, carrier

ph = phonenumbers.parse("+94757864885")
carr = carrier.name_for_number(ph, 'en')
reg = geocoder.description_for_number(ph, 'en')
print(carr, reg)'''

'''import phonenumbers
from phonenumbers import geocoder, carrier

ph = phonenumbers.parse("+94757864885")
carr = carrier.name_for_number(ph, 'en')
reg = geocoder.description_for_number(ph, 'en')
print(carr, reg)