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

<style scoped>
.map-container {
  width: 100%;
  height: 500px;
}
.map {
  width: 100%;
  height: 100%;
}
</style>