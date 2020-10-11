<template>
  <div>
    <Menu />
    <div class="home">
      <Calendar :days="this.days" />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Calendar from '@/components/Calendar'
import Menu from '@/components/Menu';
import axios from "axios";

export default {
  name: 'Home',
  components: {
    Calendar,
    Menu
  },
  data: function () {
    return {
      days: [],
    }
  },
  mounted() {
    const component = this

    axios.get('http://localhost:8000/day/all', {
      headers: {
        'Authorization': component.$session.get('token')
      }
    }).then(function (response) {
      component.days = response.data
    }).catch(function () {
    });
  }
}
</script>
