<template>
  <v-card class="mx-auto" outlined>
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title>
          {{question}}
        </v-list-item-title>
        <v-list-item-content>
          Seu voto: {{rating}} - {{rating_text[rating - 1]}}<br>
          Pontuação: {{score_formatter(score)}} ({{votes_formatter(votes)}} votos)
        </v-list-item-content>
      </v-list-item-content>
    </v-list-item>
    <v-divider />
    <v-card-actions>
      <v-row align="center">
        <v-rating dense hover length="5" size="20" class="ml-4" v-model="rating" />
        <v-spacer />
        <v-btn outlined text color="primary" class="mr-4">Votar</v-btn>
      </v-row>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: 'Rating',
  props: ['score', 'votes', 'question'],
  data () {
    return {
      rating: 3,
      rating_text: ['De jeito nenhum', 'Não muito', 'Mais ou menos', 'Razoavalmente', 'Muito']
    }
  },
  methods: {
    score_formatter (n) {
      return (new Intl.NumberFormat('pt-Br',
        {maximumFractionDigits: 2, minimumFractionDigits: 2})).format(parseFloat(n))
    },

    votes_formatter (n) {
      return (new Intl.NumberFormat('pt-Br')).format(parseInt(n))
    }
  }
}
</script>

<style scoped>

</style>
