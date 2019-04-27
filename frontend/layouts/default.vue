<template>
  <div>
    <Header />
    <nuxt />
  </div>
</template>

<script>
import Header from '../components/Header'

export default {
  components: { Header },

  mounted() {
    if (process.browser) {
      screen.orientation.lock('portrait')
    }
  }
}
</script>

<style lang="scss">
@import '~/assets/global.scss';
</style>
