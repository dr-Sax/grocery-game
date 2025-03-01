<template>
    <!-- input address in HTML text box input-->
      <label for="address">Address:</label>
      <input type="text" id="address" name="address" placeholder="Type your address...">
      <br>
    <!-- longitude -->
      <label for="longitude">Longitude:</label>
      <input type="text" id="longitude" name="longitude" placeholder="Type your longitude...">
      <br>
    <!-- latitude -->
      <label for="latitude">Latitude:</label>
      <input type="text" id="latitude" name="latitude" placeholder="Type your latitude...">
      <br>
      <button style= "color:white;background-color: #5A2E47" @click="emitData">Submit</button>
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



