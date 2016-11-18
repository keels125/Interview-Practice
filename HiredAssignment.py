import geocoder
from math import radians, sin, cos, asin, sqrt

def haversine(lat1, long1, lat2, long2):
		#equation to calculate distance between 2 sets of coordinates

		R = 3959  #earth's radius in miles
		lat1, long1, lat2, long2 = map(radians, [lat1, long1, lat2, long2])
		
		delta1 = lat2 - lat1
		delta2 = long2 - long1
	
		a = sin(delta1/2)**2 + (cos(lat1) * cos(lat2))* sin(delta2/2)**2
		c = 2 * asin(sqrt(a))
		d = R * c
		
		return d

def findTwoClosest(cities):
		two_cities = [cities[0], cities[1]] #keep track of city names with min dist
		coords = []
		
		for city in cities:
				g = geocoder.google(city) #used to convert city names to coordinates
				coords.append(g.latlng) #store the coordinates
		
		min_dist = haversine(coords[0][0], coords[0][1], coords[1][0], coords[1][1])

		for i in range(0, len(coords)): #for each city, compute dist with all others
				for j in range(i+1, len(coords)):
						dist = haversine(coords[i][0], coords[i][1],
										coords[j][0], coords[j][1])
						
						if dist < min_dist: #check if we have a new min dist
								min_dist = dist
								two_cities[0] = cities[i]
								two_cities[1] = cities[j]
		
		print(two_cities)

findTwoClosest(["Los Angeles", "San Francisco", "Boston",
								"New York", "Washington", "Seattle", "Austin",
								"Chicago", "San Diego", "Denver", "London",
								"Toronto", "Sydney", "Melbourne", "Paris", "Singapore"])

