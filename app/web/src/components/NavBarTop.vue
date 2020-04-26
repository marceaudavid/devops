<template>
  <div class="container-navBarTop">
    <Logo />
    <div class="navBarTop">
      <h1>Au bon beurre</h1>
    </div>
  </div>
</template>

<script>
import Logo from "./Logo.vue";

export default {
  name: "NavBarTop",
  components: { Logo },
  props: {
    msg: String
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container-navBarTop {
  background-color: #293d56;
  width: 100%;
  min-height: 7vh;
  display: flex;
  align-items: center;
}
.navBarTop {
  width: 85%;
  min-height: 7vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
h1 {
  color: white;
  margin: 0;
  text-align: center;
}
</style>