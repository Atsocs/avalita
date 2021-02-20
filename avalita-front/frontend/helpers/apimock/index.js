import { zuck } from './db_people'
import { todos } from './db_todos'
import { items } from './db_items'
import { mockasync } from './mockutils'

const keepLoggedIn = true

export default {
  login (username, password) {
    return mockasync(zuck)
  },
  logout () {
    return mockasync({})
  },
  whoami () {
    const iam = {authenticated: keepLoggedIn}
    if (iam.authenticated) {
      iam.user = zuck
    }
    return mockasync(iam)
  },
  settings () {
    return mockasync({
      SENTRY_DSN_FRONT: ''
      // SENTRY_DSN_FRONT: 'https://abcd1234@sentry.example.com/10'
    })
  },
  list_todos () {
    return mockasync(todos)
  },
  add_todo (newtask) {
    return mockasync({description: newtask, done: false})
  },
  list_items () {
    return mockasync(items)
  },
  vote (classId, col, value, studentUsername) {
    // todo: tem que mudar na db o valor do rating

    let sum = 0
    let count = 0
    for (let i = 0; i < items.length; i++) {
      const item = items[i]
      if (item.class_id === classId) {
        const v = item.ratings[col]
        if (v) {
          sum += v
          count++
        }
      }
    }
    const score_formatter = (n) => {
      return new Intl.NumberFormat('pt-Br',
        {maximumFractionDigits: 2, minimumFractionDigits: 2}).format(parseFloat(n))
    }
    const votes_formatter = (n) => {
      return new Intl.NumberFormat('pt-Br').format(parseInt(n))
    }
    let score = count > 0 ? score_formatter(sum / count) : '--'
    score += ' (' + votes_formatter(count) + ' votos)'
    return mockasync({rating: value, score})
  },
  load_vote (classId, col, studentUsername) {
    const value = 3
    const score = '2.34 (3 votos)'
    return mockasync({rating: value, score})
  }
}
