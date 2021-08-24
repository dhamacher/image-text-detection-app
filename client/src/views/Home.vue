<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-1"></div>
      <div class="col-2">        <img alt="Vue logo" src="../assets/logo.png" class="row-cols-1">
        <HelloWorld msg="Get Text From Images" class="row-cols-1"/>
        <TesseractTextToImage title="upload" class="row-cols-1"/>
      </div>
      <div class="col-3"></div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /server
import HelloWorld from '@/components/HelloWorld.vue'
import TesseractTextToImage from '@/components/TesseractTextToImage.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld,
    TesseractTextToImage
  }
}
</script>
