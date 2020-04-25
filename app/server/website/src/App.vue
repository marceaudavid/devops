<template>
  <div id="app">
    <NavBarTop />
    <div class="container">
      <NavBarLeft />
      <div class="container-graph">
        <div class="title-graph">
          <h1>graph 1</h1>
        </div>
        <Graph />
      </div>
    </div>
  </div>
</template>

<script>
import NavBarLeft from "./components/NavBarLeft.vue";
import NavBarTop from "./components/NavBarTop.vue";
import Graph from "./components/Graph.vue";

export default {
  name: "App",
  components: {
    NavBarLeft,
    NavBarTop,
    Graph,
  },
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
  width: 85%;
  height: 100%;
}
.title-graph {
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
</style>
