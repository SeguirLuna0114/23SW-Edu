import folium
# Folium 라이브러리를 사용하여 지도를 생성하고 저장하는 작업을 수행(웹 기반 지도를 생성하기 위한 library)
latitude = 37.566345
longitude = 126.977893

#.Map클래스 =>지도 객체를 생성하는 클래스
map_osm = folium.Map(location=[latitude, longitude])
#location 매개변수: 지도의 중심 좌표를 설정(latitude와 longitude 값을 사용하여 서울의 위도와 경도를 지도의 중심으로 설정함)
map_osm.save('./xx_map1.html') #생성한 지도를 HTML 파일로 저장
print(type(map_osm)) #map_osm 객체의 타입을 출력(Map 객체가 생성되었는지 확인하기 위한 용도)
# <class 'folium.folium.Map'>

map_osm = folium.Map(location=[latitude, longitude], zoom_start=16)
#zoom_start: 지도의 초기 확대/축소 레벨을 설정(값이 클수록 더 확대된 상태로 시작)
map_osm.save('./xx_map2.html')
print(type(map_osm)) #map_osm 객체의 타입을 출력(Map 객체가 생성되었는지 확인하기 위한 용도)
# <class 'folium.folium.Map'>

map_osm = folium.Map(location=[latitude, longitude], zoom_start=17, tiles='Stamen Terrain')
#tiles: 지도의 타일 제공자를 설정. 기본값은 'OpenStreetMap'이며, 다른 제공자를 선택할 수 있음
#control_scale: 지도의 축척 컨트롤을 표시할지 여부를 설정
map_osm.save('./xx_map3.html')
print(type(map_osm)) #map_osm 객체의 타입을 출력(Map 객체가 생성되었는지 확인하기 위한 용도)
# <class 'folium.folium.Map'>

map_osm = folium.Map(location=[latitude, longitude])
folium.Marker([latitude, longitude], popup='서울특별시청').add_to(map_osm)
map_osm.save('./xx_map4.html')

map_osm = folium.Map(location=[latitude, longitude], zoom_start=17)
folium.Marker([latitude, longitude], popup='서울특별시청', icon=folium.Icon(color='red', icon='info-sign')).add_to(map_osm)
folium.CircleMarker([37.5658859, 126.9754788], radius='덕수궁').add_to(map_osm)
map_osm.save('./xx_map5.html')
print('file saved...')