<template>
    <div id="page-login">
        <div id="cover-slide" :class="{ loggingin: loggingIn }"></div>
        <section id="login-section">
            <div class="btn blue" v-on:click="handleJoin" :class="{ loggingin: loggingIn }">Join</div>
            <div class="btn red" v-on:click="handleLoggingIn" :class="{ loggingin: loggingIn }">Log in</div>

            <input type="text" class="ipt" id="username" :class="{ loggingin: loggingIn }" placeholder="Username" v-model="username"/>
            <input type="password" class="ipt" id="password" :class="{ loggingin: loggingIn }" placeholder="Password" v-model="password"/>
            <div class="btn red" id="login-btn" v-on:click="handleSubmitLogin" :class="{ loggingin: loggingIn }">Submit</div>
        </section>
    </div>
</template>

<script>
export default {
  layout: 'default',
  data() {
      return {
          loggingIn: false,
          username: '',
          password: ''
      }
  },
  methods: {
      // Handle our Join Button clicked
      handleJoin: function(e) {
      },
      // Handle our Login Button clicked
      handleLoggingIn: function(e) {
          this.loggingIn = true;
      },
      // Handle submitting our login
      handleSubmitLogin: function(e) {
          console.log("User has logged in. {username:"+this.username+",password:"+this.password+"}");
            // Broadcast our event with our user's credentials
            this.$emit('user-credentials', {"username":this.username, "password":this.password});
            // Navigate to our home page
            this.$router.push({ path: "/" });
      }
  }
}
</script>

<style lang="scss" scoped>
@import '~assets/global';

#cover-slide {
    width: 100%;
    height: 60vh;
    background-color: $color-red;
    margin-bottom: 80px;
    -webkit-transition: height 1s; /* Safari */
    transition: height 1s;
    &.loggingin {
        height: 30vh;
    }
}

.btn {
    width: 70vw;
    padding: 15px;
    position: relative;
    left: 15vw;
    opacity: 1;
    margin-top: 35px;
    text-align: center;
    font-size: 20px;
    -webkit-transition: opacity 1s; /* Safari */
    transition: opacity 1s;
    &.loggingin {
        opacity: 0;
    }
}

.btn.blue {
  background-color: $color-light-blue;
  color: $color-white;
}

.btn.red {
  background-color: $color-red;
  color: $color-white;
}

#login-btn {
    opacity: 0;
    &.loggingin {
        opacity: 1;
    }
}

.ipt {
    padding-left: 20px;
    font-family: 'Lato';
    width: 70vw;
    position: relative;
    left: 15vw;
    opacity: 0;
    height: 50px;
    margin-bottom: 25px;
    border: 0;
    border-bottom: 1px solid $color-red;
    position: relative;
    top: -100px;
    display: none;
    &.loggingin {
        display: block;
        opacity: 1;
    }
}
</style>
