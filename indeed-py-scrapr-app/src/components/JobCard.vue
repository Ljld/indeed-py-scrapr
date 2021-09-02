<template>
    <div class="mission-card">
        <h3>React Native developer</h3>
        <p>
        Looking for a senior dev{{jobDesc}} in React Native 5+ years of xp. <br>
        Other skills required : Gitlab, AWS. <br>
        Salary : $80K
        </p>
        <p>{{jobDesc}}</p>
        <p>{{element}}</p>
    </div>
</template>

<script>
//import axios from 'axios';

export default {
  name: 'JobCard',
  data: function () {
      return {
        jobDesc: null,
        element: 2
      }
  },
  mounted() {
      this.element += 18;
      //console.log("Hey !");
      /*axios.get(`http://127.0.0.1:5000/jobs`)
        .then(response => {
        // JSON responses are automatically parsed.
        this.jobDesc = response;
        console.log(response);
        });*/

    



  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a {
  color: #42b983;
}
h3 {
    margin-bottom: 0.2em;
    /*color: #3700b3;*/
}

h3:hover {
    /*margin-left: 10px;*/
    /*animation: 100ms slide-right ease;*/
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
