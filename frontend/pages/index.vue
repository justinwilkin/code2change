<template>
  <div id="page-index">
    <GoogleMaps :width="'100vw'" :height="'100vh'" />
  </div>
</template>

<script>
import GoogleMaps from '@/components/GoogleMaps.vue'

export default {
  layout: 'default',
  components: {
    GoogleMaps
  }
}
</script>

<style lang="scss" scoped>
@import '~assets/variables';
</style>
