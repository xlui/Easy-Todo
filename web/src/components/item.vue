<template>
  <transition name="slide-fade">
    <!-- 最外层容器 -->
    <div class="list-item editingClass editing" :class="{checked: item.isDone}">
      <label class="checkbox">
        <input type="checkbox" v-model="item.isDone" name="checked" @change="onChange" :disabled="locked">
        <span class="checkbox-custom"></span>
      </label>
      <input type="text" v-model="item.content" placeholder="写点什么" :disabled="item.isDone || locked" @keyup.enter="onChange">
      <a class="delete-item" v-if="item.isDone && !locked" @click="item.isDelete=true;onChange()">
        <span class="icon-trash"></span>
      </a>
    </div>
  </transition>
</template>

<script>
import {updateItem} from '../api/api'
export default {
  // 子组件显式使用 props 选项声明它期待获得的数据
  // 这里声明它想要一个叫 item 的数据
  props: {
    item: {
      type: Object,
      default: () => {
        return {
          isDone: true,
          content: 'Hello World!'
        }
      }
    },
    'locked': {

    },
    'init': {

    }
  },
  methods: {
    onChange () {
      updateItem(this.$route.params.id, this.item.id, this.item).then(data => {
        this.init()
        this.$store.dispatch('getTodo')
      })
    }
  }
}
</script>

<style lang="less">
  @import "../common/style/list-items.less";
  .slide-fade-enter-active {
    transition: all .3s ease;
  }
  .slide-fade-leave-active {
    transition: all .3s cubic-bezier(1.0, 0.5, 0.8, 1.0);
  }
  .slide-fade-enter, .slide-fade-leave-active {
    transform: translateX(10px);
    opacity: 0;
  }
</style>
