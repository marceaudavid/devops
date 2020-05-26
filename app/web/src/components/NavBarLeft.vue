<template>
  <div class="container-navBarLeft">
    <div class="container-menu">
      <h2>MENU:</h2>
    </div>
    <div class="filter">
      <div class="graph">
        <router-link :to="{ name: 'root' }" class="link">Tous les Robots</router-link>
        <router-link
          :to="{ name: 'RobotsAllMilkWeight' }"
          class="link"
        >Poid du lait de tous les Robots</router-link>
        <router-link
          :to="{ name: 'UnitsId', params: { id: 1 } }"
          class="link"
        >Tous les Robots par Unité</router-link>
        <router-link
          :to="{ name: 'UnitsIdMilkWeight', params: { id: 1 } }"
          class="link"
        >Poid du lait de tous les Robots par Unité</router-link>
        <router-link :to="{ name: 'RobotsId', params: { id: 1 } }" class="link">Choix des Robots</router-link>
        <router-link
          :to="{ name: 'RobotsIdMilkWeight', params: { id: 1 } }"
          class="link"
        >Choix des Robots Customs</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "NavBarLeft",
  components: {},
  props: {
    msg: String
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container-navBarLeft {
  width: 15%;
  background-color: #293d56;
}
.container-menu {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 10%;
}
.filter {
  background-color: #293d56;
  width: 100%;
  height: 90%;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.graph {
  width: 100%;
  display: flex;
  flex-direction: column;
  font-size: 30px;
  justify-content: space-between;
}
.link {
  font-size: 25px;
  color: white;
  padding: 1rem 0;
  outline: none;
  text-decoration: none;
}
.link:hover {
  background: #1a222f;
}
.link:active {
  background: gray;
}
.router-link-exact-active {
  background: #1a222f;
}
h2 {
  margin: 0;
  color: white;
}
</style>
