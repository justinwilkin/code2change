<template>
  <div class="page" id="page-index">
    <LeafletMapsDisplay v-if="events.length > 0" :events="events" />
    <div class="button-wrapper">
     <button class="button circle plus" @click="btnClick" />
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import LeafletMapsDisplay from '@/components/LeafletMapsDisplay'
import { eventsModule, REQUEST, EVENTS, EVENT_BY_ID } from '../store/events/methods'

export default {
  layout: 'withFooter',
  components: {
    LeafletMapsDisplay
  },
  computed: {
    events: {
      get() {
        return this.$store.getters[eventsModule(EVENTS)]
      },
    }
  },
  methods: {
    btnClick() {
      this.$router.push({ path: '/events/create' })
    }
  },
  async mounted() {
    await this.$store.dispatch(eventsModule(REQUEST))
  },
}
</script>

<style lang="scss" scoped>
@import '~assets/variables';

button {
  &.circle {
    z-index: 1000;
    border-radius: 50%;
    position: fixed;
    height: 65px;
    width: 65px;
    right: 20px;
    bottom: 80px;
    box-shadow: 0px 3px 6px 0px rgba(0,0,0,0.16);
    &:after {
      content: '+';
      font-weight: $fontweight-bold;
      font-size: $font-reee;
      position: relative;
      top: -1px;
    }
  }
}
</style>
