import Vue from "vue";
import App from "./App.vue";
// import chessboard from "vue-chessboard";

// Vue.component("chessboard", chessboard);
/* Vue.component("chessboard", {
  template: `<a><slot></slot></a>`
}); */

Vue.config.productionTip = false;

export const eventBus = new Vue();

new Vue({
  render: h => h(App)
}).$mount("#app");
