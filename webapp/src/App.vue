<template>
  <div id="app">
    <Pane msg="Welcome to Your Vue.js App" />
    <Board />
  </div>
</template>

<script>
import Pane from "./components/Pane.vue";
import Board from "./components/Board.vue";

export default {
  name: "app",
  components: {
    Pane,
    Board
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
