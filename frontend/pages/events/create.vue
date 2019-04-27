<template>
  <div class="page" id="page-index">
    <GoogleMaps :width="'100%'" :height="'100%'" />
  </div>
</template>

<script>
import GoogleMaps from '@/components/GoogleMaps.vue'

export default {
  layout: 'withFooter',
  components: {
    GoogleMaps
  }
}
</script>

<style lang="scss" scoped>
@import '~assets/variables';
</style>
