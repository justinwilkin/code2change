<template>
  <div>
    <Header />
    <nuxt />
    <Footer />
  </div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'

export default {
  components: { Header, Footer },

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
