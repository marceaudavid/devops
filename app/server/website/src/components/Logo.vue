<template>
  <div class="container-logo">
    <a href="#" class="col-logo">
      <img class="logo" src="./../assets/logo.svg" alt="Logo" />
    </a>
  </div>
</template>

<script>
export default {
  name: "Logo",
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container-logo {
  background-color: #1a222f;
  width: 15%;
  min-height: 7vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
.col-logo {
  width: 100%;
  height: 7vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
.logo {
  width: 100%;
  height: 80%;
}
</style>
