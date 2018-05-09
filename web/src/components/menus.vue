<template>
  <div class="list-todos">
    <a class="list-todo activeListClass list" v-for="item in items" :key="item.id">
      <span class="icon-lock" v-if="item.locked"></span>
      <span class="count-list" v-if="item.count > 0">
        {{ item.count }}
      </span>
      {{ item.title }}
    </a>
    <a class="link-list-new">
      <span class="icon-plus"></span>
      新增
    </a>
  </div>
</template>

<script>
export default {
  data () {
    return {
      items: [
        {
          title: '星期一',
          count: 1,
          locked: true
        },
        {
          title: '星期二',
          count: 2,
          locked: true
        },
        {
          title: '星期三',
          count: 3,
          locked: false
        }
      ]
    }
  }
}
</script>

<style lang="less">
  @import "../common/style/menu.less";
</style>
