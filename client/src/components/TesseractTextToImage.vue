<!--
This component uploads an image to the web server and extracts the text from that image.
The text is than displayed as a result of the upload.
-->

<template>
<!-- TODO: need to fix layout and make it look smooth. -->
<!--  TODO: need a way to reset and send another image. -->
  <div class="container">
    <div class="row-cols-1">
      <h2>Select an image</h2>
    </div>
    <div v-if="!image" class="row-cols-1">
      <input type="file" @change="uploadFile()" ref="file" class="form-control-file">
    </div>
    <div v-else class="row-cols-1">
      <img id="output" width="200" :src="image" class="img-rounded" alt="No Image" />
    </div>
    <div class="row-cols-1">
      <button @click="submitFile" class="btn btn-primary">Upload!</button>
    </div>
    <div class="row-cols-1">
      <p>{{ output }}</p>
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
          axios.post('http://localhost:5000/getText', formData, { headers }).then((res) => {
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