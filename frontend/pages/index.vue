<template>
  <div id="page-index">
    <Header />
    <GoogleMaps :width="'100vw'" :height="'100vh'" />
  </div>
</template>

<script>
import Header from '@/components/Header.vue'
import GoogleMaps from '@/components/GoogleMaps.vue'

export default {
  layout: 'default',
  components: {
    Header,
    GoogleMaps
  }
}
</script>

<style lang="scss" scoped>
@import '~assets/variables';
</style>
