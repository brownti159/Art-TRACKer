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

let artWorks = {
    "longitude" :  -78.9048045,
    "latitude" : 35.9968398,
    "title" : "Pleiades Gallery",
    "year" : "2015", 
    "creators" : "Kim-n-friends",
    "photo" : "./img/bull.jpeg",
    "description" : "This was Kim's gallery."
}

const marker1 = new mapboxgl.Marker()
.setLngLat([-78.9048045, 35.9968398])
.addTo(map);

function addPopup (work) {

    map.on('click', (e) => {
        let features = map.queryRenderedFeatures(e.point, {
        });
        if (!features.length) {
            return;
        }
        let feature = features[0];
        
        let popup1 = new mapboxgl.Popup({ offset: [0, -15] })
        .setLngLat([work.longitude, work.latitude])
        .setHTML(
            '<h3>' + `${work.title}` + '</h3>' +
            // '<img>' + feature.properties.image + '</img>' +
            '<p>' + `${work.description}` + '</p>'
            )
            .addTo(map);
        });
}

addPopup(artWorks)
