<!-- frontend/src/App.vue -->
<template>
    <div id="app">    <!-- root node, all other divs must be nested inside-->
      <div id="addressInput">
        <AddressInput 
          @lat_lng="handleCoordinatesUpdate" 
          @store_list="populateMap"
        />
      </div>
      <div id="viewMap">
        <StoreMap 
          @store-selected="handleStoreSelected"
          :megan_latitude="newLatitude"
          :megan_longitude="newLongitude"
          :list_of_stores="newStores"
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
        newStores: null,
      }
    },
    methods: {
      handleStoreSelected(marker) {
        console.log('Store selected:', marker);
      },
      handleCoordinatesUpdate(data) {
        console.log("hello");
        this.newLatitude = Number(data.latitude);
        this.newLongitude = Number(data.longitude);
      },
      populateMap(data) {
        console.log("time to populate the map");
        this.newStores = data.stores;
      }
    }
  }
  </script>

  