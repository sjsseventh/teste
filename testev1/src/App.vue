<template>
  <div class="phone-viewport">
    <md-toolbar md-theme="default">
      <h1 class="md-title">{{title}}</h1>
    </md-toolbar>
  
    <HelloWorld></HelloWorld>
  </div>

</template>

<script>
import HelloWorld from './components/HelloWorld.vue';

export default {
  name: 'App',
  data () {
    return {
      title: 'Teste Cedro'
    }
  },

  components: {
    HelloWorld
  },

  methods: {
    teste () {
      console.log('teste')
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
