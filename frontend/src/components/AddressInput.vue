<template>
    <!--
    <p>Message is: {{ message }}</p>
      <input v-model="message" placeholder="edit me" />
    -->
    
    <!-- input address in HTML text box input, pressing submit does nothing yet-->
      <label for="address">Address:</label>
      <input type="text" id="address" name="address" placeholder="Type your address...">
      <button style= "color:white;background-color: #5A2E47" @click="emitData">Submit</button>

      <!-- longitude -->
      <label for="longitude">Longitude:</label>
      <input type="text" id="longitude" name="longitude" placeholder="Type your address...">
      <button style= "color:white;background-color: #5A2E47" @click="emitData">Submit</button>

      <!-- latitude -->
      <label for="latitude">Latitude:</label>
      <input type="text" id="latitude" name="latitude" placeholder="Type your address...">
      <button style= "color:white;background-color: #5A2E47" @click="emitData">Submit</button>

  </template>

<script>
// import { ref } from 'vue'
// const message = ref('')

export default {
    name: 'AddressInput',
    methods: {
        emitData() {
        this.$emit('data-updated', document.getElementById("address").value);
        this.$emit('long-updated', document.getElementById("longitude").value);
        this.$emit('lat-updated', document.getElementById("latitude").value);
        }
    }
}

</script>



