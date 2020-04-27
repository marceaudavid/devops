<template>
  <div class="row-button">
    <a class="exportButton" @click="exportButton()">
      <img src="../assets/download-outline.svg" alt="download-upload" />
    </a>
  </div>
</template>

<script>
import jsPDF from "jspdf";
export default {
  name: "ExportButton",
  props: {
    msg: String,
  },
  methods: {
    exportButton() {
      // Default export is a4 paper, portrait, using millimeters for units
      var doc = new jsPDF();
      var source = window.document.getElementsByTagName("body")[0];
      doc.fromHTML(source, 15, 15, {
        width: 180,
      });
      doc.text("PDF GENERATOR GRAPH 1", 10, 10);
      doc.save("graphics-generator-pdf.pdf");
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.row-button {
  display: inline-flex;
  background-color: #4eb4a8;
  width: 100%;
  height: 10%;
  justify-content: center;
  align-items: center;
  border-radius: 5px;
  cursor: pointer;
}
.exportButton {
  width: 50%;
  height: 50%;
}
img {
  width: 100%;
  height: 100%;
}
</style>
