<template>
    <footer>
        <ul>
          <li><router-link to="/">Events</router-link></li>
          <li><router-link to="/">Saved</router-link></li>
        </ul>
    </footer>
</template>

<script>
export default {
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
