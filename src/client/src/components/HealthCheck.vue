<template>
  <div class="container">
    <div v-if="msg.length > 0" class='row-cols-1'>
      <h3 class="h3">{{ msg }}</h3>
    </div>
    <div v-else class="row-cols-1">

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
      const path = 'http://localhost:5000/health-check';
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