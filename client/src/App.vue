<template>
  <!-- TODO: need to fix layout and make it look smooth -->
  <div id="app" class="container-sm">
    <div id="nav" class="row">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/health-check">Status</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
  margin-top: 60px;
  margin-left: 30px;
  margin-right: 30px; 
}

#nav {
  padding: 30px;
}
</style>

<!--
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}



#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
-->