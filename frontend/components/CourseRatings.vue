<template>
  <v-row no-gutters>
    <template v-for="(info, n) in getCourseInfo(item)">
      <v-col :key="n" class="ma-1">
        <rating
          :question="info.title"
          :score="info.score" :votes="info.votes" :rating="info.rating" class="text-left"
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
  props: ['items', 'item'],
  data () {
    return {
      titles: [
        'Gostaria de fazer outra disciplina com este(a) professor(a)?',
        'O(A) professor(a) foi coerente?',
        'O(A) professor(a) explicava bem?',
        'Foi fácil passar nesta Disciplina?'
      ]
    }
  },
  methods: {
    getCourseInfo (item) {
      return [...this.titles].map((title, col) => {
        return {
          title,
          score: this.getScore(item.class_id, col),
          rating: this.item.ratings[col]
        }
      })
    },
    getScore (class_id, col) {
      let sum = 0
      let count = 0
      for (let i = 0; i < this.items.length; i++) {
        const item = this.items[i]
        if (item.class_id === class_id) {
          const v = item.ratings[col]
          if (v) {
            sum += v
            count++
          }
        }
      }
      const score = count > 0 ? this.score_formatter(sum / count) : '--'
      return score + ' (' + this.votes_formatter(count) + ' votos)'
    },
    votes_formatter (n) {
      return (new Intl.NumberFormat('pt-Br')).format(parseInt(n))
    },
    score_formatter (n) {
      return (new Intl.NumberFormat('pt-Br',
        {maximumFractionDigits: 2, minimumFractionDigits: 2})).format(parseFloat(n))
    }
  }
}
</script>

<style scoped>

</style>
