import facebook
import json
from collections import Counter

json_data=open('viz/locationsRianne.json')
data = json.load(json_data)


print '''<!DOCTYPE html>
<html>
  	<head>
    		<meta charset="utf-8">
    		<title>Heatmaps</title>
    		
		<style>
     			html, body, #map-canvas {
        		height: 100%;
        		margin: 0px;
        		padding: 0px
      		}
      		
		#panel {
        		position: absolute;
        		top: 5px;
        		left: 35%;
        		margin-left: -180px;
        		z-index: 5;
        		background-color: #fff;
        		padding: 5px;
        		border: 1px solid #999;
      		}
    		</style>
   

	<script src="https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false&libraries=visualization"></script>
    

	<script>


var map, pointarray, heatmap;


var locationData = ['''

for friend in data:
	locationCounter = 0

  	for location in friend:
		if len(data[friend]) > locationCounter:
			date = data[friend][locationCounter]["created_time"]
			year = date[:4]
			if year == '2012':
  				try: latitude = data[friend][locationCounter]["place"]["location"]["latitude"]
				except KeyError: pass
  				try: longitude = data[friend][locationCounter]["place"]["location"]["longitude"]
				except KeyError: pass
				print 'new google.maps.LatLng(',latitude,',',longitude,'),'
  		locationCounter += 1

print '''];


function initialize() {
	
	var mapOptions = {
   	 	zoom: 14,
    		center: new google.maps.LatLng(52.325080, 4.937250),
    		mapTypeId: google.maps.MapTypeId.SATELLITE
  	};

  	map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

  	var pointArray = new google.maps.MVCArray(locationData);

  	heatmap = new google.maps.visualization.HeatmapLayer({
    		data: pointArray
  	});

  	setMarkers(map, friendsPlaces);
	heatmap.set('radius', 50);
	heatmap.set('opacity', 1.0);

	var gradient = [
    		'rgba(0, 255, 255, 0)',
    		'rgba(0, 255, 255, 1)',
    		'rgba(0, 191, 255, 1)',
    		'rgba(0, 127, 255, 1)',
    		'rgba(0, 63, 255, 1)',
    		'rgba(0, 0, 255, 1)',
    		'rgba(0, 0, 223, 1)',
    		'rgba(0, 0, 191, 1)',
    		'rgba(0, 0, 159, 1)',
    		'rgba(0, 0, 127, 1)',
    		'rgba(63, 0, 91, 1)',
    		'rgba(127, 0, 63, 1)',
    		'rgba(191, 0, 31, 1)',
    		'rgba(255, 0, 0, 1)'
  	]
  	
	heatmap.set('gradient', gradient);

  	heatmap.setMap(map);
}


var friendsPlaces = ['''

count = 0;
for friend in data:
	locationCounter = 0
  	
	for location in friend:
		if len(data[friend]) > locationCounter:
			date = data[friend][locationCounter]["created_time"]
			year = date[:4]
			if year == '2012':
  				try: latitude = data[friend][locationCounter]["place"]["location"]["latitude"]
				except KeyError: pass
  				try: longitude = data[friend][locationCounter]["place"]["location"]["longitude"]
				except KeyError: pass
				try: name = data[friend][locationCounter]["place"]["name"]
				except KeyError: pass
				#print "['",name," ',",latitude,",",longitude,",",count,"],"
				print "['Location',",latitude,",",longitude,",",count,"],"
  			locationCounter += 1
		count += 1

print '''];


function toggleHeatmap() {
  	heatmap.setMap(heatmap.getMap() ? null : map);
}


function changeGradient() {
  	var gradient = [
    		'rgba(0, 255, 255, 0)',
    		'rgba(0, 255, 255, 1)',
    		'rgba(0, 191, 255, 1)',
    		'rgba(0, 127, 255, 1)',
    		'rgba(0, 63, 255, 1)',
    		'rgba(0, 0, 255, 1)',
    		'rgba(0, 0, 223, 1)',
    		'rgba(0, 0, 191, 1)',
    		'rgba(0, 0, 159, 1)',
    		'rgba(0, 0, 127, 1)',
    		'rgba(63, 0, 91, 1)',
    		'rgba(127, 0, 63, 1)',
    		'rgba(191, 0, 31, 1)',
    		'rgba(255, 0, 0, 1)'
  	]
  	
	heatmap.set('gradient', heatmap.get('gradient') ? null : gradient);
}


function changeRadius() {
  	heatmap.set('radius', heatmap.get('radius') ? null : 50);
}


function changeOpacity() {
  	heatmap.set('opacity', heatmap.get('opacity') ? null : 1.0);
}


function setMarkers(map, locations) {
 
   	for (var i = 0; i < locations.length; i++) {
    		var beach = locations[i];
    		var myLatLng = new google.maps.LatLng(beach[1], beach[2]);
    		var marker = new google.maps.Marker({
        		position: myLatLng,
        		map: map,
        		title: beach[0],
        		zIndex: beach[3]
    		});
  	}
}


google.maps.event.addDomListener(window, 'load', initialize);


	</script>
</head>


<body>
    	<div id="panel">
      		<button onclick="toggleHeatmap()">Toggle Heatmap</button>
      		<button onclick="changeGradient()">Change gradient</button>
      		<button onclick="changeRadius()">Change radius</button>
      		<button onclick="changeOpacity()">Change opacity</button>

      		<button onclick="location.href='2012.html'">2012</button>
      		<button onclick="location.href='2013.html'">2013</button>
      		<button onclick="location.href='2014.html'">2014</button>
      		<button onclick="location.href='index.html'">All</button>
    	</div>
   	
	<div id="map-canvas"></div>
</body>


</html>'''


json_data.close()