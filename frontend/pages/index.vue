<template>
  <div class="page" id="page-index">
    <LeafletMaps/>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import LeafletMaps from '@/components/LeafletMaps.vue'
import { eventsModule, REQUEST, EVENTS, EVENT_BY_ID } from '../store/events/methods'

export default {
  layout: 'withFooter',
  components: {
    LeafletMaps
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
