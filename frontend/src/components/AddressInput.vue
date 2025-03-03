<template>
    <!-- input address in HTML text box input-->
      <label for="address">Address:</label>
      <input type="text" id="address" name="address" placeholder="Type your address..." @keyup.enter="emitData">
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
      <p class="backend-address">{{ backendAddress }}</p>
  </template>

<script>
import axios from 'axios';

export default {
    name: 'AddressInput',
    emits: ['lat_lng','coordinates-updated'],

    mounted(){
      this.fetchAddress();
    },
    data(){
      return{
        backendAddress: ''
      }
    },

    methods: {
      async fetchAddress(){
        this.loading = true;
        this.error = null;
        try {
          const response = await axios.get('api/address');
          this.backendAddress = response.data.address;
        }
        catch (err){
          this.error = 'failed to fetch backend address';
          console.error(err)
        }
        finally{
          this.loading = false;
        }
      },

      async updateAddress(address){
        this.loading = true;
        this.error = null;
        this.success = false;
        this.address = address;

        try{
          const response = await axios.post('api/address', {address: this.address});
          if (response.data.success){
            this.backendAddress = response.data.address;
            console.log(this.backendAddress["lat"]);
            this.$emit('lat_lng', {
              latitude: this.backendAddress["lat"],
              longitude: this.backendAddress["lng"],
        })
          }
        }
        catch (err){

        }
      },

      emitData() {
        // existing update map code
        this.$emit('coordinates-updated', {
          // latitude: document.getElementById("latitude").value,
          // longitude: document.getElementById("longitude").value,
          address: document.getElementById("address").value
        });

        // testing backend update address
        this.updateAddress(document.getElementById("address").value)
      }
    }
}
</script>



