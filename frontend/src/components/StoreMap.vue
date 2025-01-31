<!-- frontend/src/components/StoreMap.vue -->
<template>
    <div class="map-container">
      <GoogleMap
        :api-key="import.meta.env.VITE_GOOGLE_MAPS_API_KEY"
        class="map"
        :center="center"
        :zoom="12"
        @click="addMarker"
      >
        <Marker
          v-for="marker in markers"
          :key="marker.id"
          :options="{ position: marker.position }"
          @click="selectStore(marker)"
        />
      </GoogleMap>
    </div>
  </template>
  
  <script>
  import { defineComponent, ref } from 'vue'
  import { GoogleMap, Marker } from 'vue3-google-map'
  
  export default defineComponent({
    name: 'StoreMap',
    components: { GoogleMap, Marker },
    
    setup() {
      const center = ref({ lat: 40.7128, lng: -74.0060 }) // Default to NYC
      const markers = ref([])
      
      const addMarker = (event) => {
        const position = {
          lat: event.latLng.lat(),
          lng: event.latLng.lng()
        }
        markers.value.push({
          id: Date.now(),
          position
        })
        // Emit event for parent component
        emit('store-added', position)
      }
      
      const selectStore = (marker) => {
        // Emit event for parent component
        emit('store-selected', marker)
      }
      
      return {
        center,
        markers,
        addMarker,
        selectStore
      }
    }
  })
  </script>
  
  <style>
  .map-container {
    width: 100%;
    height: 500px;
    border: 1px solid #ccc;
    margin: 20px 0;
  }
  .map {
    width: 100%;
    height: 100%;
    display: block;
  }
  </style>