<template>
    <GmapMap
  :center="{lat:15, lng:10}"
  :zoom="7"
  :options="{styles: styles}"
  map-type-id="roadmap"
  style="width: 500px; height: 300px"
  
>
  <GmapMarker
    :key="index"
    v-for="(m, index) in markers"
    :position="m.position"
    :clickable="true"
    :draggable="true"
    @click="center=m.position"
  />
</GmapMap>
</template>

<script>
import json from '../assets/maps-style.json'

export default {
  data() {
    return {
      styles: json
    }
  }
}
</script>

<style>

</style>
