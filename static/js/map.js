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

let artWorks = [{
    "longitude" :  -78.9048045,
    "latitude" : 35.9968398,
    "title" : "Pleiades Gallery",
    "year" : 2019, 
    "creators" : "Kim-n-friends",
    "description" : "This was Kim's gallery.",
    "photo" : "./static/img/pleiades.jpeg",
},
{
    "longitude" : -78.903233 ,
    "latitude" : 35.9971451,
    "title" : "Test Site",
    "year" : 1821, 
    "creators" : "artists",
    "description" : "This is some art.",
    "photo" : "./static/img/logo.jpg",
}]

const marker1 = new mapboxgl.Marker()
.setLngLat([-78.9048045, 35.9968398])
.addTo(map);
console.log(marker1)
marker1._element.addEventListener('click', (e) => {
    console.log(e.point)
        let popup = new mapboxgl.Popup({ offset: [0, -50] })       
        .setLngLat([-78.9048045, 35.9968398])     
        .setHTML(
            '<h3>' + "Pleiades Gallery" + '</h3>' +
            '<img src="./static/img/pleiades.jpg" width="200" height="150"></img>'
            )
        .addTo(map);
})

const marker2 = new mapboxgl.Marker()
.setLngLat([-78.903233, 35.9971451])
.addTo(map);

// function addPopup (workArray) {
//     map.on('click', (e) => {
//         let pinLat = e.lngLat.lat
//         let pinLng = e.lngLat.lng
        // let features = map.queryRenderedFeatures(e.point, {
        // });
        // if (!features.length) {
        //     return;
        // }
        // let feature = features[0];
        // console.log(feature)

//         for (let work of workArray) {
//             console.log (pinLat, pinLng)
//             console.log(work.latitude, work.longitude)
//             }
//         };
//     });
// }
//         addPopup(artWorks)
