<!-- frontend/src/App.vue -->
<template>
    <div id="app">
      <AddressInput @data-updated="handleDataUpdate" 
        @lat-updated="handleDataUpdate"
        @long-updated="handleDataUpdate"
      />
      <StoreMap 
        @store-added="handleStoreAdded"
        @store-selected="handleStoreSelected"
        :megan_latitude="newLatitude"
        :megan_longitude="newLongitude"
      />
    </div>


  </template>
  
  <script>

  import AddressInput from './components/AddressInput.vue';
  import StoreMap from './components/StoreMap.vue'


  
  export default {
    name: 'App',
    components: {
      StoreMap,
      AddressInput
    },
    megan_latitude() {
      return {
        newLatitude: 41
      };
    },
    megan_longitude() {
      return {
        newLongitude: 81
      };
    },
    methods: {
      handleStoreAdded(position) {
        console.log('New store added at:', position);
      },
      handleStoreSelected(marker) {
        console.log('Store selected:', marker);
      },
      handleDataUpdate(data) {
        const lines = data.split("\n");
       this.newLatitude = data;
       this.newLongitude = data;
       console.log(data);
       console.log(this.newLatitude);
       console.log(this.newLongitude);
      }
    }
  }
  </script>

  