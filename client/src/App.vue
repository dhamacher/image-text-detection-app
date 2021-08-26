<template>
  <div id="app" class="content-panel justify-content-center">
    <div id="nav" class="row justify-content-center">
      <div class="col-sm-10">
        <router-link class="router-link" to="/" >Home</router-link>
        <router-link class="router-link" to="/about">About</router-link>
        <router-link class="router-link" to="/health-check">Status</router-link>
      </div>
    </div>
    <router-view/>
  </div>
</template>

<style>
#nav a {
  font-weight: bold;
  color: #2c3e50;
  font-size: 35px;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.content-panel {
  background: antiquewhite;
  padding: 25px;
  margin-top: 10px;
  margin-left: 25px;
  margin-right: 25px;
}

.component-layout {
  padding: 10px;
}

.router-link {
  padding: 20px;
}

.body {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background: #2c3e50;
}
</style>
