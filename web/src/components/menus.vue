<template>
  <div class="list-todos">
    <a
      @click="gotoList(list.id)"
      class="list-todo activeListClass list"
      :class="{'active' : list.id === todoId}"
      v-for="list in todoList"
      :key="list.id">

      <span class="icon-lock" v-if="list.locked"></span>
      <span class="count-list" v-if="list.count > 0">{{ list.count }}</span>
      {{ list.content }}
    </a>

    <a class="link-list-new" @click="addNewTodoList">
      <span class="icon-plus"></span>
      新增
    </a>

    <a class="link-list-new" @click="init">
      <span class="icon-sync"></span>
      重新初始化
    </a>
  </div>
</template>

<script>
import {addTodoList, init} from '../api/api'
export default {
  data () {
    return {
      lists: [],
      todoId: ''
    }
  },
  methods: {
    gotoList (id) {
      this.todoId = id
    },
    addNewTodoList () {
      addTodoList({
        content: 'newList'
      }).then(data => {
        this.$store.dispatch('getTodo').then(() => {
          this.$nextTick(() => {
            setTimeout(() => {
              this.gotoList(this.todoList[this.todoList.length - 1].id)
            }, 100)
          })
        })
      })
    },
    init () {
      init({})
      location.reload()
    }
  },
  computed: {
    todoList () {
      return this.$store.getters.getTodoList
    }
  },
  created () {
    this.$store.dispatch('getTodo').then(() => {
      this.$nextTick(() => {
        this.gotoList(this.todoList[0].id)
      })
    })
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
