<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <SearchBar @search-for="loadJobs"/>
    <div class="mission-card" v-for="job in jobs" v-bind:key="job">
        <h3>{{job.title}}</h3>
        <p>
          {{job.summary}} <br>
          Salary : {{job.salary}}
        </p>
    </div>
    
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
  props: {
    msg: String,
  },
  data: function () {
      return {
        jobs: {}
      }
  },
  methods: {
    test () {
      console.log('test');
    },
    loadJobs (search) {
      axios.get(search)
        .then(response => {
        // JSON responses are automatically parsed.
        this.jobs = response.data;
        console.log(this.jobs);
        });
    }
  }/*,
  created() {
      axios.get(`http://127.0.0.1:5000/jobs`)
        .then(response => {
        // JSON responses are automatically parsed.
        this.jobs = response.data;
        console.log(this.jobs);
        });

  }*/
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

template {
  display: flex;
  justify-content: center;
}

a {
  color: #42b983;
}
h3 {
    margin-bottom: 0.2em;
    /*color: #3700b3;*/
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
    /*border-radius: 0;*/
    /*border-bottom-color: blue;*/
    border-color: #3700b3;
    
}

.mission-card > * {
    transition: margin-left 100ms ease;
}

.mission-card:hover > * {
    margin-left: 10px;
}

.mission-card:hover > * {
    /*animation: slide-right 100ms ease;*/
}

@keyframes slide-right {
  0%   {
      margin-left: 0;
      }
  100% {
      
      }
}
</style>
