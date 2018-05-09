<template>
  <section class="container">
    <!-- 左边的容器  -->
    <section class="menu">
      <menus></menus>
    </section>
    <!-- 右边的容器 -->
    <section class="content-container"></section>
  </section>
</template>

<script>
import menus from './menus'
export default {
  components: {
    menus
  }
}
</script>

<style lang="less">
@import '../common/style/layouts.less';
</style>
