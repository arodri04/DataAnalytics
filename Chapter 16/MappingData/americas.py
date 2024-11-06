############################################
# Software Req Doc: Mapping Global Data Sets
# Release Date: 11/15/24
# Sam Rodriguez
# Description: File to map the Americas
# 
############################################
from pygal_maps_world.maps import World

wm = World()
wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')