<template>
  <section class="container" :class="{'menu-open': menuOpen}">
    <!-- 根据 menuOpen 的值来判断是否使用 menu-open 样式 -->
    <!-- 左边的容器  -->
    <section class="menu">
      <menus></menus>
    </section>
    <!-- 这个是当页面收缩时覆盖在上面的模糊层，点击后复原-->
    <!-- 他可以直接调用 vuex actions.js 里面的 updateMenu 方法 -->
    <div class="content-overlay" @click="$store.dispatch('updateMenu')"></div>
    <!-- 右边的容器 -->
    <section class="content-container">
      <todo></todo>
    </section>
  </section>
</template>

<script>
import menus from './menus'
import todo from './todo'
export default {
  components: {
    menus,
    todo
  },
  computed: {
    menuOpen () {
      return this.$store.state.menuOpen
    }
  }
}
</script>

<style lang="less">
@import '../common/style/layouts.less';
</style>
