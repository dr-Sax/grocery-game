<!-- frontend/src/App.vue -->
<template>
    <div id="app">
      <AddressInput @data-updated="handleDataUpdate" />
      <StoreMap 
        @store-added="handleStoreAdded"
        @store-selected="handleStoreSelected"
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
    methods: {
      handleStoreAdded(position) {
        console.log('New store added at:', position);
      },
      handleStoreSelected(marker) {
        console.log('Store selected:', marker);
      },
      handleDataUpdate(data) {
       console.log(data); // 'Data from Child'
      }
    }
  }
  </script>

  