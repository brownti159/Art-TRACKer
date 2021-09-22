mapboxgl.accessToken = 'pk.eyJ1IjoiY2xvbWJhcmRpIiwiYSI6ImNrcnpuM3R1dTA4NmIydm9jdHVhNXFudGIifQ.Wuy9V0zOtcfLgdX7efVAWw';
let map = new mapboxgl.Map({
    center: [-78.90282, 35.99860],
    zoom: 15,
container: 'map',
style: 'mapbox://styles/mapbox/streets-v11',

});
        


let artWorks;

fetch("api/places/works", {
    headers:{
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
    },
})
.then(response => {
    return response.json() //Convert response to JSON
})
.then(data => {
artWorks = data
setMarkers(artWorks)
})

let popup = new mapboxgl.Popup({closeButton: true, offset: [0, -15]}) 


function setMarkers(works) {
    for (let work of works){
        let marker = new mapboxgl.Marker()
        .setLngLat([work.longitude, work.latitude])
        .addTo(map);
        let div = marker.getElement()
        div.addEventListener('click', (e) => {
            console.log(e)
            let coordinates = map.unproject([e.x, e.y]);
            popup.setLngLat(coordinates)
                .setHTML(
                    '<h3>' + `${work.title}` + '</h3>' +
                    `<img src=${work.photo} width="200" height="150"></img>` +
                    '<button id="detailButton" class="submit-button border-black border-2 px-2 mt-2 rounded-md hover:bg-gray-300">See Details</button>' +
                    '<button id="directionsButton" class="submit-button border-black border-2 px-2 mt-2 rounded-md hover:bg-gray-300">Get Directions</button>' +
                    `<data-work-id=${work.id}>`
                    )
                .addTo(map);
                e.stopPropagation();              
            document.getElementById("detailButton").onclick = function () {
                location.href = `works/${work.id}`;
            };
            document.getElementById("directionsButton").onclick = function () {
                map.addControl(
                    new MapboxDirections({
                    accessToken: mapboxgl.accessToken
                    }),
                    'top-left'
                    );
                    directions.setOrigin([work.longitude, work.latitude]); // can be address in form setOrigin("12, Elm Street, NY")
            };
        });
        }
}




// map.addControl(
//     directions, 
//     'top-left'
//     );
//     map.on('load',  function() {
//         directions.setOrigin([12, 23]); // can be address in form setOrigin("12, Elm Street, NY")
//         directions.setDestination([11, 22]); // can be address
//     })
// console.log(directions)