<template>
  <div class="container-navBarLeft">
    <div class="filter">
      <div class="graph">
        <h2>le graph 1</h2>
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
}
.filter {
  background-color: #293d56;
  width: 100%;
  min-height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
h2 {
  margin: 0;
  color: white;
}
</style>
