<template>
  <section class="page bodyContent" id="page-index">
    <EventDetails :event="event" />
  </section>
</template>

<script>
import { mapGetters } from 'vuex'
// import GoogleMaps from '@/components/GoogleMaps.vue'
import LeafletMaps from '@/components/LeafletMaps.vue'
import { eventsModule, REQUEST, EVENT_BY_ID } from '../../store/events/methods'
import EventDetails from '../../components/EventDetails'
export default {
  layout: 'withFooter',
  components: {
    // GoogleMaps,
    LeafletMaps,
    EventDetails
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
    this.event = this.getEventById(id);
  },
}
</script>

<style lang="scss" scoped>
@import '~assets/variables';
</style>
