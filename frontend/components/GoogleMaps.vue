<template>
    <GmapMap
  :center="{lat:15, lng:10}"
  :zoom="7"
  :options="{styles: styles}"
  map-type-id="roadmap"
  :style="style"

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
  props: {
    height: String,
    width: String
  },
  computed: {
    style () {
      return `width: ${this.width}; height: ${this.height};`
    }
  },
  data() {
    return {
      styles: json
    }
  }
}
</script>

<style>

</style>
