<template>
    <div clas="page-section" id="page-login">
        <div id="cover-slide" :class="{ loggingin: loggingIn }"></div>
        <section id="login-section">
            <button v-on:click="loginClick" :class="{ loggingin: loggingIn }">Login</button>
            <a v-on:click="handleJoin" :class="{ loggingin: loggingIn }">Register</a>
            <label for="username" :class="{ loggingin: loggingIn }">Username</label>
            <input type="text" id="username" :class="{ loggingin: loggingIn }" v-model="login.username"/>
            <label for="password" :class="{ loggingin: loggingIn }">Password</label>
            <input type="password" id="password" :class="{ loggingin: loggingIn }" v-model="login.password"/>
            <button id="login-btn" v-on:click="handleSubmitLogin" :class="{ loggingin: loggingIn }">Login</button>
        </section>
    </div>
</template>

<script>
import { authModule, REQUEST, USER } from '../store/auth/methods'
export default {
  layout: 'default',
  data() {
      return {
          loggingIn: false,
          login: {
            username: 'barry',
            password: 'cactus'
          }
      }
  },
  methods: {
      // Handle our Login Button clicked
      loginClick(e) {
          this.loggingIn = true;
      },
      // Handle submitting our login
      async handleSubmitLogin(e) {
        await this.$store.dispatch(authModule(REQUEST), this.login)
        // Navigate to our home page
        this.$router.push({ path: "/" });
      }
  }
}
</script>

<style lang="scss" scoped>
@import '~assets/variables';

#login-section {
  width: 70%;
  margin: 0 auto;
  input, button {
    width: 100%;
  }
}

#cover-slide {
    width: 100%;
    height: 60vh;
    -webkit-transition: height 1s; /* Safari */
    transition: height 1s;
    &.loggingin {
        height: 0;
    }
}

button, a {

  // width: 70vw;
  // position: relative;
  // left: 15vw;
  opacity: 1;
  -webkit-transition: opacity 1s; /* Safari */
  transition: opacity 1s;
  margin-bottom: 25px;
  &.loggingin {
      opacity: 0;
  }
}

a {
  display: block;
  text-align: center;
}

#login-btn, label, input {
    opacity: 0;
    display: none;
    &.loggingin {
        display: block;
        opacity: 1;
    }
}

</style>
