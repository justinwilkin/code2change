<template>
  <div class="page" id="page-index">
    <!-- <GoogleMaps :width="'100%'" :height="'100%'" /> -->
    <LeafletMaps />
  </div>
</template>

<script>
// import GoogleMaps from '@/components/GoogleMaps.vue'
import LeafletMaps from '@/components/LeafletMaps.vue'

export default {
  layout: 'withFooter',
  components: {
    // GoogleMaps
    LeafletMaps
  }
}
</script>

<style lang="scss" scoped>
@import '~assets/variables';
</style>
