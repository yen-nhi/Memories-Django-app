
console.log('Access new_memory.js');

function initMap() {
    const initialLatLng = { lat: 10.800197, lng: 106.6984883 };
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 5,
      center: initialLatLng,
    });
    
    // Create the initial InfoWindow.
    let infoWindow = new google.maps.InfoWindow({
      content: "Click to choose location!",
      position: initialLatLng,
    });

    infoWindow.open(map);
    // Configure the click listener.
    map.addListener("click", (e) => {

      const latlng = e.latLng.toJSON();
      const lat = latlng.lat;
      const long = latlng.lng;
      document.getElementById('lat').value = lat;
      document.getElementById('long').value = long;

      // Close the current InfoWindow.
      infoWindow.close();
      // Create a new InfoWindow.
      infoWindow = new google.maps.InfoWindow({
        position: e.latLng,
      });
      infoWindow.setContent(
        'You picked this place!'
      );
      infoWindow.open(map);
    });
  }
  