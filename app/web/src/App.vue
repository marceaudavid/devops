<template>
  <div id="app">
    <NavBarTop />
    <div class="container">
      <NavBarLeft />
      <div class="container-graph">
        <Graph />
      </div>
      <div class="container-eportButton">
        <ExportButton />
      </div>
    </div>
  </div>
</template>

<script>
import NavBarLeft from "./components/NavBarLeft.vue";
import NavBarTop from "./components/NavBarTop.vue";
import Graph from "./components/Graph.vue";
import ExportButton from "./components/ExportButton.vue";

export default {
  name: "App",
  components: {
    NavBarLeft,
    NavBarTop,
    Graph,
    ExportButton
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
  height: 93vh;
}
.container-graph {
  width: 75%;
  height: 100%;
}
.container-eportButton {
  width: 10%;
  height: 100%;
}
</style>
