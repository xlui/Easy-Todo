import axios from 'axios'

// const base = 'http://127.0.0.1:5000'
const base = 'https://todo.dx.style/api'
const listBaseUrl = base + '/todo-list'
const itemBaseUrl = listBaseUrl + '/'

axios.interceptors.request.use(config => {
  return config
}, error => {
  alert('请求超时！')
  return Promise.resolve(error)
})

axios.interceptors.response.use(data => {
  return data
}, error => {
  alert('status: ' + error.response.status + '\nmessage: ' + error.response.data.message)
  return Promise.resolve(error)
})

export const getTodoList = params => {
  return axios.get(listBaseUrl, {
    params: params
  })
}

export const addTodoList = params => {
  return axios.post(listBaseUrl, params).then(res => res.data)
}

export const updateTodoList = (listId, params) => {
  return axios.put(itemBaseUrl + listId, params)
}

export const getItems = listId => {
  return axios.get(itemBaseUrl + listId + '/todo-item', {})
}

export const addItem = (listId, params) => {
  return axios.post(itemBaseUrl + listId + '/todo-item', params).then(res => res.data)
}

export const updateItem = (listId, itemId, params) => {
  return axios.put(itemBaseUrl + listId + '/todo-item/' + itemId, params).then(res => res.data)
}

export const init = params => {
  return axios.get(base + '/init', params).then(res => res.data)
}
