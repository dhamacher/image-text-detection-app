<!--
HelloWorld example, the classic and most boring! I used this as a reference for props.
TODO Remove this component since it is not really useful unless for reference purposes.
-->
<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-sm-10 component-layout">
        <h1>{{ msg }}</h1>
        <h4>This app can be used to extract text from images using Google's Tesseract OCR engine.
        The front end is build with Vue.js, which I never used before.</h4>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!--&lt;!&ndash; Add "scoped" attribute to limit CSS to this component only &ndash;&gt;-->
<!--<style scoped>-->
<!--h3 {-->
<!--  margin: 40px 0 0;-->
<!--}-->
<!--ul {-->
<!--  list-style-type: none;-->
<!--  padding: 0;-->
<!--}-->
<!--li {-->
<!--  display: inline-block;-->
<!--  margin: 0 10px;-->
<!--}-->
<!--a {-->
<!--  color: #42b983;-->
<!--}-->
<!--</style>-->
