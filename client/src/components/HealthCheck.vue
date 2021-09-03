<!--
This template is used to get a health check from the backend web server.
A JSON object is returned with metadata from the server and the current status.
-->
<template>
  <div class="container component-layout">
    <div v-if="msg.length > 0" class='row-cols-1'>
      <h3 class="h3">{{ msg }}</h3>
    </div>
    <div v-else class="row-cols-1">
      <h2>Server is offline</h2>
    </div>
  </div>
</template>

<script>
import axios from 'axios';


export default {
  name: 'HealthCheck',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:80/health-check';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>