<template>
  <div class="list-todos">
    <a
      @click="gotoList(list.id)"
      class="list-todo activeListClass list"
      :class="{'active' : list.id === todoId}"
      v-for="list in lists"
      :key="list.id">

      <span class="icon-lock" v-if="list.locked"></span>
      <span class="count-list" v-if="list.count > 0">{{ list.count }}</span>
      {{ list.content }}
    </a>

    <a class="link-list-new" @click="addNewTodoList">
      <span class="icon-plus"></span>
      新增
    </a>
  </div>
</template>

<script>
import {getTodoList, addTodoList} from '../api/api'
export default {
  data () {
    return {
      lists: [],
      todoId: ''
    }
  },
  created () {
    getTodoList({}).then(res => {
      const TODOs = res.data.lists
      this.lists = TODOs
      this.todoId = TODOs[0].id
    })
  },
  methods: {
    gotoList (id) {
      this.todoId = id
    },
    addNewTodoList () {
      addTodoList({
        content: 'newList'
      }).then(data => {
        getTodoList({}).then(res => {
          const ToDos = res.data.lists
          this.lists = ToDos
          this.todoId = ToDos[ToDos.length - 1].id
        })
      })
    }
  },
  watch: {
    'todoId' (id) {
      // 监听到用户点击 todoId 的变化再跳转路由
      this.$router.push({
        name: 'todo',
        params: {
          id: id
        }
      })
    }
  }
}
</script>

<style lang="less">
  @import "../common/style/menu.less";
</style>
