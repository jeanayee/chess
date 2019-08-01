<template>
  <div class="board">
    <h1>{{ number }}</h1>
    <chessboard></chessboard>
  </div>
</template>

<script>
import { chessboard } from "vue-chessboard";
// import "vue-chessboard/dist/vue-chessboard.css";

export default {
  name: "Board",
  components: { chessboard },
  data() {
    return {
      number: 0
    };
  },
  methods: {
    test() {
      console.log(this.number);
      if (this.number === 3) {
        return 3;
      } else {
        return 0;
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

.board {
  float: right;
  width: 60%;
}
</style>
