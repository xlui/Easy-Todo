<template>
  <div class="list-todos">
    <a
      @click="gotoList(item.id)"
      class="list-todo activeListClass list"
      :class="{'active' : item.id === todoId}"
      v-for="item in items"
      :key="item.id">

      <span class="icon-lock" v-if="item.locked"></span>
      <span class="count-list" v-if="item.count > 0">{{ item.count }}</span>
      {{ item.content }}
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
      items: [],
      todoId: ''
    }
  },
  created () {
    getTodoList({}).then(res => {
      const TODOs = res.data.lists
      this.items = TODOs
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
          this.todoId = ToDos[ToDos.length - 1].id
          this.items = ToDos
        })
      })
    }
  }
}
</script>

<style lang="less">
  @import "../common/style/menu.less";
</style>
