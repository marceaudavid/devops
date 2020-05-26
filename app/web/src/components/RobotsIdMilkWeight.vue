<template>
  <div id="pdf2" class="area">
    <form name="Form">
      <div class="input-field">
        <label for="unit">Robots...</label>
        <div class="formfield-select--container">
          <select id="unit" name="unit" class="unit" @change="getData()" v-model="selected">
            <option value="1">Robot 1</option>
            <option value="2">Robot 2</option>
            <option value="3">Robot 3</option>
            <option value="4">Robot 4</option>
            <option value="5">Robot 5</option>
          </select>
        </div>
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
    <line-chart :chart-data="datacollection" :styles="styles" :height="null" :width="null"></line-chart>
    <div class="row-button">
      <a class="exportButton" @click="exportButton()">
        <img class="download-upload" src="../assets/download-outline.svg" alt="download-upload" />
      </a>
    </div>
  </div>
</template>

<script>
import LineChart from "./LineChart.js";
import axios from "axios";
import html2pdf from "html2pdf.js";

export default {
  name: "RobotsId2",
  props: {
    msg: String
  },
  components: {
    LineChart
  },
  data() {
    return {
      selected: 1,
      datacollection: null,
      loaded: false,
      poidLait: [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
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
    this.getData();
  },
  methods: {
    fillData() {
      this.datacollection = {
        labels: this.time,
        datasets: [
          {
            label: "Poid du lait (Kg)",
            backgroundColor: "rgba(255, 255, 0, 0.2)",
            borderColor: "orange",
            pointBackgroundColor: "orange",
            borderWidth: 1,
            pointBorderColor: "orange",
            data: this.poidLait
          }
        ]
      };
    },
    // get
    getData() {
      var url = `http://localhost:3000/robot/${this.selected}`;
      var headers = {
        headers: {
          "Content-Type": "application/json"
        }
      };
      axios
        .get(url, headers)
        .then(x => {
          var results = x.data;

          var poidLait = [];
          var time = [];
          for (var i = 20; i >= 0; i--) {
            var pl = parseInt(results[0].weight_of_milk_in_tank);

            var ti = results[0].creation_time.split("T");
            poidLait.push(pl);

            time.push(ti);
          }
          this.poidLait = poidLait;

          this.time = time;
          this.loaded = true;
          this.fillData();
        })
        .catch(err => {
          err;
          alert("Failed to get the data 😭");
        });
    },
    exportButton() {
      // Default export is a4 paper, landscape, using millimeters for units
      var element = document.getElementById("pdf2");
      var opt = {
        filename: "graphics-generator-pdf.pdf",
        image: { type: "pdf", quality: 0.98 },
        html2canvas: { scale: 2 },
        jsPDF: { unit: "in", format: "letter", orientation: "landscape" }
      };

      html2pdf(element, opt);
    }
  }
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
  color: #293d56;
}
.formfield-select--container {
  position: relative;
  background-color: #fff;
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
  color: #293d56;
  cursor: pointer;
  border-bottom: 1px #293d56 solid;
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
