<template>
  <div id="pdf" class="area">
    <form name="Form">
      <div class="input-field">
        <h1 for="unit">Tous les Robots</h1>
      </div>

      <div class="button-col">
        <div class="row">
          <a class="button-get" @click="getData()">
            <img
              class="cloud-download"
              src="../assets/cloud-download-outline.svg"
              alt="cloud-download"
            />
          </a>
        </div>
      </div>
    </form>
    <line-chart
      :chart-data="datacollection"
      :styles="styles"
      :height="null"
      :width="null"
    ></line-chart>
    <div class="row-button">
      <a class="exportButton" @click="exportButton()">
        <img
          class="download-upload"
          src="../assets/download-outline.svg"
          alt="download-upload"
        />
      </a>
    </div>
  </div>
</template>

<script>
import LineChart from "./LineChart.js";
import axios from "axios";
import html2pdf from "html2pdf.js";

export default {
  name: "RobotsId",
  props: {
    msg: String,
  },
  components: {
    LineChart,
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
        1,
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
        2,
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
        4,
      ],
      MesurePH: [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
      MesureK: [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
      ConcentrationNaCi: [
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
      ],
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
        7,
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
        8,
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
        9,
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
        20,
      ],
    };
  },
  mounted() {
    this.fillData();
    this.getData();
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
            data: this.temperatureCuve,
          },
          {
            label: "Température extérieur (°C)",
            backgroundColor: "rgba(0, 0, 255, 0.2)",
            borderColor: "lightblue",
            pointBackgroundColor: "blue",
            borderWidth: 1,
            pointBorderColor: "blue",
            data: this.temperatureExterieur,
          },
          // {
          //   label: "Poid du lait (Kg)",
          //   backgroundColor: "rgba(255, 255, 0, 0.2)",
          //   borderColor: "orange",
          //   pointBackgroundColor: "orange",
          //   borderWidth: 1,
          //   pointBorderColor: "orange",
          //   data: this.poidLait,
          // },
          // {
          //   label: "Poid du produit fini (Kg)",
          //   backgroundColor: "rgb(138, 43, 226, 0.2)",
          //   borderColor: "BlueViolet",
          //   pointBackgroundColor: "BlueViolet",
          //   borderWidth: 1,
          //   pointBorderColor: "BlueViolet",
          //   data: this.poidProduitFini,
          // },
          {
            label: "Mesure du PH",
            backgroundColor: "rgb(0, 255, 255, 0.2)",
            borderColor: "Cyan",
            pointBackgroundColor: "Cyan",
            borderWidth: 1,
            pointBorderColor: "Cyan",
            data: this.MesurePH,
          },
          {
            label: "Mesure K+ (mg/L)",
            backgroundColor: "rgb(169,169,169, 0.2)",
            borderColor: "DarkGray",
            pointBackgroundColor: "DarkGray",
            borderWidth: 1,
            pointBorderColor: "DarkGray",
            data: this.MesureK,
          },
          {
            label: "Concentration NaCi",
            backgroundColor: "rgb(165, 42, 42, 0.2)",
            borderColor: "Brown",
            pointBackgroundColor: "Brown",
            borderWidth: 1,
            pointBorderColor: "Brown",
            data: this.ConcentrationNaCi,
          },
          {
            label: "Niveau de salmonelle (ppm)",
            backgroundColor: "rgb(255,215,0, 0.2)",
            borderColor: "Gold",
            pointBackgroundColor: "Gold",
            borderWidth: 1,
            pointBorderColor: "Gold",
            data: this.NiveauSalmonelle,
          },
          {
            label: "Niveau E-coli (ppm)",
            backgroundColor: "rgb(95, 95, 95, 0.2)",
            borderColor: " #5f5f5f",
            pointBackgroundColor: " #5f5f5f",
            borderWidth: 1,
            pointBorderColor: " #5f5f5f",
            data: this.NiveauEColis,
          },
          {
            label: "Niveau bactérien listeria (ppm)",
            backgroundColor: "rgb(138, 43, 226, 0.2)",
            borderColor: "Purple",
            pointBackgroundColor: "Purple",
            borderWidth: 1,
            pointBorderColor: "Purple",
            data: this.NiveauBactérienListeria,
          },
        ],
      };
    },
    // get
    getData() {
      var url = `http://localhost:3000/robot`;
      var headers = {
        headers: {
          "Content-Type": "application/json",
        },
      };
      axios
        .get(url, headers)
        .then((x) => {
          var results = x.data;

          var temperatureCuve = [];
          var temperatureExterieur = [];
          var poidLait = [];
          var poidProduitFini = [];
          var MesurePH = [];
          var MesureK = [];
          var ConcentrationNaCi = [];
          var NiveauSalmonelle = [];
          var NiveauEColis = [];
          var NiveauBactérienListeria = [];
          var time = [];
          for (var i = 20; i >= 0; i--) {
            var tc = parseInt(results[i].tank_temperature);
            var te = parseInt(results[i].external_temperature);
            var pl = parseInt(results[i].weight_of_milk_in_tank);
            var pdf = parseInt(results[i].weight_of_milk_difference);
            var mp = parseInt(results[i].ph_measure);
            var mk = parseInt(results[i].k_measure);
            var cn = parseInt(results[i].nacl_concentration);
            var ns = parseInt(results[i].salmonella_bacterium_level);
            var nec = parseInt(results[i].e_coli_bacterium_level);
            var nbl = parseInt(results[i].listeria_bacterium_level);

            var ti = results[i].creation_time.split("T");
            temperatureCuve.push(tc);
            temperatureExterieur.push(te);
            poidLait.push(pl);
            poidProduitFini.push(pdf);
            MesurePH.push(mp);
            MesureK.push(mk);
            ConcentrationNaCi.push(cn);
            NiveauSalmonelle.push(ns);
            NiveauEColis.push(nec);
            NiveauBactérienListeria.push(nbl);

            time.push(ti);
          }
          this.temperatureCuve = temperatureCuve;
          this.temperatureExterieur = temperatureExterieur;
          this.poidLait = poidLait;
          this.poidProduitFini = poidProduitFini;
          this.MesurePH = MesurePH;
          this.MesureK = MesureK;
          this.ConcentrationNaCi = ConcentrationNaCi;
          this.NiveauSalmonelle = NiveauSalmonelle;
          this.NiveauEColis = NiveauEColis;
          this.NiveauBactérienListeria = NiveauBactérienListeria;

          this.time = time;
          this.loaded = true;
          this.fillData();
        })
        .catch((err) => {
          // console.log(err);
          err;
          alert("Failed to get the data 😭");
        });
    },
    exportButton() {
      // Default export is a4 paper, landscape, using millimeters for units
      var element = document.getElementById("pdf");
      var opt = {
        filename: "graphics-generator-pdf.pdf",
        image: { type: "pdf", quality: 0.98 },
        html2canvas: { scale: 2 },
        jsPDF: { unit: "in", format: "letter", orientation: "landscape" },
      };
      html2pdf(element, opt);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.area {
  width: 1000px;
  padding: 2rem;
  box-shadow: 0px 0px 5px 0px rgba(0, 0, 0, 0.3);
  border-radius: 5px;
  display: flex;
  flex-direction: column;
  justify-content: center;
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
.cloud-download {
  width: 50%;
  height: 50%;
}
.row-button {
  display: flex;
  width: 100%;
  justify-content: center;
  align-items: center;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 2rem;
}
.exportButton {
  width: 100px;
  border-radius: 5px;
  background-color: #4eb4a8;
  height: 50px;
  border-radius: 5px;
  padding: 10px;
}
.download-upload {
  width: 100%;
  height: 100%;
}
</style>
