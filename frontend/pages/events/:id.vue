<template>
  <div class="page" id="page-index">
    {{ event }}
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import GoogleMaps from '@/components/GoogleMaps.vue'
import { eventsModule, REQUEST, EVENT_BY_ID } from '../../store/events/methods'

export default {
  layout: 'withFooter',
  components: {
    GoogleMaps
  },
  computed: {
    ...mapGetters({
      getEventById: eventsModule(EVENT_BY_ID)
    }),
  },
  data() {
    return {
      event: null
    }
  },
  async created() {
    await this.$store.dispatch(eventsModule(REQUEST))
    const id = Number(this.$route.params.id)
    this.event = this.getEventById(id)
  },
}
</script>

<style lang="scss" scoped>
@import '~assets/variables';
</style>
