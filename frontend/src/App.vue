<!-- frontend/src/App.vue -->
<template>
    <div id="app">    <!-- root node, all other divs must be nested inside-->
      <div id="addressInput">
        <AddressInput 
          @lat_lng="handleCoordinatesUpdate" 
          @store_list="populateMap"
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
              @store-selected="handleStoreSelected"
              :megan_latitude="newLatitude"
              :megan_longitude="newLongitude"
              :list_of_stores="newStores"
              @list_of_names="createNameList"
              :green_marker_stores="isChecked"
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
      return{
        newLatitude: 39.96,
        newLongitude: -82.99,
        newStores: null,
        nameList: [],
        isChecked: [],
      }
    },
    methods: {
      handleStoreSelected(marker) {
        console.log('Store selected:', marker);
      },
      handleCoordinatesUpdate(data) {
        this.newLatitude = Number(data.latitude);
        this.newLongitude = Number(data.longitude);
      },
      populateMap(data) {
        console.log("time to populate the map");
        this.newStores = data.stores;
      },
      createNameList(data) {
        console.log("hello")
        this.nameList = data;
      },
      checkboxSelected(index, state){
        console.log("Checkbox state changed. Checked store:", index, "Checked:", state);
        this.isChecked.push(index);
        console.log(this.isChecked);
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