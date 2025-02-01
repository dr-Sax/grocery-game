<template>
    <!--
    <p>Message is: {{ message }}</p>
      <input v-model="message" placeholder="edit me" />
    -->
      <button @click="emitData">Send Data</button>
  </template>

<script>
// import { ref } from 'vue'
// const message = ref('')

export default {
       methods: {
         emitData() {
           this.$emit('data-updated', 'Data from Child');
         }
       }
     }

</script>