<template>
    <div class="search-bar">
        <input @keyup.enter='$emit("searchFor", `http://127.0.0.1:5000/jobs?search=${this.research}&l=${this.location}`)' v-model="research"  placeholder="Poste" />
        <input @keyup.enter='$emit("searchFor", `http://127.0.0.1:5000/jobs?search=${this.research}&l=${this.location}`)' v-model="location" placeholder="Lieu" />
        <button @click='$emit("searchFor", `http://127.0.0.1:5000/jobs?search=${this.research}&l=${this.location}`)'>Search</button>
    </div>
</template>

<script>

export default {
  name: 'SearchBar',
  data: function () {
      return {
        research: null,
        location: null
      }
  }
}
</script>

<style scoped>

input {
    padding: 1em 3em;
    margin: 1em;
    border: none;
    border-radius: 25px;
    outline: none;
}

button {
    border-radius: 25px;
    outline: 3px solid white;
    border: none;
    background-color: transparent;
    color: white;
    padding: 1em 3em;
    margin: 1em;
    transition: all 100ms linear;
}

button:hover {
    cursor: pointer;
}

button:active {
    outline-width: 1px;
}

</style>
