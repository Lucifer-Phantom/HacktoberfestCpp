""" 

Mexico uses a specific cartographic projection to more accurately map
locations, under "International Terrestrial Reference Frame 2008", called
"Lambert Conformal Conic projection 2SP (epsg:9802)". 

https://en.wikipedia.org/wiki/Lambert_conformal_conic_projection

To interface census or geographic data, this requires transforming 
Longitude and Latitude from the more international frame of reference.

The following code allows for transforming one to the other.

"""

# National Geography institute explanatory PDF
# https://www.inegi.org.mx/contenidos/temas/MapaDigital/Doc/asignar_sistema_coordenadas.pdf

# Pyproj, Lambert projections
# https://proj.org/operations/projections/lcc.html

from pyproj import Proj
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

# Definition of lambert conical projection.
lambert = {'proj': 'lcc', # Lambert Conformal Conic 2SP (epsg:9802)
     'ellps': 'GRS80', #'epsg:7019', #'epsg:9802', # 'epsg:6651',
     'lon_0': -102.00000000,
     'lat_0': 12.00000000, # 12° 00’ 0.0’’ N
     'lat_1': 17.50000000, # 17° 30’ 0.00’’ N
     'lat_2': 29.50000000, # 29° 30’ 0.00’’ N
     'x_0': 2500000,
     'y_0': 0}
#     'k_0': }

prj = Proj(lambert) 

# Coordinates for the city of Monterrey, Nuevo León, México

city = {'c_name': 'Monterrey', 'lon': -100.316116, 'lat': 25.686613}

x, y = prj(city['lon'], city['lat']) 

print('                     X                 Y')
print(city['c_name'], ':  lon:', city['lon'], '      , lat:', city['lat'])
print('Lambert function:', x, ',', y)
print('   Should return: 2668223.843       , 1516271.922') 

# Should return:

"""
                     X                 Y
Monterrey :  lon: -100.316116       , lat: 25.686613
Lambert function: 2668223.842598227 , 1516271.9216458194
   Should return: 2668223.843       , 1516271.922
"""