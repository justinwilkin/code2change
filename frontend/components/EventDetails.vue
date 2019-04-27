<template>
  <section id="event-details">
    <div v-if="!!event">
      <label>Event Name</label>
      <p>{{ event.name }}</p>
      <label>When</label>
      <p>{{ moment(event.date).format('MMMM Do YYYY, h:mm a') }}</p>
      <label>Location</label>
      <p>{{ event.location }}</p>
      <label>Description</label>
      <p>{{ event.description }}</p>
      <label>Event Type</label>
      <p>{{ event.event_type }}</p>
      <label>Info URL</label>
      <p v-if="event.url_info">{{ event.url_info }}</p>
      <p v-else>none</p>
    </div>
  </section>
</template>

<script>
import moment from 'moment'

export default {
  props: {
    event: Object
  },
  methods: {
    moment: moment
  }
}
</script>

<style lang="scss" scoped>
@import '~assets/variables';
</style>
