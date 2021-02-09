<template>
  <v-expansion-panels>
    <v-expansion-panel
      v-for="(item,period) in groupedItems"
      :key="period"
    >
      <v-expansion-panel-header class="subtitle-1">
        {{period}}
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        <v-expansion-panels>
          <v-expansion-panel
            v-for="(subItem, i) in item"
            :key="i"
          >
            <v-expansion-panel-header>
              <div>
                <span class="subtitle-2">{{subItem.professor.name}}</span> |
                <span class="body-2">{{subItem.course_abbr}} | {{subItem.course_name}}</span> |
                <span class="outline">{{subItem.student.name}}</span>
              </div>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <course :items="items" :item="subItem" />
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script>
import _ from 'lodash'
import Course from './Course'

export default {
  name: 'Periods',
  components: {Course},
  props: ['items'],
  data () {
    return {}
  },
  computed: {
    groupedItems () {
      return _.mapValues(_.groupBy(this.items, 'period'),
        c_list => c_list.map(x => _.omit(x, 'period')))
    }
  }
}
</script>

<style scoped>

</style>
