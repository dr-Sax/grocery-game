<template>
    <!-- input address in HTML text box input-->
      <label for="address">Address:</label>
      <input type="text" id="address" name="address" placeholder="Type your address..." @keyup.enter="submitAddress">
      <br>
      <button style= "color:white;background-color: #5A2E47" @click="submitAddress">Submit</button>
      <p class="backend-address">{{ backendAddress }}</p>
  </template>

<script>
import axios from 'axios';

export default {
    name: 'AddressInput',
    emits: ['lat_lng_add', 'store_list_add'],

    mounted(){
      this.fetchAddress();
    },

    data() {
      return {
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
            this.$emit('lat_lng_add', {
              latitude: this.backendAddress["lat"],
              longitude: this.backendAddress["lng"],
            })
            this.$emit('store_list_add', {
              stores: this.storeList,
            })
          }
        }
        catch (err){

        }
      },

      submitAddress() {
        // testing backend update address
        this.updateAddress(document.getElementById("address").value)
      }

    }
}
</script>



