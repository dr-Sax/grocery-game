<!-- frontend/src/App.vue -->
<template>
    <div id = "app">    <!-- root node, all other divs must be nested inside-->
      <div id = "addressInput">
        <AddressInput 
          @lat_lng_add = "handleCoordinatesUpdate" 
          @store_list_add = "populateMap"
        />
      </div>
      <div class="flex-container">

        <!-- adding checklist items for stores: -->
        <div id="checklist-items" style="flex-grow: 1">
          <ul style="list-style-type: none">
            <li v-for="(item, index) in nameList" :key="index">
              <label>
                <input type="checkbox" :value="item.marker_id" v-model="item.isChecked" @change="checkboxSelected(item.marker_id, item.isChecked)">
                  <strong>{{ item.name }}</strong>
                  <br>
                  <em>{{ item.address }}</em>
                  <br>
                  {{ item.isChecked }}
              </label>
            </li>
          </ul>
        </div>


        <div id="viewMap" style="flex-grow: 3">
            <StoreMap
              :latitude_map = "latitude"
              :longitude_map = "longitude"
              :store_list_map = "store_list"
              :name_list_map = "nameList"
              @create_checklist_map = "createChecklist"
            />
          </div>
        </div>
    </div>
  </template>


  <script>
  //import children from component folder
  import { pushScopeId } from 'vue';
  import AddressInput from './components/AddressInput.vue';
  import StoreMap from './components/StoreMap.vue'

  export default {

    name: 'App',

    components: {
      StoreMap,
      AddressInput
    },

    data(){
      return {
        latitude: 39.96,
        longitude: -82.99,
        store_list: null,
        nameList: []
      }
    },

    methods: {

      handleCoordinatesUpdate(data) {
        this.latitude = Number(data.latitude);
        this.longitude = Number(data.longitude);
      },

      populateMap(data) {
        console.log("time to populate the map");
        this.store_list = data.stores;
      },

      createChecklist(data) {
        console.log("hello")
        this.nameList = data;
      },

      checkboxSelected(index, state){
        console.log("Checkbox state changed. Checked store:", index, "Checked:", state);
        console.log(this.nameList);
      }

    }
  }
  </script>

<style>
.flex-container {
  display: flex;
  margin: 10px;
}
</style>