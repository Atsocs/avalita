<template>
  <v-row no-gutters v-else>
    <template v-for="(title, n) in titles">
      <v-col :key="n" class="ma-1">
        <rating
          :question="title"
          :col="n" :class-id="item.class_id"
          :student-username="item.student.username"
          class="text-left"
        />
      </v-col>
      <v-responsive
        v-if="(n + 1) % 2 === 0"
        :key="`width-${n}`"
        width="100%"
      />
    </template>
  </v-row>
</template>

<script>
import Rating from './Rating'

export default {
  name: 'CourseRatings',
  components: {Rating},
  props: ['item'],
  items: [],
  data () {
    return {
      loading: true,
      titles: [
        'Gostaria de fazer outra disciplina com este(a) professor(a)?',
        'O(A) professor(a) foi coerente?',
        'O(A) professor(a) explicava bem?',
        'Foi fácil passar nesta Disciplina?'
      ]
    }
  }
}
</script>

<style scoped>

</style>
