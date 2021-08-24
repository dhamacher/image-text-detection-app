<template>
  <div class="container">
    <img alt="Vue logo" src="../assets/logo.png" class="row-cols-1">
    <HelloWorld msg="Get Text From Images" class="row-cols-1"/>
    <TesseractTextToImage title="upload" class="row-cols-1"/>
  </div>
</template>

<script>
// @ is an alias to /src
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
