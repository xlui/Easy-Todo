import axios from 'axios'

const baseUrl = 'http://127.0.0.1:5000'

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
  return axios.get(baseUrl + '/todo-list', {
    params: params
  })
}

export const addTodoList = params => {
  return axios.post(baseUrl + '/todo-list', params).then(res => res.data)
}
