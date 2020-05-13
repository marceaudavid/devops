<template>
  <div id="app">
    <NavBarTop />
    <div class="container">
      <NavBarLeft />
      <div class="container-graph">
        <Graph />
        <GraphRobot1 />
        <div class="contenent-arrow">
          <a @click="functionArrow()" id="arrow">
            <img class="arrow" src="./assets/chevron-down-outline.svg" alt="chevron-down-outline" />
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavBarLeft from "./components/NavBarLeft.vue";
import NavBarTop from "./components/NavBarTop.vue";
import Graph from "./components/Graph.vue";
import GraphRobot1 from "./components/GraphRobot1.vue";

export default {
  name: "App",
  components: {
    NavBarLeft,
    NavBarTop,
    Graph,
    GraphRobot1
  },
  methods: {
    functionArrow() {
      //récuperer la hauteur de ma page
      // var h = window.scrollMaxY + document.body.offsetHeight;

      //récuper la hauteur de ma fenetre
      // var hauteur = window.innerHeight;

      // Récuperer la balise fleche du fichier html
      var x = document.getElementById("arrow");

      // Récuperer la valeur px du body en fonction du haut de la fenetre de l'utilisateur
      var top = window.scrollY;
      console.log(top);

      if (top >= 0 && top <= 742) {
        window.scrollTo({
          top: 1000,
          left: 0,
          behavior: "smooth"
        });
        x.style.transform = "rotate(180deg)";
      }
      // if (top >= 728 && top <= 1456) {
      //   window.scrollTo(0, 1456);
      // }
      // if (top >= 1456 && top <= 2184) {
      //   window.scrollTo(0, 2184);
      //   x.style.transform = "rotate(180deg)";
      // }
      if (top >= 742 && top <= 742) {
        window.scroll({
          top: 0,
          left: 0,
          behavior: "smooth"
        });
        x.style.transform = "rotate(0deg)";
      }
    }
  }
};
</script>

<style>
* {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
}
#app {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100vh;
}
.container {
  display: flex;
  width: 100%;
}
.container-graph {
  width: 85%;
}
.contenent-arrow {
  position: fixed;
  bottom: 0;
  width: 81%;
  height: 30px;
  display: flex;
  align-content: center;
  justify-content: flex-end;
  margin: 2rem;
}
#arrow {
  width: 30px;
  height: 30px;
  transform: rotate(0deg);
  transition: transform 0.5s;
  background-color: #4eb4a8;
  border-radius: 5px;
  box-shadow: 0px 0px 5px 0px rgba(0, 0, 0, 0.3);
}
.arrow {
  width: 100%;
  height: 100%;
}
</style>
