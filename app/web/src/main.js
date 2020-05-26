import Vue from "vue";
import VueRouter from "vue-router";
import App from "./App.vue";
import RobotsAll from "./components/RobotsAll.vue";
import RobotsAllMilkWeight from "./components/RobotsAllMilkWeight.vue";

Vue.config.productionTip = false;
Vue.use(VueRouter);

const router = new VueRouter({
  mode: "history",
  routes: [
    {
      path: "/",
      component: RobotsAll,
      name: "root",
    },
    {
      path: "/MilkWeight",
      component: RobotsAllMilkWeight,
      name: "RobotsAllMilkWeight",
    },
    {
      path: "/robots/:id(\\d+)",
      component: (resolve) => require(["./components/RobotsId.vue"], resolve),
      name: "RobotsId",
    },
    {
      path: "/robots/:id(\\d+)/MilkWeight",
      component: (resolve) =>
        require(["./components/RobotsIdMilkWeight.vue"], resolve),
      name: "RobotsIdMilkWeight",
    },
    {
      path: "/units/:id(\\d+)",
      component: (resolve) => require(["./components/UnitsId.vue"], resolve),
      name: "UnitsId",
    },
    {
      path: "/units/:id(\\d+)/MilkWeight",
      component: (resolve) =>
        require(["./components/UnitsIdMilkWeight.vue"], resolve),
      name: "UnitsIdMilkWeight",
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
