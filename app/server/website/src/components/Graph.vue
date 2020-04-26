<template>
  <div class="area">
    <form name="Form">
      <div class="input-field">
        <label for="unit">Unité...</label>
        <div class="formfield-select--container">
          <select id="unit" name="unit" class="unit">
            <option value="unit1">Unité1</option>
            <option value="unit2">Unité2</option>
            <option value="unit3">Unité3</option>
            <option value="unit4">Unité4</option>
          </select>
        </div>
      </div>

      <div class="button-col">
        <div class="row">
          <a class="button-get" @click="getFavoriot()">
            <img src="../assets/cloud-download-outline.svg" alt="cloud-download" />
          </a>
        </div>
      </div>
    </form>
    <line-chart :chart-data="datacollection"></line-chart>
  </div>
</template>

<script>
import LineChart from "./LineChart.js";
import axios from "axios";

export default {
  name: "Graph",
  props: {
    msg: String
  },
  components: {
    LineChart
  },
  data() {
    return {
      datacollection: null,
      loaded: false,
      temperatureCuve: [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1
      ],
      temperatureExterieur: [
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2
      ],
      poidLait: [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
      poidProduitFini: [
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4
      ],
      MesurePH: [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
      MesureK: [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
      NiveauSalmonelle: [
        7,
        7,
        7,
        7,
        7,
        7,
        7,
        7,
        7,
        7,
        7,
        7,
        7,
        7,
        7,
        7,
        7,
        7,
        7,
        7,
        7
      ],
      NiveauEColis: [
        8,
        8,
        8,
        8,
        8,
        8,
        8,
        8,
        8,
        8,
        8,
        8,
        8,
        8,
        8,
        8,
        8,
        8,
        8,
        8,
        8
      ],
      NiveauBactérienListeria: [
        9,
        9,
        9,
        9,
        9,
        9,
        9,
        9,
        9,
        9,
        9,
        9,
        9,
        9,
        9,
        9,
        9,
        9,
        9,
        9,
        9
      ],
      time: [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20
      ]
    };
  },
  mounted() {
    this.fillData();
    this.getFavoriot();
  },
  methods: {
    fillData() {
      this.datacollection = {
        labels: this.time,
        datasets: [
          {
            label: "Température de la cuve (°C)",
            backgroundColor: "rgba(255, 0, 0, 0.2)",
            borderColor: "lightpink",
            pointBackgroundColor: "red",
            borderWidth: 1,
            pointBorderColor: "red",
            data: this.temperatureCuve
          },
          {
            label: "Température extérieur (°C)",
            backgroundColor: "rgba(0, 0, 255, 0.2)",
            borderColor: "lightblue",
            pointBackgroundColor: "blue",
            borderWidth: 1,
            pointBorderColor: "blue",
            data: this.temperatureExterieur
          },
          {
            label: "Poid du lait (Kg)",
            backgroundColor: "rgba(255, 255, 0, 0.2)",
            borderColor: "orange",
            pointBackgroundColor: "orange",
            borderWidth: 1,
            pointBorderColor: "orange",
            data: this.poidLait
          },
          {
            label: "Poid du produit fini (Kg)",
            backgroundColor: "rgb(138, 43, 226, 0.2)",
            borderColor: "BlueViolet",
            pointBackgroundColor: "BlueViolet",
            borderWidth: 1,
            pointBorderColor: "BlueViolet",
            data: this.poidProduitFini
          },
          {
            label: "Mesure du PH",
            backgroundColor: "rgb(0, 255, 255, 0.2)",
            borderColor: "Cyan",
            pointBackgroundColor: "Cyan",
            borderWidth: 1,
            pointBorderColor: "Cyan",
            data: this.MesurePH
          },
          {
            label: "Mesure K+ (mg/L)",
            backgroundColor: "rgb(169,169,169, 0.2)",
            borderColor: "DarkGray",
            pointBackgroundColor: "DarkGray",
            borderWidth: 1,
            pointBorderColor: "DarkGray",
            data: this.MesureK
          },
          {
            label: "Niveau de salmonelle (ppm)",
            backgroundColor: "rgb(255,215,0, 0.2)",
            borderColor: "Gold",
            pointBackgroundColor: "Gold",
            borderWidth: 1,
            pointBorderColor: "Gold",
            data: this.NiveauSalmonelle
          },
          {
            label: "Niveau E-coli (ppm)",
            backgroundColor: "rgb(255,250,205, 0.2)",
            borderColor: "LemonChiffon",
            pointBackgroundColor: "LemonChiffon",
            borderWidth: 1,
            pointBorderColor: "LemonChiffon",
            data: this.NiveauEColis
          },
          {
            label: "Niveau bactérien listeria (ppm)",
            backgroundColor: "rgb(138, 43, 226, 0.2)",
            borderColor: "Purple",
            pointBackgroundColor: "Purple",
            borderWidth: 1,
            pointBorderColor: "Purple",
            data: this.NiveauBactérienListeria
          }
        ]
      };
    },
    // get favoriot
    getFavoriot() {
      var url = "localhost:3000/robot";
      var headers = {
        headers: {
          "Content-Type": "application/json"
        }
      };
      axios
        .get(url, headers)
        .then(x => {
          console.log(x);
          // var results = x.data.results;
          // var temp = [];
          // var hum = [];
          // var pot = [];
          // var time = [];
          // for (var i = 20; i >= 0; i--) {
          //   var t = parseInt(results[i].data.Temperature);
          //   var h = parseInt(results[i].data.Humidity);
          //   var p = parseInt(results[i].data.Potentio);
          //   var ti = results[i].stream_created_at.split("T");

          //   temp.push(t);
          //   hum.push(h);
          //   pot.push(p);
          //   time.push(ti);
          // }
          // console.log(results)
          // console.log(temp)
          // console.log(hum)
          // console.log(pot)
          // this.temperature = temp;
          // this.humidity = hum;
          // this.potentio = pot;
          // this.time = time;
          // this.loaded = true;
          // this.fillData();
        })
        .catch(() => {
          alert("Failed to get the data 😭");
        });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.area {
  width: 600px;
  height: 200px;
  margin: auto;
  margin-top: 2rem;
}
form {
  display: flex;
  justify-content: center;
  margin-bottom: 2rem;
}
.input-field {
  width: 35%;
  margin-right: 2rem;
  position: relative;
}
.formfield-select--container {
  position: relative;

  background-color: #fff;
  border-bottom: 1px #000 solid;

  overflow: hidden;
  /* 
		Le select natif pourra 
		dépasser sans être vu 
	*/
}
.formfield-select--container select {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;

  width: 110%;
  /* 
		On est sûr de ne plus voir
		la flèche native 
	*/

  height: auto;
  border: 0;
  margin: 0;
  padding: 0.75em;
  border-radius: 0;

  overflow: hidden;
  text-overflow: ellipsis;
  /* 
		On empêche le texte d'aller
		jusqu'au bout s'il est trop long
	*/
}
.formfield-select--container::after {
  /* Le pointeur du select */
  content: "";
  position: absolute;
  top: 50%;
  margin-top: -3px;
  right: 0.75em;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-top-color: #444;
  border-width: 6px;
  border-style: solid;
  pointer-events: none;
}
.unit {
  width: 100%;
  height: 2rem;
  border: none;
  cursor: pointer;
  border-bottom: 1px black solid;
  /* -webkit-appearance: none; */
  margin: 0;
  /* -moz-appearance: textfield; */
}
.unit:focus {
  border-bottom: 2px #248b85 solid;
  /* -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none; */
  margin: 0;
}
.button-col {
  width: 10%;
}
.row {
  width: 100%;
  height: 100%;
  display: flex;
}
.button-get {
  display: inline-flex;
  background-color: #4eb4a8;
  width: 100%;
  height: 100%;
  justify-content: center;
  align-items: center;
  border-radius: 5px;
  cursor: pointer;
}
img {
  width: 50%;
  height: 50%;
}
</style>
