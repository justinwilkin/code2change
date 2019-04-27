<template>
  <section class="page" id="page-event-create">
    <div class="bodyContent">
      <h1>Create an Event</h1>
      <EventDetailsForm v-if="step === 1" :btn-click="onProgress" />
      <div v-if="step === 2">
        <p>Select 4 points to create a zone for people to receive information in</p>
        <!-- Map goes here -->
        <button @click="onProgress">Review</button>
      </div>
      <div v-if="step === 3">
        <p>Check if these details are correct. Please correct them if they aren’t!</p>
        <EventDetails :event="event" />
        <button @click="onSubmit">Submit</button>
      </div>
    </div>
  </section>
</template>

<script>
import { mapGetters } from 'vuex'
import { eventModule, NAME, DESCRIPTION, LOCATION, DATE, TYPE, URL_INFO, GEO_FENCE, EVENT, SUBMIT } from '../../store/event/methods'
import EventDetails from '../../components/EventDetails'
import EventDetailsForm from '../../components/EventDetailsForm'

export default {
  layout: 'withFooter',
  components: {
    EventDetails,
    EventDetailsForm
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
</style>
