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
  props: ['score', 'question', 'rating'],
  data () {
    return {
      rating_text: ['De jeito nenhum', 'Não muito', 'Mais ou menos', 'Razoavalmente', 'Muito']
    }
  }
}
</script>

<style scoped>

</style>
