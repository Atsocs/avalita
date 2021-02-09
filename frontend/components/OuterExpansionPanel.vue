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
            v-if="subItem.student.username === student.username"
            v-for="(subItem, i) in item"
            :key="i"
          >
            <v-expansion-panel-header>
              <div>
                <span class="body-2">{{subItem.course_abbr}} | {{subItem.course_name}}</span> |
                <span class="outline">{{subItem.student.name}}</span>
              </div>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <router-link
                class="body-2"
                text
                :to="{ name: 'p', params: { username: subItem.professor.username }}"
              >
                {{subItem.professor.name}}
              </router-link>
              <course-ratings :items="items" :item="subItem" />
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script>
import _ from 'lodash'
import CourseRatings from './CourseRatings'
import api from '~api'

export default {
  name: 'OuterExpansionPanel',
  components: {CourseRatings},
  props: ['student'],
  data () {
    return {
      loading: true,
      items: []
    }
  },
  computed: {
    groupedItems () {
      return _.mapValues(_.groupBy(this.items, 'period'),
        c_list => c_list.map(x => _.omit(x, 'period')))
    }
  },
  async mounted () {
    this.loading = true
    const response = await api.list_items()
    this.items = response.items
    this.loading = false
  }
}
</script>

<style scoped>

</style>
