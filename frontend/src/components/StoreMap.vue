<!-- frontend/src/components/StoreMap.vue -->
<template>
    <p>{{ megan_latitude }}</p>
    <div class="map-container">
      <GoogleMap
        :api-key="apiKey"
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
    props: ['megan_latitude', 'megan_longitude'],

    setup() {
      const apiKey = import.meta.env.VITE_GOOGLE_MAPS_API_KEY
      const center = ref({ lat: megan_latitude, lng: megan_longitude })
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
      }
      
      const selectStore = (marker) => {
        console.log('Selected store:', marker)
      }
      
      return {
        apiKey,
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