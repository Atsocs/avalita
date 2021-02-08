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
                        period: '2020 - 2° semestre',
                        professor: {username: 'fpereira', name: 'Fulano Silva'},
                        course_abbr: 'ART-01',
                        course_name: 'Introdução à Carteação',
                        rates: [0, 0, 0, 0]
                    },
                    {
                        period: '2020 - 2° semestre',
                        professor: {username: 'fpereira', name: 'Fulano Silva'},
                        course_abbr: 'ART-01',
                        course_name: 'Introdução à Carteação',
                        rates: [0, 0, 0, 0]
                    }
                ]
            }
        }
    }
</script>

<style>
</style>
