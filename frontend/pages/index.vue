<template>
  <div>
<!--    <pre>-->
      {{items}}
<!--    </pre>-->
    <periods :items="items" />
  </div>
</template>

<script>
import Periods from '../components/Periods'

export default {
  components: {Periods},
  data () {
    return {
      items: [
        {
          class_id: 0,
          period: '2020 - 1° semestre',
          student: {name: 'Alberto'},
          professor: {username: 'bsilva', name: 'Beltrano Silva'},
          course_abbr: 'ART-01',
          course_name: 'Introdução à Carteação',
          ratings: [null, 2, null, 1]
        },
        {
          class_id: 2,
          period: '2020 - 1° semestre',
          student: {name: 'Bianca'},
          professor: {username: 'csilva', name: 'Ciclano Silva'},
          course_abbr: 'MAC-01',
          course_name: 'Introdução ao Macaco',
          ratings: [4, null, 4, null]
        },
        {
          class_id: 2,
          period: '2020 - 1° semestre',
          student: {name: 'Camila'},
          professor: {username: 'csilva', name: 'Ciclano Silva'},
          course_abbr: 'MAC-01',
          course_name: 'Introdução ao Macaco',
          ratings: [3, 2, 3, 3]
        },
        {
          class_id: 2,
          period: '2020 - 1° semestre',
          student: {name: 'Dudu'},
          professor: {username: 'csilva', name: 'Ciclano Silva'},
          course_abbr: 'MAC-01',
          course_name: 'Introdução ao Macaco',
          ratings: [5, 4, 5, 4]
        },
        {
          class_id: 2,
          period: '2020 - 1° semestre',
          student: {name: 'Elane'},
          professor: {username: 'csilva', name: 'Ciclano Silva'},
          course_abbr: 'MAC-01',
          course_name: 'Introdução ao Macaco',
          ratings: [4, 4, 3, 2]
        },
        {
          class_id: 1,
          period: '2020 - 2° semestre',
          student: {name: 'Fernando'},
          professor: {username: 'fsilva', name: 'Fulano Silva'},
          course_abbr: 'ART-02',
          course_name: 'Introdução à Carteação 2',
          ratings: [3, 1, 2, null]
        }
      ]
    }
  }
}
</script>

<style>
</style>
