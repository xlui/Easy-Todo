<template>
  <div class="page lists-show">
    <nav>
      <div class="form list-edit-form" v-show="isUpdate">
        <input type="text" v-model="todo.content" @keyup.enter="updateContent" :disabled="todo.locked">
        <div class="nav-group right">
          <a class="nav-item" @click="isUpdate = false">
            <span class="icon-close"></span>
          </a>
        </div>
      </div>

      <!-- 在菜单图标下添加 updateMenu 事件，可以直接调用 vuex actions.js 里面的 updateMenu 方法 -->
      <div class="nav-group" @click="$store.dispatch('updateMenu')" v-show="!isUpdate">
        <a class="nav-item">
          <span class="icon-list-unordered">
          </span>
        </a>
      </div>

      <h1 class="title-page" v-show="!isUpdate" @click="isUpdate = true">
        <span class="title-wrapper">{{ todo.content }}</span>
        <span class="count-list">{{ todo.count || 0 }}</span>
      </h1>

      <div class="nav-group right" v-show="!isUpdate">
        <div class="options-web">
          <a class="nav-item" @click="onLock">
            <span class="icon-lock" v-if="todo.locked"></span>
            <span class="icon-unlock" v-else></span>
          </a>
          <a class="nav-item" @click="onDelete">
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
        <item
          :item="item"
          :locked="todo.locked"
          :init="init">
        </item>
      </div>
    </div>
  </div>
</template>

<script>
import item from './item'
import {getItems, addItem, updateTodoList} from '../api/api'
export default {
  data () {
    return {
      todo: {},
      items: [],
      text: '',
      isUpdate: false
    }
  },
  methods: {
    init () {
      const ID = this.$route.params.id
      getItems(ID).then(res => {
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
      const ID = this.$route.params.id
      addItem(ID, {
        content: this.text
      }).then(res => {
        this.text = ''
        this.init()
      })
    },
    onLock () {
      this.todo.locked = !this.todo.locked
      this.updateTodo()
    },
    onDelete () {
      this.todo.isDelete = true
      this.updateTodo()
    },
    updateContent () {
      this.updateTodo()
      this.isUpdate = false
    },
    updateTodo () {
      let _this = this
      updateTodoList(this.$route.params.id, this.todo).then(data => {
        _this.$store.dispatch('getTodo')
      })
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
