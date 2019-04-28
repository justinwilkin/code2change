<template>
  <form>
    <label class="required">Event Name</label>
    <input type="text" v-model="name"/>
    <label class="required">Event Description</label>
    <textarea v-model="description"/>
    <label class="required">Location</label>
    <input type="text" v-model="location"/>
    <label class="required">Date</label>
    <input type="text" v-model="date"/>
    <label class="required">Event Type</label>
    <select v-model="type">
      <option disabled value="">Please select an event type</option>
      <option value="Music">Music</option>
      <option value="Free">Free</option>
      <option value="LAN Party">LAN Party</option>
      <option value="Food Markets">Food Markets</option>
      <option value="Shopping">Shopping</option>
      <option value="PSA">Public Service Announcement</option>
      <option value="Sports">Sports</option>
    </select>
    <label>Info URL (optional)</label>
    <input type="text" v-model="url_info"/>
    <button @click="btnClick">Next</button>
  </form>
</template>


<script>
import { eventModule, NAME, DESCRIPTION, LOCATION, DATE, TYPE, URL_INFO, GEO_FENCE, EVENT } from '../store/event/methods'

export default {
  props: {
    btnClick: Function
  },
  computed: {
    name: {
      get() {
        return this.$store.getters[eventModule(NAME)]
      },
      set(value) {
        this.$store.commit(eventModule(NAME), value)
      }
    },
    description: {
      get() {
        return this.$store.getters[eventModule(DESCRIPTION)]
      },
      set(value) {
        this.$store.commit(eventModule(DESCRIPTION), value)
      }
    },
    location: {
      get() {
        return this.$store.getters[eventModule(LOCATION)]
      },
      set(value) {
        this.$store.commit(eventModule(LOCATION), value)
      }
    },
    date: {
      get() {
        return this.$store.getters[eventModule(DATE)]
      },
      set(value) {
        this.$store.commit(eventModule(DATE), value)
      }
    },
    type: {
      get() {
        return this.$store.getters[eventModule(TYPE)]
      },
      set(value) {
        this.$store.commit(eventModule(TYPE), value)
      }
    },
    url_info: {
      get() {
        return this.$store.getters[eventModule(URL_INFO)]
      },
      set(value) {
        this.$store.commit(eventModule(URL_INFO), value)
      }
    },
    geo_fence: {
      get() {
        return this.$store.getters[eventModule(GEO_FENCE)]
      },
      set(value) {
        this.$store.commit(eventModule(GEO_FENCE), value)
      }
    },
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

.required {
  &:after {
    content: '*';
     margin-left: 5px;
    color: $color-red;
  }
}

form {
  margin-bottom: 20px;
}
</style>
