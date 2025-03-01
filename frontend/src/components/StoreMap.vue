<!-- frontend/src/components/StoreMap.vue -->
<template>
    
    <div class="map-container">
      <GoogleMap
        :api-key="apiKey"
        class="map"
        :center="center"
        :zoom="10"
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
  import { defineComponent, ref, watch, computed } from 'vue'
  import { GoogleMap, Marker } from 'vue3-google-map'
  
  export default defineComponent({
    name: 'StoreMap',
    components: { GoogleMap, Marker },
    props: ['megan_latitude', 'megan_longitude'],

    setup(props) {
      const apiKey = import.meta.env.VITE_GOOGLE_MAPS_API_KEY
      const center = computed(
        () => (
          { 
            lat: Number(props.megan_latitude), 
            lng: Number(props.megan_longitude)
          }
        )
      )
      const markers = ref([])
      // Make center reactive to prop changes
      watch(() => props.megan_latitude, (newLat) => {
      center.value.lat = newLat
      })
      watch(() => props.megan_longitude, (newLng) => {
      console.log(center.value);
      center.value.lng = newLng;
      console.log(center.value);
      })
      
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
    
    }
  )

  
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