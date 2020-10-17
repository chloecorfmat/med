<template>
  <div>
    <Menu />
    <div class="day">
      <div>
        <h1>{{ day.date | formatDate('DD MMMM YYYY') }}</h1>
        <div>
          <form @submit="addComment">
            <textarea cols="30" rows="10" v-model="comment"></textarea>
            <button >Ajouter un commentaire</button>
          </form>

        </div>
        <PainEvaluations :date="this.date"/>
      </div>
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
      comment: null,
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
      component.comment = component.day.comment
    }).catch(function () {
    });
  },
  methods: {
    addComment: function () {
      const component = this

      axios.post('http://localhost:8000/day/comment', {
        comment: this.comment,
        date: this.date
      },{
        headers: {
          'Authorization': component.$session.get('token')
        }}).then(function (response) {
        component.day = response.data
      }).catch(function (e) {
        component.error = e
      });
    }
  }
}
</script>
