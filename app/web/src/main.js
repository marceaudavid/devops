import Vue from "vue";
import VueRouter from "vue-router";
import App from "./App.vue";
import Graph from "./components/Graph.vue";

Vue.config.productionTip = false;
Vue.use(VueRouter);

require(["./components/GraphRobot1.vue"], function(GraphRobot1) {
  console.log(GraphRobot1);
});

const router = new VueRouter({
  mode: "history",
  routes: [
    {
      path: "/",
      component: Graph,
      name: "root",
    },
    {
      path: "/robot/:id(\\d+)",
      component: (resolve) =>
        require(["./components/GraphRobot1.vue"], resolve),
      name: "robot",
    },
    {
      path: "*",
      redirect: "/",
    },
  ],
});

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
