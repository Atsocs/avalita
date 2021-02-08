<template>
    <div>
        {{ret}}
        <v-expansion-panels>
            <v-expansion-panel
                    v-for="(item,i) in groupedItems(items)"
                    :key="i"
            >
                <v-expansion-panel-header>
                    {{item.period}}
                </v-expansion-panel-header>
                <v-expansion-panel-content v-for="(course, j) in item.courses">
                    {{item.courses[j].professor.name}}<br>
                    {{item.courses[j].course_abbr}}: {{item.courses[j].course_name}}
                </v-expansion-panel-content>
            </v-expansion-panel>
        </v-expansion-panels>
    </div>
</template>

<script>
    import _ from 'underscore'

    export default {
        name: 'Periods',
        props: ['items'],
        data () {
            return {
                ret: null
            }
        },
        methods: {
            groupedItems (x) {
                //

                const ret = _.mapValues(_.groupBy(x, 'period'),
                    clist => clist.map(x => _.omit(x, 'period')))
                this.ret = ret
                return ret

                // return [
                //     {
                //         period: '2020 - 1° semestre',
                //         courses: [
                //             {
                //                 professor: {username: 'fpereira', name: 'Fulano Silva'},
                //                 course_abbr: 'ART-01',
                //                 course_name: 'Introdução à Carteação',
                //                 rates: [0, 0, 0, 0]
                //             }
                //         ]
                //     },
                //     {
                //         period: '2020 - 2° semestre',
                //         courses: [
                //             {
                //                 professor: {username: 'fpereira', name: 'Beltrano Silva'},
                //                 course_abbr: 'ART-02',
                //                 course_name: 'Introdução à Carteação 2',
                //                 rates: [0, 0, 0, 0]
                //             }
                //         ]
                //     }
                // ]
            }
        }
    }
</script>

<style scoped>

</style>
