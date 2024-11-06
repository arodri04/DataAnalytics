############################################
# Software Req Doc: Mapping Global Data Sets
# Release Date: 11/15/24
# Sam Rodriguez
# Description: Python file to list the 
# country keys from pygal
############################################
from pygal_maps_world.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])