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

const marker1 = new mapboxgl.Marker()
.setLngLat([-78.9048045, 35.9968398])
.addTo(map);

// let layers

map.on('click', function(e) {
    let features = map.queryRenderedFeatures(e.point, {
        // layers: ['durham-art']
    });
    if (!features.length) {
        console.log(features)
        return;
    }
    let feature = features[0];

    let popup1 = new mapboxgl.Popup({ offset: [0, -15] })
        .setLngLat([-78.9048045, 35.9968398])
        .setHTML(
            '<h3>' + "Pleiades" + '</h3>' +
            // '<img>' + feature.properties.image + '</img>' +
            '<p>' + feature.properties.description + '</p>'
        )
        .addTo(map);
});