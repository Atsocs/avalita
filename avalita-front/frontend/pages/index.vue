<template>
  <div>
    user: {{user.username}}
    <outer-expansion-panel :student="user" />
  </div>
</template>

<script>
import OuterExpansionPanel from '../components/OuterExpansionPanel'

export default {
  components: {OuterExpansionPanel},
  data () {
    return {
      user: {username: 'alberto', name: 'Alberto'} // todo: remove-me
    }
  }
}
</script>

<style>
</style>
