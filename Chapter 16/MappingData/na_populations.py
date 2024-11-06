############################################
# Software Req Doc: Mapping Global Data Sets
# Release Date: 11/15/24
# Sam Rodriguez
# Description: Python file to map populations 
# to each country.
############################################
from pygal_maps_world.maps import World

wm = World()
wm.title = "Populations of Countries in North America"
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('na_populations.svg')
