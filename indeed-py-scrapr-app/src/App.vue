<template>
  <JobCardContainer/>
</template>

<script>
import JobCardContainer from './components/JobCardContainer.vue';

export default {
  name: 'App',
  components: {
    JobCardContainer
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0;
  background-color: #f6f6f6;
  min-height: 100vh;
}

h1 {
  color: white;
  font-size: 5rem;
}
</style>
