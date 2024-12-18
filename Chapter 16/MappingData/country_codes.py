############################################
# Software Req Doc: Mapping Global Data Sets
# Release Date: 11/15/24
# Sam Rodriguez
# Description: Function to get and return the 
# country codes.
############################################
from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """Return the pygal 2 country code for country"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        #If not found
    return None

print(get_country_code('Andorra'))
print(get_country_code('United Arab Emirates'))
print(get_country_code('Afghanistan'))
