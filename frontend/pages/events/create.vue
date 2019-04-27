<template>
  <section class="page" id="page-event-create">
    <div class="content">
      <h1>Create an Event</h1>
      <EventDetailsForm v-if="step === 1" :btn-click="onProgress" />
      <div v-if="step === 2">
        <p>Select 4 points to create a zone for people to receive information in</p>
        <LeafletMaps class="map"/>
        <div class="buttonWrapper">
          <button @click="onProgress">Review</button>
        </div>
      </div>
      <div v-if="step === 3">
        <p>Check if these details are correct. Please correct them if they aren’t!</p>
        <div class="bodyContent">
          <EventDetails :event="event" />
          <button @click="onSubmit">Submit</button>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { mapGetters } from 'vuex'
import { eventModule, NAME, DESCRIPTION, LOCATION, DATE, TYPE, URL_INFO, GEO_FENCE, EVENT, SUBMIT } from '../../store/event/methods'
import EventDetails from '../../components/EventDetails'
import EventDetailsForm from '../../components/EventDetailsForm'
import LeafletMaps from '@/components/LeafletMaps.vue'

export default {
  layout: 'withFooter',
  components: {
    EventDetails,
    EventDetailsForm,
    LeafletMaps
  },
  data() {
    return {
      step: 1
    }
  },
  methods: {
    onProgress() {
      this.step = this.step + 1
    },
    async onSubmit() {
      await this.$store.dispatch(eventModule(SUBMIT))
      this.$router.push({ path: '/' })
    }
  },
  computed: {
    event: {
      get() {
        return this.$store.getters[eventModule(EVENT)]
      }
    }
  }
}
</script>

<style lang="scss" scoped>
@import '~assets/variables';

.map{
  height: 62vh;
}

.content {
  h1, p, form, .buttonWrapper {
    padding: 0 20px;
  }
}

.buttonWrapper {
  display: flex;
  align-items: center;
  z-index: 1000;
  position: absolute;
  width: 100%;
  bottom: 60px;
  height: 100px;
  background: linear-gradient(to bottom, rgba(0,0,0,0) 0%, #000 100%);
}
</style>
