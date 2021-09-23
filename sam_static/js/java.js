function createmap(Countries) {
    // Title Layer and background 
  var openstreetmap = L.titleLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  var basemap = {
    "Street map": Streetmap
  };

  var overlay = {
    "Countries": Countries
  }

  var map = L.map("id", {
    center: [37.0902, 95.7129],
    zoom: 12,
    layers: [Streetmap, Countries]
  });

  var countries = [
    {
      name: "USA",
      location: [37.0902, 95.7129],
      points: 210
    },
    {
      name: "England"
      location: [52.355, 1.1743],
      points: 150
    },
    {
      name: "France"
      location: [46.2276, 2.2137],
      points: 89
    }
  ];

  L.control.layers(basemap, overlay, {
    collapsed: false
  }).addTo(map);
}

  for (var i = 0; i < countries.length; i++) {

    // Conditionals for country points
    var color = "";
    if (countries[i].points > 200) {
      color = "yellow";
    }
    else if (countries[i].points > 100) {
      color = "blue";
    }
    else if (countries[i].points > 90) {
      color = "green";
    }
    else {
      color = "red";
    }



