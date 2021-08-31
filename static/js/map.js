import artWorks from "./works.js"

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

let popup = new mapboxgl.Popup({closeButton: false, offset: [0, -15]}) 


function setMarkers(works) {
    for (let work of works){
        let marker = new mapboxgl.Marker()
        .setLngLat([work.longitude, work.latitude])
        .addTo(map);
        let div = marker.getElement()
        div.addEventListener('mouseover', (e) => {
            let coordinates = map.unproject([e.x, e.y]);
            popup.setLngLat(coordinates)
                .setHTML(
                    '<h3>' + `${work.title}` + '</h3>' +
                    `<img src=${work.photo} width="200" height="150"></img>`
                    )
                .addTo(map);                
        });

        div.addEventListener('mouseout', (e) => {
            popup.remove()
        })
        }
}

setMarkers(artWorks)
