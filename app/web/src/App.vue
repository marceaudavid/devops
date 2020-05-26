<template>
  <div id="app">
    <NavBarTop />
    <div class="container">
      <NavBarLeft />
      <div class="container-graph">
        <transition name="fade" mode="out-in">
          <router-view></router-view>
        </transition>
      </div>
    </div>
  </div>
</template>

<script>
import NavBarLeft from "./components/NavBarLeft.vue";
import NavBarTop from "./components/NavBarTop.vue";

export default {
  name: "App",
  components: {
    NavBarLeft,
    NavBarTop
  },
  methods: {}
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
  height: 93vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  overflow-y: auto;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>
