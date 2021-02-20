<template>
  <v-card class="mx-auto" outlined>
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title class="body-2">
          {{question}}
        </v-list-item-title>
        <v-list-item-content class="body-2">
          Pontuação: {{score}}<br>
          Seu voto: {{rating}} - {{rating_text[rating - 1]}}
        </v-list-item-content>
      </v-list-item-content>
    </v-list-item>
    <v-divider />
    <v-card-actions>
      <v-progress-linear v-if="loading" />
      <template v-else>
        <v-row align="center">
          <v-rating dense hover length="5" size="20" class="ml-4" v-model="rating" />
          <v-spacer />
          <v-btn outlined text color="primary" class="mr-4" @click="vote(rating)">Votar</v-btn>
        </v-row>
      </template>
    </v-card-actions>
  </v-card>
</template>

<script>
import api from '~api'
// eslint-disable-next-line no-unused-vars
import Snacks from '~/helpers/Snacks.js'

export default {
  name: 'Rating',
  props: ['question', 'col', 'classId', 'studentUsername'],
  data () {
    return {
      rating_text: ['De jeito nenhum', 'Não muito', 'Mais ou menos', 'Razoavalmente', 'Muito'],
      voting: false,
      loading: false,
      score: null,
      rating: null
    }
  },
  async mounted () {
    this.loading = true
    const response = await api.load_vote(this.classId, this.col, this.studentUsername)
    this.rating = response.rating
    this.score = response.score
    this.loading = false
  },
  methods: {
    async vote (value) {
      this.voting = true
      const response = await api.vote(value, this.classId, this.col, this.studentUsername)
      this.rating = response.rating
      this.score = response.score
      window.alert('Voto atualizado!')
      // Snacks.show(this.$store, {text: 'Voto atualizado!'}) // todo: arrumar snacks, buga se usar duas vezes esperando fechar sozinha
      this.voting = false
    }

  }
}
</script>

<style scoped>

</style>
