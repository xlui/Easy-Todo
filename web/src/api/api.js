import axios from 'axios'

const listBaseUrl = 'http://127.0.0.1:5000/todo-list'
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

export const getTodo = params => {
  return axios.get(itemBaseUrl + params + '/todo-item', {})
}

export const addItem = params => {
  return axios.post(itemBaseUrl + params + '/todo-item', params).then(res => res.data)
}
