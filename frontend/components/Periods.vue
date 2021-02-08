<template>
  <div>
    <v-expansion-panels>
      <v-expansion-panel
        v-for="(item,period) in groupedItems(items)"
        :key="period"
      >
        <v-expansion-panel-header>
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
                  <span class="title">
                    {{subItem.professor.name}}
                  </span>
                  <span class="body-2">
                    {{subItem.course_abbr}} | {{subItem.course_name}}
                  </span>
                </div>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <course />
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
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
  methods: {
    groupedItems (x) {
      return _.mapValues(_.groupBy(x, 'period'),
        c_list => c_list.map(x => _.omit(x, 'period')))
    }
  }
}
</script>

<style scoped>

</style>
