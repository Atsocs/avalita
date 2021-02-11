import {mockasync} from '../apimock/mockutils'
import {get, post} from './ajaxutils'

export default {
  login (username, password) {
    return post('/api/login', {username, password})
  },
  logout () {
    return post('/api/logout')
  },
  whoami () {
    return get('/api/whoami')
  },
  settings () {
    return get('/api/settings')
  },
  list_todos () {
    return get('/api/list_todos')
  },
  add_todo (new_task) {
    return post('/api/add_todo', {new_task})
  },
  list_items () {
    return get('/api/list_items')
  },
  vote (classId, col, value, studentUsername) {
    return post('/api/vote', {classId, col, value, studentUsername})
  }
}
