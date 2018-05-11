import {getTodoList} from '../api/api'

export const getTodo = ({
  commit
}) => {
  return new Promise(resolve => {
    getTodoList().then(res => {
      commit('EDITTODE', res.data.lists)
      resolve()
    })
  })
}

export const updateMenu = ({
  commit
}) => {
  commit('MENUOPEN')
}
