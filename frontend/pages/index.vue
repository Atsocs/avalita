<template>
  <periods :items="items" />
</template>

<script>
import Periods from '../components/Periods'

export default {
  components: {Periods},
  data () {
    return {
      items: [
        {
          period: '2020 - 1° semestre',
          professor: {username: 'fsilva', name: 'Fulano Silva'},
          course_abbr: 'ART01',
          course_name: 'Introdução à Carteação',
          rates: [0, 0, 0, 0]
        },
        {
          period: '2020 - 2° semestre',
          professor: {username: 'bsilva', name: 'Beltrano Silva'},
          course_abbr: 'ART02',
          course_name: 'Introdução à Carteação 2',
          rates: [0, 0, 0, 0]
        },
        {
          period: '2020 - 1° semestre',
          professor: {username: 'csilva', name: 'Ciclano Silva'},
          course_abbr: 'MAC01',
          course_name: 'Introdução ao Macaco',
          rates: [0, 0, 0, 0]
        }
      ]
    }
  }
}
</script>

<style>
</style>
