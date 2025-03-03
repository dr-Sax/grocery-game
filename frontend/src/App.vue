<!-- frontend/src/App.vue -->
<template>
    <div id="app">    <!-- root node, all other divs must be nested inside-->
      <div id="addressInput">
        <AddressInput 
          @lat_lng="handleCoordinatesUpdate" 
          
        />
      </div>
      <div id="viewMap">
        <StoreMap 
          @store-added="handleStoreAdded"
          @store-selected="handleStoreSelected"
          :megan_latitude="newLatitude"
          :megan_longitude="newLongitude"
        />
      </div>
    </div>
  </template>


  <script>
  //import children from component folder
  import AddressInput from './components/AddressInput.vue';
  import StoreMap from './components/StoreMap.vue'

  export default {
    name: 'App',
    components: {
      StoreMap,
      AddressInput
    },
    data(){
      return{
        newLatitude: 39.96,
        newLongitude: -82.99,
      }
    },
    methods: {
      handleStoreAdded(position) {
        console.log('New store added at:', position);
      },
      handleStoreSelected(marker) {
        console.log('Store selected:', marker);
      },
      handleCoordinatesUpdate(data) {
        console.log("hello");
        this.newLatitude = Number(data.latitude);
        this.newLongitude = Number(data.longitude);
      }
    }
  }
  </script>

  