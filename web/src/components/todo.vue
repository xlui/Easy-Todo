<template>
  <div class="page lists-show">
    <nav>
      <div class="nav-group">
        <a class="nav-item">
          <span class="icon-list-unordered">
          </span>
        </a>
      </div>

      <h1 class="title-page">
        <span class="title-wrapper">{{ todo.content }}</span>
        <span class="count-list">{{ todo.count || 0 }}</span>
      </h1>

      <div class="nav-group right">
        <div class="options-web">
          <a class="nav-item">
            <span class="icon-lock" v-if="todo.locked"></span>
            <span class="icon-unlock" v-else></span>
          </a>
          <a class="nav-item">
            <span class="icon-trash"></span>
          </a>
        </div>
      </div>

      <div class="form todo-new input-symbol">
        <input type="text"
               v-model="text"
               placeholder="请输入"
               @keyup.enter="onAdd"
               :disabled="todo.locked">
        <span class="icon-add"></span>
      </div>
    </nav>

    <!-- 容器的下半部分-->
    <div class="content-scrollable list-items">
      <div v-for="item in items" :key="item.id">
        <!-- 传递 item 到子组件 -->
        <item :item="item"></item>
      </div>
    </div>
  </div>
</template>

<script>
import item from './item'
import {getTodo} from '../api/api'
export default {
  data () {
    return {
      todo: {
        content: '星期一',
        count: 12,
        locked: false
      },
      items: [],
      text: ''
    }
  },
  methods: {
    init () {
      const ID = this.$route.params.id
      getTodo(ID).then(res => {
        this.items = res.data.items
        this.todo = {
          id: res.data.id,
          content: res.data.content,
          count: res.data.count,
          isDelete: res.data.isDelete,
          locked: res.data.locked
        }
      })
    },
    onAdd () {
      this.items.push({
        checked: false, text: this.text, isDelete: false
      })
      this.text = ''
    }
  },
  components: {
    item
  },
  created () {
    // this.init()
  },
  watch: {
    // 监听 $route.params
    '$route.params.id' () {
      this.init()
    }
  }
}
</script>

<style lang="less">
  @import '../common/style/nav.less';
  @import "../common/style/form.less";
  @import "../common/style/todo.less";
</style>
