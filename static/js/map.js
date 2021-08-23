mapboxgl.accessToken = 'pk.eyJ1IjoiY2xvbWJhcmRpIiwiYSI6ImNrcnpuM3R1dTA4NmIydm9jdHVhNXFudGIifQ.Wuy9V0zOtcfLgdX7efVAWw';
let map = new mapboxgl.Map({
    center: [-78.9040881, 35.9964035,],
    zoom: 10,
container: 'map',
style: 'mapbox://styles/mapbox/streets-v11',


});

map.addControl(
new MapboxGeocoder({
accessToken: mapboxgl.accessToken,
mapboxgl: mapboxgl
}));

const major_the_bull = new mapboxgl.Marker()
.setLngLat([-78.9014462, 35.9963274])
.addTo(map);

const our_roots = new mapboxgl.Marker()
.setLngLat([-78.903123, 35.9971181])
.addTo(map);

const i_am_my_own_muse = new mapboxgl.Marker()
.setLngLat([-78.902838, 35.997092])
.addTo(map);

const ninth_st = new mapboxgl.Marker()
.setLngLat([-78.9031598, 35.9967071])
.addTo(map);

const wall_of_hope = new mapboxgl.Marker()
.setLngLat([-78.9027649, 35.9963675])
.addTo(map);

const along_the_way = new mapboxgl.Marker()
.setLngLat([-78.9014761, 36.0009749])
.addTo(map);

const here_comes_the_sun = new mapboxgl.Marker()
.setLngLat([-78.899663, 35.994717])
.addTo(map);

const winding_out = new mapboxgl.Marker()
.setLngLat([-78.9002386, 35.9959346])
.addTo(map);

const chalice = new mapboxgl.Marker()
.setLngLat([-78.9020611, 35.9965452])
.addTo(map);

const cecys_gallery = new mapboxgl.Marker()
.setLngLat([-78.9016427, 35.999848])
.addTo(map);

const the_art_of_the_warli = new mapboxgl.Marker()
.setLngLat([-78.901872, 35.9987581])
.addTo(map);

const phat_ryan = new mapboxgl.Marker()
.setLngLat([-78.9009637, 36.0006088])
.addTo(map);

const swarm = new mapboxgl.Marker()
.setLngLat([-78.9063472, 35.9951356])
.addTo(map);

const durham_continuum = new mapboxgl.Marker()
.setLngLat([-78.9035749, 35.9958228])
.addTo(map);

const celebrate = new mapboxgl.Marker()
.setLngLat([-78.9026999, 35.9946107])
.addTo(map);

const charging_durham = new mapboxgl.Marker()
.setLngLat([78.9014468, 35.996085])
.addTo(map);

const grab_life_by_the_horns = new mapboxgl.Marker()
.setLngLat([-78.9028958, 35.9964094])
.addTo(map);

const pursuit_of_happiness = new mapboxgl.Marker()
.setLngLat([-78.9037234, 35.9974708])
.addTo(map);

const time_bridge = new mapboxgl.Marker()
.setLngLat([-78.9032525, 35.9984626])
.addTo(map);

const liberty_warehouse = new mapboxgl.Marker()
.setLngLat([-78.9021754, 36.0019981])
.addTo(map);

const two_way_bridges = new mapboxgl.Marker()
.setLngLat([-78.9104586, 35.9996805])
.addTo(map);

const pepsi_mural = new mapboxgl.Marker()
.setLngLat([-78.8859631, 35.9852023])
.addTo(map);

const ground_plane = new mapboxgl.Marker()
.setLngLat([-78.922138, 36.025353])
.addTo(map);

const penguin = new mapboxgl.Marker()
.setLngLat([-78.889999, 35.90799])
.addTo(map);

