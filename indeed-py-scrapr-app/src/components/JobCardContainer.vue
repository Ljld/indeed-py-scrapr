<template>
  <div>
    <header>
      <h1>Indeed PyScrapr</h1>
      <SearchBar @search-for="loadJobs"/>
    </header>
    <section class="cards">
      <div class="mission-card" v-for="job in jobs" v-bind:key="job">
          <a :href="job.link">
            <h3>{{job.title}}</h3>
            <p>
              {{job.summary}} <br>
              Salary : {{job.salary}}
            </p>
          </a>
      </div>
    </section>
  </div>  
</template>

<script>
import axios from 'axios';
import SearchBar from './SearchBar.vue'

export default {
  name: 'JobCardContainer',
  components: {
    SearchBar
  },
  data: function () {
      return {
        jobs: {}
      }
  },
  methods: {
    loadJobs (search) {
      axios.get(search).then(response => this.jobs = response.data);
    }
  }
}
</script>

<style scoped>

header {
  background: rgb(33,12,164);
  background: linear-gradient(184deg, rgba(33,12,164,1) 0%, rgba(19,57,202,1) 37%, rgba(7,97,236,1) 79%, rgba(0,119,255,1) 100%);
  padding: 1em;
  height: 12em;
}

ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}

template {
  display: flex;
  justify-content: center;
}

a {
  color: inherit;
  text-decoration: none;
}

h3 {
    margin-bottom: 0.2em;
}

.mission-card {
    background-color: white;
    max-width: 30em;
    margin: auto;
    text-align: left;
    border: transparent solid 2px;
    margin-bottom: 1em;
    margin-top: 1em;
    padding: 1em;
    border-radius: 9px;
    box-shadow: 0 2px 5px 1px rgb(64 60 67 / 16%);
    transition: all 1000ms ease;
    border-width: 3px;
    
}

.mission-card:hover {
    box-shadow: 0 8px 5px 1px rgb(64 60 67 / 16%);
    border-color: #1339ca;
    
}

.mission-card > * {
    transition: margin-left 100ms ease;
}

.mission-card:hover > * {
    margin-left: 10px;
}

.cards {
  padding: 1em;
}

</style>
