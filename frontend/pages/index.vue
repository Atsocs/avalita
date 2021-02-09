<template>
  <div v-show="!loading">
    user: {{user.username}}
    <outer-expansion-panel :student="user" :items="items" />
    <span class="title">items</span>
    <pre>
      {{items}}
    </pre>
  </div>
</template>

<script>
import OuterExpansionPanel from '../components/OuterExpansionPanel'
import api from '~api'

export default {
  components: {OuterExpansionPanel},
  data () {
    return {
      loading: true,
      items: [],
      user: {username: 'alberto', name: 'Alberto'}
    }
  },
  async mounted () {
    this.loading = true
    const response = await api.list_items()
    const todos = response.items
    this.items = todos
    this.loading = false
  }
}
</script>

<style>
</style>
