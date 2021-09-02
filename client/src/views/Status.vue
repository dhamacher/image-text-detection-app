<template>
  <div class="container content-panel justify-content-center" >
    <div class="row justify-content-center">
      <div class="col-sm-10">
        <HealthCheck  />
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /server
import HealthCheck from "@/components/HealthCheck";

export default {
  name: 'Status',
  components: {
    HealthCheck,
  }
}
</script>
