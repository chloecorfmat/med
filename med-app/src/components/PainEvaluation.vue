<template>
    <div class="pain-evaluation">
        <h1>{{ this.name }}</h1>
        <div>
            <button v-for="n in 10" :key="n" v-on:click="submitPainEvaluation(n)" :value="n" v-bind:class="[value == n ? 'active' : '']">{{ n }}</button>
        </div>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        name: 'PainEvaluation',
        components: {
        },
        props: {
            date: String,
            type: String,
            name: String
        },
        data: function () {
            return {
                value: null,
            }
        },
        mounted: function() {
            const component = this

            axios.get('http://localhost:8000/pain-value?type=' + this.type + '&date=' + this.date, {
                headers: {
                    'Authorization': component.$session.get('token')
                }
            }).then(function (response) {
                component.value = response.data.value
            }).catch(function () {
            });
        },
        methods: {
            submitPainEvaluation(value) {
                const component = this
                console.log(value)

                axios.post('http://localhost:8000/pain', {
                    date: component.date,
                    type: component.type,
                    value: value
                }, {
                    headers: {
                        'Authorization': component.$session.get('token')
                    }
                }).then(function (response) {
                    console.log(response.data)
                    component.value = value
                }).catch(function (e) {
                    component.error = e
                });
            }
        }
    }
</script>

<style scoped>
    .active {
        background: red;
    }
</style>
