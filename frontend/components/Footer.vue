<template>
    <footer>
        <ul>
          <li><router-link to="/">Events</router-link></li>
          <li @click="simulateNotification()">Saved</li>
        </ul>
    </footer>
</template>

<script>
import Swal from 'sweetalert2'

export default {
  methods: {
    simulateNotification() {
      Swal.fire({
        position: 'top-end',
        title: '<b>Neerby Event</b>',
        html:
          '<b>Arts and Culture</b> <br /> Experience local art and culture. <br/>' +
          'George Street - happening now',
        showConfirmButton: false,
        showCancelButton: false,
        showCloseButton: true,
        timer: 6500
      })
    }
  }
}
</script>
<style lang="scss" scoped>
@import '~assets/variables';
footer {
  height: 60px;
  background: $color-background;
  font-weight: $fontweight-bold;
  font-size: $font-regular;
  color: $color-white;
  border-top: 1px solid;
  border-color: $color-darkgray;
  ul {
    padding: 0;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    list-style: none;
    height: 100%;
  }
}
</style>
