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
                <input type="checkbox" :value="item.id" v-model="selectedItems">
                  <strong>{{ item.name }}</strong>
                  <br>
                  <em>{{ item.address }}</em>
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
            />
          </div>
        </div>
    </div>
  </template>


  <script>
  //import children from component folder
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