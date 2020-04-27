<template>
  <div id="app">
    <NavBarTop />
    <div class="container">
      <NavBarLeft />
      <div class="container-graph">
        <Graph />
        <GraphRobot1 />
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
</style>
