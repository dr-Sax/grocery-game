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

      <!-- latitude -->
      <label for="latitude">Latitude:</label>
      <input type="text" id="latitude" name="latitude" placeholder="Type your address...">

  </template>

<script>

export default {
    name: 'AddressInput',
    emits: ['coordinates-updated'],
    methods: {
      emitData() {
        this.$emit('coordinates-updated', {
          latitude: document.getElementById("latitude").value,
          longitude: document.getElementById("longitude").value,
          address: document.getElementById("address").value,
        });
      }
    }
}

</script>



