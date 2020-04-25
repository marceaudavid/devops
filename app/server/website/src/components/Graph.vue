<template>
  <div class="area">
    <form name="Form">
      <div class="input-field">
        <label for="temp">Temperature...</label>
        <input
          id="temp"
          name="temp"
          type="number"
          class="validate"
          placeholder="Temperature..."
          ref="temp"
          min="0"
          max="1000"
          required
        />
      </div>

      <div class="input-field">
        <label for="hum">Humidity...</label>
        <input
          id="hum"
          name="hum"
          type="number"
          class="validate"
          placeholder="Humidity..."
          ref="hum"
          min="0"
          max="1000"
          required
        />
      </div>

      <div class="input-field">
        <label for="pot">Potentio...</label>
        <input
          id="pot"
          name="pot"
          type="number"
          class="validate"
          placeholder="Potentio..."
          ref="pot"
          min="0"
          max="1000"
          required
        />
      </div>

      <div class="button-col">
        <div class="row">
          <a class="button-get" @click="getFavoriot()">
            <img src="../assets/cloud-download-outline.svg" alt="cloud-download" />
          </a>
          <a class="button-post" @click="postFavoriot()">
            <img src="../assets/cloud-upload-outline.svg" alt="cloud-upload" />
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
      var checkTemp = document.Form.temp.value;
      var checkHum = document.Form.hum.value;
      var checkPot = document.Form.pot.value;

      if (checkTemp == "") {
        alert("Please complete the entire form");
        return false;
      }
      if (checkHum == "") {
        alert("Please complete the entire form");
        return false;
      }
      if (checkPot == "") {
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
}
form {
  display: flex;
  justify-content: space-between;
  margin-bottom: 2rem;
}
.input-field {
  width: 20%;
}
.validate {
  width: 100%;
  height: 2rem;
  border: none;
  border-bottom: 1px black solid;
  -webkit-appearance: none;
  margin: 0;
  -moz-appearance: textfield;
}
.validate:focus {
  border-bottom: 2px #248b85 solid;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  margin: 0;
}
.button-col {
  width: 25%;
}
.row {
  width: 100%;
  height: 100%;
  display: flex;
}
.button-get {
  display: inline-flex;
  background-color: #4eb4a8;
  width: 50%;
  height: 100%;
  justify-content: center;
  align-items: center;
  border-radius: 5px;
}
.button-post {
  display: inline-flex;
  background-color: #f06593;
  width: 50%;
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
