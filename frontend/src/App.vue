<!-- frontend/src/App.vue -->
<template>
    <div id="app">
      <StoreMap 
        @store-added="handleStoreAdded"
        @store-selected="handleStoreSelected"
      />
    </div>
  </template>
  
  <script>
  import StoreMap from './components/StoreMap.vue'
  
  export default {
    name: 'App',
    components: {
      StoreMap
    },
    methods: {
      handleStoreAdded(position) {
        console.log('New store added at:', position)
      },
      handleStoreSelected(marker) {
        console.log('Store selected:', marker)
      }
    }
  }
  </script>

  