<template>
  <div class="container content-panel" >
    <div class="row justify-content-center">
      <div class="col-sm-10">
        <img alt="Vue logo" src="../assets/logo.png">
        <img alt="Vue logo" src="../assets/google_tesseract.png">
        <HelloWorld msg="Get Text From Images"  />
        <TesseractTextToImage title="upload" />
      </div>
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
