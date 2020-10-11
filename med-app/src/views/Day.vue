<template>
  <div>
    <Menu />
    <div class="day">
      <h1>{{ day.date | formatDate('DD MMMM YYYY') }}</h1>
      <PainEvaluations :date="this.date"/>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Menu from '@/components/Menu';
import PainEvaluations from '@/components/PainEvaluations';
import axios from "axios";

export default {
  name: 'Day',
  components: {
    Menu,
    PainEvaluations
  },
  props: {
    date: String
  },
  data: function () {
    return {
      day: {},
    }
  },
  mounted() {
    const component = this

    axios.get('http://localhost:8000/day?date=' + component.date, {
      headers: {
        'Authorization': component.$session.get('token')
      }
    }).then(function (response) {
      component.day = response.data
    }).catch(function () {
    });
  }
}
</script>
