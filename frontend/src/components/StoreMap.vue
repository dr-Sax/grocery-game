<!-- frontend/src/components/StoreMap.vue -->
<template>
    <div class="map-container">
      <GoogleMap
        :api-key="apiKey"
        class="map"
        :center="center"
        :zoom="10"
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
    emits: ['list_of_names'],
    components: { GoogleMap, Marker },
    props: ['megan_latitude', 'megan_longitude', 'list_of_stores'],

    setup(props, {emit}) {
      const apiKey = import.meta.env.VITE_GOOGLE_MAPS_API_KEY
      const center = computed(
        () => (
          { 
            lat: Number(props.megan_latitude), 
            lng: Number(props.megan_longitude),
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
      })

      watch(() => props.list_of_stores, (newStores) => {
        let store_list = props.list_of_stores.results;
        let name_list = [];

        for (let i = 0; i < store_list.length; i++){
          let lat= store_list[i].geometry.location.lat;
          let lng= store_list[i].geometry.location.lng;
          markers.value.push(
            {
              "id": i,
              "position": {"lat": lat, "lng": lng}
            })
          
          // formatting for checklist items:
          let adr = props.list_of_stores.results[i].formatted_address
          let str_name = props.list_of_stores.results[i].name
          let idx = i;
          let str_fmt = {"id": idx, "name": str_name, "address": adr};
          name_list.push(str_fmt);
        // end of loop  
        }
        
        emit('list_of_names', name_list);
      })
      

      //this can be used for icon color changing and selection
      const selectStore = (marker) => {
        console.log('Selected store:', marker)
      }
      
      return {
        apiKey,
        center,
        markers,
        //addMarker,
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
    display: flex;
  }
  </style>