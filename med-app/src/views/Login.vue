<template>
  <div class="login">
    <h1>Se connecter</h1>
    <p v-if="this.error" class="error">{{ this.error }}</p>
    <form @submit="login">
      <div>
        <label for="name">Name</label>
        <input
                id="name"
                v-model="name"
                type="text"
                name="name"
        >
      </div>

      <div>
        <label for="password">Password</label>
        <input
                id="password"
                v-model="password"
                type="password"
                name="password"
        >
      </div>
      <input type="submit" value="Se connecter">
    </form>
  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    name: 'Login',
    data: function() {
      return {
        name: null,
        password: null,
        token: null,
        error: null
      };
    },
    methods:{
      login: function (e) {
        e.preventDefault();
        const component = this

        axios.post('http://localhost:8000/login', {
          name: this.name,
          password: this.password
        }).then(function (response) {
          const token = response.data.token
          component.token = token
          component.$session.start()
          component.$session.set('token', token)
          component.$router.push('/')
        }).catch(function (e) {
            component.error = e
        });
      }
    }
  }
</script>
