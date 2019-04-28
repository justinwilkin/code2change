<template>
  <section class="page" id="page-index">
    <EventDetails class="bodyContent" :event="event" />
  </section>
</template>

<script>
import { mapGetters } from 'vuex'
import LeafletMapsDisplay from '@/components/LeafletMapsDisplay'
import { eventsModule, REQUEST, EVENT_BY_ID } from '../../store/events/methods'
import EventDetails from '../../components/EventDetails'
export default {
  layout: 'withFooter',
  components: {
    LeafletMapsDisplay,
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
