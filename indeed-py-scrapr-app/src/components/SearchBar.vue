<template>
    <div class="search-bar">
        <input v-model="research" @search-for="test" placeholder="Poste" />
        <input v-model="location" @click="test" placeholder="Lieu" />
        <button @click='$emit("searchFor", `http://127.0.0.1:5000/jobs?search=${this.research}&l=${this.location}`)'>Search</button>
    </div>
</template>

<script>
//import axios from 'axios';

export default {
  name: 'SearchBar',
  data: function () {
      return {
        research: null,
        location: null
      }
  },
  methods: {
      test () {
          console.log('teest');
      },
      searchFor () {
        //this.$emit('searchFor', `http://127.0.0.1:5000/jobs?search=${this.research}&l=${this.location}`);
        //this.$emit('searchFor');
        console.log("boom1");
        /*console.log(this.research);
        axios.get(`http://127.0.0.1:5000/jobs?search=${this.research}&l=${this.location}`)
            .then(response => {
                this.jobs = response.data;
                console.log(this.jobs);
            });*/
      },
      searchEvent () {
          this.$emit('search');
      }
  } 
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
