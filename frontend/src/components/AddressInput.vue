<template>
    <!-- input address in HTML text box input-->
      <label for="address">Address:</label>
      <input type="text" id="address" name="address" placeholder="Type your address..." @keyup.enter="emitData">
      <br>
      <button style= "color:white;background-color: #5A2E47" @click="emitData">Submit</button>
      <p class="backend-address">{{ backendAddress }}</p>
  </template>

<script>
import axios from 'axios';

export default {
    name: 'AddressInput',
    emits: ['lat_lng','coordinates-updated','store_list'],

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
            this.storeList = response.data.stores;
            console.log(this.backendAddress["lat"]);
            this.$emit('lat_lng', {
              latitude: this.backendAddress["lat"],
              longitude: this.backendAddress["lng"],
            })
            this.$emit('store_list', {
              stores: this.storeList,
            })
          }
        }
        catch (err){

        }
      },

      emitData() {
        // existing update map code
        this.$emit('coordinates-updated', {
          address: document.getElementById("address").value
        });
        // testing backend update address
        this.updateAddress(document.getElementById("address").value)
      }
    }
}
</script>



