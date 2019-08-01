<template>
  <div class="board">
    <h3>Turn: {{ turn }}</h3>
    <chessboard :fen="currentFen" @onMove="showInfo"></chessboard>
  </div>
</template>

<script>
import { chessboard } from "vue-chessboard";
// import "vue-chessboard/dist/vue-chessboard.css";
import { eventBus } from "../main";

export default {
  name: "Board",
  components: { chessboard },
  data() {
    return {
      currentFen: "",
      turn: "white"
    };
  },
  methods: {
    showInfo(data) {
      this.turn = data.turn;
    }
  },
  mounted() {
    eventBus.$on("updateBoard", fen => {
      this.currentFen = fen;
      console.log(this.currentFen);
    });
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.board {
  float: right;
  width: 60%;
  margin: 0;
}

.cg-board {
  width: 320px;
  height: 320px;
}
</style>
