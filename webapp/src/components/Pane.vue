<template>
  <div class="pane">
    <h1>Reassess Your Chess</h1>
    <h1>4th ed.</h1>
    <h3>Search for page</h3>
    <div>Page #:</div>
    <div
      id="buttons"
      class="ui grey three item inverted bottom fixed menu transition hidden"
    >
      <a class="item" @click="page > 1 ? page-- : 1">
        <i class="left chevron icon"></i>
        Back
      </a>
      <a class="ui active item">
        {{ page }} / {{ numPages ? numPages : "∞" }}
      </a>
      <a class="item" @click="page < numPages ? page++ : 1">
        Forward
        <i class="right chevron icon"></i>
      </a>
    </div>
    <div id="pdfvuer">
      <pdf
        :src="pdfdata"
        v-for="i in numPages"
        :key="i"
        :id="i"
        :page="i"
        :scale="scale"
        style="width:100%;margin:20px auto;"
      >
        <template slot="loading">
          loading content here...
        </template>
      </pdf>
    </div>
    <!--pdf2
      src="ReassessYourChess.pdf"
      @num-pages="pageCount = $event"
      @page-loaded="currentPage = $event"
    ></pdf2-->
    <!--PDFDocument v-bind="{ url, scale }" /-->
  </div>
</template>

<script>
// import pdf2 from "vue-pdf";
import pdfvuer from "pdfvuer";
// import PDFDocument from "./PDFDocument";
import $ from "jquery";

export default {
  name: "Pane",
  components: {
    pdf: pdfvuer
    // pdf2
    //PDFDocument,
  },
  data() {
    return {
      page: 1,
      numPages: 0,
      pdfdata: undefined,
      errors: [],
      scale: "page-width"
    };
  },
  mounted() {
    this.getPdf();
  },
  watch: {
    show: function(s) {
      if (s) {
        this.getPdf();
      }
    },
    page: function(p) {
      if (
        window.pageYOffset <= this.findPos(document.getElementById(p)) ||
        (document.getElementById(p + 1) &&
          window.pageYOffset >= this.findPos(document.getElementById(p + 1)))
      ) {
        // window.scrollTo(0,this.findPos(document.getElementById(p)));
        document.getElementById(p).scrollIntoView();
      }
    }
  },
  methods: {
    getPdf() {
      var self = this;
      self.pdfdata = pdfvuer.createLoadingTask("2-1-Make.pdf");
      self.pdfdata.then(pdf => {
        self.numPages = pdf.numPages;
        window.onscroll = function() {
          changePage();
          stickyNav();
        };

        // Get the offset position of the navbar
        var sticky = $("#buttons")[0].offsetTop;

        // Add the sticky class to the self.$refs.nav when you reach its scroll position. Remove "sticky" when you leave the scroll position
        function stickyNav() {
          if (window.pageYOffset >= sticky) {
            $("#buttons")[0].classList.remove("hidden");
          } else {
            $("#buttons")[0].classList.add("hidden");
          }
        }

        function changePage() {
          var i = 1,
            count = Number(pdf.numPages);
          do {
            if (
              window.pageYOffset >= self.findPos(document.getElementById(i)) &&
              window.pageYOffset <= self.findPos(document.getElementById(i + 1))
            ) {
              self.page = i;
            }
            i++;
          } while (i < count);
          if (window.pageYOffset >= self.findPos(document.getElementById(i))) {
            self.page = i;
          }
        }
      });
    },
    findPos(obj) {
      return obj.offsetTop;
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
}

#buttons {
  margin-left: 0 !important;
  margin-right: 0 !important;
}
/* Page content */
.content {
  padding: 16px;
}

#pdfvuer {
  max-height: 300px;
  overflow-y: scroll;
}
</style>
