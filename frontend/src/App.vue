<template>
    <div class="app">
      <header>
        <h1>Grocery Price Optimizer</h1>
      </header>
      
      <store-locator @location-set="updateLocation" />
      
      <grocery-list 
        :stores="nearbyStores"
        @list-update="updateGroceryList" 
      />
      
      <price-comparison 
        v-if="optimizedLists"
        :lists="optimizedLists" 
      />
    </div>
  </template>
  
  <script>
  import { ref } from 'vue'
  import axios from 'axios'
//   import StoreLocator from './components/StoreLocator.vue'
//   import GroceryList from './components/GroceryList.vue'
//   import PriceComparison from './components/PriceComparison.vue'
  
  export default {
    components: {
      StoreLocator,
      GroceryList,
      PriceComparison
    },
    setup() {
      const nearbyStores = ref([])
      const optimizedLists = ref(null)
      
      const updateLocation = async (location) => {
        try {
          const response = await axios.get('/api/stores', {
            params: {
              lat: location.lat,
              lng: location.lng
            }
          })
          nearbyStores.value = response.data
        } catch (error) {
          console.error('Error fetching stores:', error)
        }
      }
      
      const updateGroceryList = async (items) => {
        try {
          const response = await axios.post('/api/search', {
            items,
            stores: nearbyStores.value.map(store => store.id)
          })
          optimizedLists.value = response.data
        } catch (error) {
          console.error('Error optimizing list:', error)
        }
      }
      
      return {
        nearbyStores,
        optimizedLists,
        updateLocation,
        updateGroceryList
      }
    }
  }
  </script>