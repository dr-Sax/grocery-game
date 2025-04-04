<!-- frontend/src/components/StoreMap.vue -->
<template>
    <div class="map-container">
      <GoogleMap
        :api-key="apiKey"
        class="map"
        :center="center"
        :zoom="10"
      >
        <CustomMarker
          v-for="marker in markers"
          :key="marker.id"
          :options="{ position: marker.position, anchorPoint: 'BOTTOM_CENTER' }"
          @click="selectStore(marker)">
          <div style="text-align: center">
              <img src="../../assets/orange_mapmarker.png" width="50" height="50" style="margin-top: 8px" />
          </div>
        </CustomMarker>
      </GoogleMap>
    </div>
  </template>
  
  <script>
  import { defineComponent, ref, watch, computed } from 'vue'
  import { GoogleMap, CustomMarker } from 'vue3-google-map'
  
  export default defineComponent({
    name: 'StoreMap',
    emits: ['create_checklist_map'],
    components: { GoogleMap, CustomMarker },
    props: ['latitude_map', 'longitude_map', 'store_list_map', 'name_list_map'],

    setup(props, {emit}) {
      const apiKey = import.meta.env.VITE_GOOGLE_MAPS_API_KEY
      const center = computed(
        () => (
          { 
            lat: Number(props.latitude_map), 
            lng: Number(props.longitude_map),
          }
        )
      )
      const markers = ref([])

      // Make center reactive to prop changes
      watch(() => props.latitude_map, (newLat) => {
      center.value.lat = newLat
      })

      watch(() => props.longitude_map, (newLng) => {
      console.log(center.value);
      center.value.lng = newLng;
      })

      //watch for if a checkbox is selected and change marker if it is
      watch(
        () => props.name_list_map, (newLng) => {
          console.log('tester checkbox:', newLng);
        },
        { deep: true }
      )

      watch(() => props.store_list_map, (newStores) => {
        let _store_list = props.store_list_map.results;
        let store_list_fmt_map = [];

        for (let i = 0; i < _store_list.length; i++){
          //formatting for store markers on map
          let lat= _store_list[i].geometry.location.lat;
          let lng= _store_list[i].geometry.location.lng;
          markers.value.push(
            {
              "marker_id": i,
              "position": {"lat": lat, "lng": lng}
            })
          
          // formatting for checklist items:
          let adr = props.store_list_map.results[i].formatted_address
          let str_name = props.store_list_map.results[i].name
          let idx = i;
          let str_fmt = {"marker_id": idx, "name": str_name, "address": adr, "isChecked": false};
          store_list_fmt_map.push(str_fmt);
    
        // end of loop  
        }
        emit('create_checklist_map', store_list_fmt_map);
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