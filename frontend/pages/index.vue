<template>
  <div>
    user: {{user.username}}
    <outer-expansion-panel :student="user" :items="items" />
    <span class="title">items</span>
    <pre>
      {{items}}
    </pre>
  </div>
</template>

<script>
import OuterExpansionPanel from '../components/OuterExpansionPanel'

export default {
  components: {OuterExpansionPanel},
  data () {
    return {
      items: [
        {
          class_id: 0,
          period: '2020 - 1° semestre',
          student: {username: 'alberto', name: 'Alberto'},
          professor: {username: 'bsilva', name: 'Beltrano Silva'},
          course_abbr: 'ART-01',
          course_name: 'Introdução à Carteação',
          ratings: [null, 2, null, 1]
        },
        {
          class_id: 0,
          period: '2020 - 1° semestre',
          student: {username: 'alberto', name: 'Alberto'},
          professor: {username: 'cmaranhao', name: 'Ciclano Maranhão'},
          course_abbr: 'MAC-01',
          course_name: 'Introdução ao Macaco',
          ratings: [5, 5, 5, 4]
        },
        {
          class_id: 2,
          period: '2020 - 1° semestre',
          student: {username: 'bianca', name: 'Bianca'},
          professor: {username: 'cmaranhao', name: 'Ciclano Maranhão'},
          course_abbr: 'MAC-01',
          course_name: 'Introdução ao Macaco',
          ratings: [4, null, 4, null]
        },
        {
          class_id: 2,
          period: '2020 - 1° semestre',
          student: {username: 'camila', name: 'Camila'},
          professor: {username: 'cmaranhao', name: 'Ciclano Maranhão'},
          course_abbr: 'MAC-01',
          course_name: 'Introdução ao Macaco',
          ratings: [3, 2, 3, 3]
        },
        {
          class_id: 2,
          period: '2020 - 1° semestre',
          student: {username: 'dudu', name: 'Dudu'},
          professor: {username: 'cmaranhao', name: 'Ciclano Maranhão'},
          course_abbr: 'MAC-01',
          course_name: 'Introdução ao Macaco',
          ratings: [5, 4, 5, 4]
        },
        {
          class_id: 2,
          period: '2020 - 1° semestre',
          student: {username: 'elane', name: 'Elane'},
          professor: {username: 'cmaranhao', name: 'Ciclano Maranhão'},
          course_abbr: 'MAC-01',
          course_name: 'Introdução ao Macaco',
          ratings: [4, 4, 3, 2]
        },
        {
          class_id: 1,
          period: '2020 - 2° semestre',
          student: {username: 'fernando', name: 'Fernando'},
          professor: {username: 'fulano', name: 'Fulano Pereira'},
          course_abbr: 'ART-02',
          course_name: 'Introdução à Carteação 2',
          ratings: [3, 1, 2, null]
        },
        {
          class_id: 1,
          period: '2020 - 2° semestre',
          student: {username: 'alberto', name: 'Alberto'},
          professor: {username: 'bsilva', name: 'Beltrano Silva'},
          course_abbr: 'ART-02',
          course_name: 'Introdução à Carteação 2',
          ratings: [3, 2, null, null]
        }
      ]
    }
  },
  computed: {
    user () { return this.items[0].student }
  }
}
</script>

<style>
</style>
