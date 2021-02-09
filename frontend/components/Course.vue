<template>
  <v-row no-gutters>
    <template v-for="(q, n) in questions">
      <v-col :key="n" class="ma-1">
        <rating
          :question="q"
          :score="3.2" :votes="122" class="text-left"
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
  name: 'Course',
  components: {Rating},
  data () {
    return {
      questions: [
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
