<template>
  <div class="pane">
    <div class="title">
      <h1>Reassess Your Chess</h1>
      <h1>4th ed.</h1>
    </div>
    <h3>Load a game</h3>
    <div>
      Page:
      <input type="text" v-model="pageNum" placeholder="Page #" />
    </div>
    <div>
      Diagram:
      <input type="text" v-model="diagramNum" placeholder="Diagram #" />
    </div>
    <button type="button" v-on:click="getBoard()">LOAD</button>
    <div v-if="showError" class="error">
      Board not found <i>(*hint: try page 1 diagram 1)</i>
    </div>
  </div>
</template>

<script>
//import fens from "../../../pdf_parsing/fens.json";
import fens from "../assets/testfens.json";

import { eventBus } from "../main";

export default {
  name: "Pane",
  data() {
    return {
      pageNum: "",
      diagramNum: "",
      showError: false
    };
  },
  methods: {
    getBoard() {
      var fen = fens[this.pageNum][this.diagramNum - 1];
      if (fen == undefined) {
        this.showError = true;
      } else {
        this.showError = false;
        // send it to Board.vue
        eventBus.$emit("updateBoard", fen);
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

a {
  color: #42b983;
}

.pane {
  float: left;
  width: 30%;
  margin: 30px;
}

#buttons {
  margin-left: 0 !important;
  margin-right: 0 !important;
}
/* Page content */
.content {
  padding: 16px;
}

.title {
  text-align: center;
}

.error {
  color: red;
}

button {
  font-style: normal;
  margin: 10px 0 10px;
  overflow: hidden;
  padding: 0.3em;
  text-decoration: none;
  transition: 2s ease;
  -webkit-transition: 2s ease;
  width: 10.6em;
}
</style>
