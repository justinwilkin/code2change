<template>
    <footer>
        <ul>
          <li>test1</li>
          <li>test2</li>
          <li>test3</li>
        </ul>
    </footer>
</template>

<script>
export default {
}
</script>
<style lang="scss" scoped>
@import '~assets/variables';
header {
  height: 58px;
  display: flex;
  align-items: center;
  background: $color-background;
  font-weight: $fontweight-bold;
  font-size: $font-heading;
  .logo {
    color: $color-white;
    text-align: center;
    width: 100%;
    span {
      color: $color-primary;
    }
  }
}
</style>
