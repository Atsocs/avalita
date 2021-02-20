<template>
  <div>
    <h1>página do professor {{ $route.params.username }}</h1>
    <v-select
      :items="x"
      label="Disciplina"
    />
  </div>
</template>

<script>
export default {
  data () {
    return {
      x: ['Foo', 'Bar', 'Fizz', 'Buzz']
    }
  }
}
</script>

<style scoped>

</style>
