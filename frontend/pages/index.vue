<template>
  <div id="page-index">
    <Header />
    <Footer />
  </div>
</template>

<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

export default {
  layout: 'default',
  components: {
    Header
  }
}
</script>

<style lang="scss" scoped>
@import '~assets/variables';
</style>
