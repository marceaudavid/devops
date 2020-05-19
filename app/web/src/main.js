import Vue from "vue";
import VueRouter from "vue-router";
import App from "./App.vue";
import RobotsAll from "./components/RobotsAll.vue";

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
      path: "/robots/:id(\\d+)",
      component: (resolve) => require(["./components/RobotsId.vue"], resolve),
      name: "robots",
    },
    {
      path: "/robots/:id(\\d+)/customs",
      component: (resolve) => require(["./components/RobotsId2.vue"], resolve),
      name: "robotsCustoms",
    },
    {
      path: "/units/:id(\\d+)",
      component: (resolve) => require(["./components/UnitsId.vue"], resolve),
      name: "units",
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
