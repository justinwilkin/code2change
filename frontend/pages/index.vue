<template>
  <div class="page" id="page-index">
    <GoogleMaps :width="'100%'" :height="'100%'" />
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import GoogleMaps from '@/components/GoogleMaps.vue'
import { eventsModule, REQUEST, EVENTS, EVENT_BY_ID } from '../store/events/methods'

export default {
  layout: 'withFooter',
  components: {
    GoogleMaps
  },
  computed: {
    ...mapGetters({
      getEventById: eventsModule(EVENT_BY_ID)
    })
  },
  async created() {
    await this.$store.dispatch(eventsModule(REQUEST))
  },
}
</script>

<style lang="scss" scoped>
@import '~assets/variables';
</style>
