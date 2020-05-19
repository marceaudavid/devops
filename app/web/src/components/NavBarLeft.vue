<template>
  <div class="container-navBarLeft">
    <div class="filter">
      <div class="graph">
        <router-link :to="{ name: 'root' }" class="link"
          >Tous les Robots</router-link
        >
        <router-link :to="{ name: 'robots', params: { id: 1 } }" class="link"
          >Robots 1</router-link
        >
        <router-link
          :to="{ name: 'robotsCustoms', params: { id: 1 } }"
          class="link"
          >Robots 1 Customs</router-link
        >
        <router-link :to="{ name: 'units', params: { id: 1 } }" class="link"
          >Tous les Robots de l'Unité 1</router-link
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "NavBarLeft",
  components: {},
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container-navBarLeft {
  width: 15%;
}
.filter {
  background-color: #293d56;
  width: 100%;
  height: 100%;
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
  font-size: 30px;
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
