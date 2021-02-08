<template>
  <div>
    <v-expansion-panels>
      <v-expansion-panel
        v-for="(item,name) in groupedItems(items)"
        :key="name"
      >
        <v-expansion-panel-header>
          {{name}}
        </v-expansion-panel-header>
        <v-expansion-panel-content v-for="(subItem, i) in item" :key="i"
        class="text-center">
          {{subItem.professor.name}}<br>
          ({{subItem.course_abbr}} - {{subItem.course_name}})
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'Periods',
  props: ['items'],
  data () {
    return {}
  },
  methods: {
    groupedItems (x) {
      //
      return _.mapValues(_.groupBy(x, 'period'),
        clist => clist.map(x => _.omit(x, 'period')))
    }
  }
}
</script>

<style scoped>

</style>
