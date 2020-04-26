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
      temperature: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      humidity: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
      potentio: [4, 6, 4, 6, 4, 6, 4, 6, 4, 6],
      time: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
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
            label: "Temp (°C)",
            backgroundColor: "rgba(255, 0, 0, 0.2)",
            borderColor: "lightpink",
            pointBackgroundColor: "red",
            borderWidth: 1,
            pointBorderColor: "red",
            data: this.temperature
          },
          {
            label: "Hum (%)",
            backgroundColor: "rgba(0, 0, 255, 0.2)",
            borderColor: "lightblue",
            pointBackgroundColor: "blue",
            borderWidth: 1,
            pointBorderColor: "blue",
            data: this.humidity
          },
          {
            label: "Potentio",
            backgroundColor: "rgba(255, 255, 0, 0.2)",
            borderColor: "orange",
            pointBackgroundColor: "orange",
            borderWidth: 1,
            pointBorderColor: "orange",
            data: this.potentio
          }
        ]
      };
    },
    // get favoriot
    getFavoriot() {
      var url =
        "https://apiv2.favoriot.com/v2/streams?device_developer_id=projectDefault@ElCoCoZooKa5&max=10";
      var headers = {
        headers: {
          "Content-Type": "application/json",
          apikey:
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IkVsQ29Db1pvb0thNSIsInJlYWRfd3JpdGUiOnRydWUsImlhdCI6MTU4NzQ5ODMzNH0.7i-dZ-qAk7_Gy5k_5_Bc_6sbIU7TyGTondZAVkUXC6w"
        }
      };
      axios
        .get(url, headers)
        .then(x => {
          var results = x.data.results;
          var temp = [];
          var hum = [];
          var pot = [];
          var time = [];
          for (var i = 9; i >= 0; i--) {
            var t = parseInt(results[i].data.Temperature);
            var h = parseInt(results[i].data.Humidity);
            var p = parseInt(results[i].data.Potentio);
            var ti = results[i].stream_created_at.split("T");

            temp.push(t);
            hum.push(h);
            pot.push(p);
            time.push(ti);
          }
          // console.log(results)
          // console.log(temp)
          // console.log(hum)
          // console.log(pot)
          this.temperature = temp;
          this.humidity = hum;
          this.potentio = pot;
          this.time = time;
          this.loaded = true;
          this.fillData();
        })
        .catch(() => {
          alert("Failed to get the data 😭");
        });
    },
    // post favoriot
    postFavoriot() {
      var url = "https://apiv2.favoriot.com/v2/streams";
      var headers = {
        headers: {
          "Content-Type": "application/json",
          apikey:
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IkVsQ29Db1pvb0thNSIsInJlYWRfd3JpdGUiOnRydWUsImlhdCI6MTU4NzQ5ODMzNH0.7i-dZ-qAk7_Gy5k_5_Bc_6sbIU7TyGTondZAVkUXC6w"
        }
      };
      var dataBody = {
        device_developer_id: "projectDefault@ElCoCoZooKa5",
        data: {
          Temperature: this.$refs.temp.value,
          Humidity: this.$refs.hum.value,
          Potentio: this.$refs.pot.value
        }
      };
      var checkUnit = document.Form.unit.value;

      if (checkUnit == "") {
        alert("Please complete the entire form");
        return false;
      } else {
        axios
          .post(url, dataBody, headers)
          .then(() => {
            alert("Data posted successfully! 😍");
            this.getFavoriot();
          })
          .catch(() => {
            alert("Failed to post the data 😭");
          });
      }
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
}
img {
  width: 50%;
  height: 50%;
}
</style>
