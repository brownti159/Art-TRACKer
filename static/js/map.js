mapboxgl.accessToken = 'pk.eyJ1IjoiY2xvbWJhcmRpIiwiYSI6ImNrcnpuM3R1dTA4NmIydm9jdHVhNXFudGIifQ.Wuy9V0zOtcfLgdX7efVAWw';
let map = new mapboxgl.Map({
    center: [-78.9040881, 35.9964035,],
    zoom: 15,
container: 'map',
style: 'mapbox://styles/mapbox/streets-v11',

});

map.addControl(
new MapboxGeocoder({
accessToken: mapboxgl.accessToken,
mapboxgl: mapboxgl
}));

let popup = new mapboxgl.Popup({closeButton: false}) 
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

// marker.addEventListener('mousemove', function(e) {
//     var coordinates = map.unproject([e.x, e.y]);
//     popup.setLngLat(coordinates)
//       .setText('Meow')
//       .addTo(map); 
//   });

// For every object in the artWorks, we want 
// 1 - marker on the map
// 2 - add event lister to marker's div for popup

function setMarkers(works) {
    for (let work of works){
        let marker = new mapboxgl.Marker()
        .setLngLat([work.longitude, work.latitude])
        .addTo(map);
        let div = marker.getElement()
        div.addEventListener('mouseover', (e) => {
            let coordinates = map.unproject([e.x, e.y]);
            console.log(coordinates)
            console.log(popup)
            popup.setLngLat(coordinates)
                .setHTML(
                    '<h3>' + `${work.title}` + '</h3>' +
                    `<img src=${work.photo} width="200" height="150"></img>`
                    )
                .addTo(map);
                console.log(popup)
                
        });

        div.addEventListener('mouseout', (e) => {
            popup.remove()
        })
        }
}

setMarkers(artWorks)