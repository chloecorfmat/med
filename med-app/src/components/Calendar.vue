<template>
    <div class="calendar">
        <ul>
            <li v-for="day in this.days" v-bind:key="day.id">
                <router-link :to="{ name: 'Day', params: { date: day.dateFormatted }}">{{ day.date | formatDate('DD MMMM YYYY') }}</router-link>
            </li>
            <li>
                <DatePicker
                        v-model="date"
                        is-inline
                        :attributes='attributes'
                        :disabled-dates="disabledDates"
                />
                <button v-on:click="addDay">Ajouter</button>
                <p v-if="this.error">{{ this.error }}</p>
            </li>
        </ul>
    </div>
</template>

<script>
    import DatePicker from 'v-calendar/lib/components/date-picker.umd'
    import axios from "axios";
    import moment from "moment";

    export default {
        name: 'Calendar',
        components: {
            DatePicker
        },
        props: {
            days: Array
        },
        updated: function () {
            if (this.disabledDates == null) {
                this.disabledDates = []
                for(const day of this.days) {
                    this.disabledDates.push(new Date(day.date))
                }
            }
        },
        data: function () {
            return {
                date: new Date(),
                attributes: [
                    {
                        highlight: true,  // Boolean, String, Object
                        dates: this.date,
                        order: 0,
                    }
                ],
                disabledDates: null,
                error: null,
            }
        },
        methods: {
            addDay: function() {
                if (this.date) {
                    this.error = null

                    const component = this

                    axios.post('http://localhost:8000/day', {
                        date: moment(component.date).format("YYYY-MM-DD"),
                    }, {
                        headers: {
                            'Authorization': component.$session.get('token')
                        }
                    }).then(function () {
                        component.$router.push('/day/' + moment(component.date).format("YYYY-MM-DD"))

                    }).catch(function (e) {
                        component.error = e
                    });

                } else {
                    this.error = 'Veuillez entrer une date.'
                }
            }
        }
    }
</script>
