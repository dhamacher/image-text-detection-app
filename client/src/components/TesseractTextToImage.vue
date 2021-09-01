<!--
This component uploads an image to the web server and extracts the text from that image.
The text is than displayed as a result of the upload.
-->

<template>
  <div class="container">
    <div class="row justify-content-center">
      <div v-if="!image" class="col-sm-10">
          <h2 class="component-layout">Select an image</h2>
          <input class="component-layout form-control form-control-lg" type="file" @change="uploadFile()" ref="file" >
      </div>
      <div v-else class="col-sm-10">
        <h2 class="component-layout">Select an image</h2>
        <input class="form-control form-control-lg component-layout" type="file" @change="uploadFile()" ref="file" >
          <img id="output" :src="image" class="img-rounded img-fluid component-layout" alt="No Image" />
          <button @click="submitFile" class="btn btn-primary btn-lg component-layout">Extract Text</button>
<!--          TODO: Beautify the text output, add pasting to clipboard, download as a file (radio buttons?) -->
          <p class="component-layout">{{ output }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ImageUpload',
  data() {
    return {
      image: false,
      path: '',
      output: 'Nothing Returned Yet!'
    }
  },
  methods:
      {
        uploadFile()
        {
          this.path = this.$refs.file.files[0];
          this.createImage(this.image, this.path);
        },
        submitFile() {
          const formData = new FormData();
          formData.append('file', this.path);
          const headers = { 'Content-Type': 'multipart/form-data' };
          axios.post('http://backend/getText', formData, { headers }).then((res) => {
            res.data.files; // binary representation of the file
            res.status; // HTTP status
            this.output = res.data
          })
        },
        createImage(image, file) {
          var reader = new FileReader();
          reader.onload = (e) => {
            this.image = e.target.result;
          };
          reader.readAsDataURL(file);
        },
      },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>