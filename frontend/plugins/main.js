import Vue from 'vue'
import * as VueGoogleMaps from 'vue2-google-maps'

 console.log(process.env.keyWord.toString())
Vue.use(VueGoogleMaps, {
  load: {
    key: process.env.keyWord.toString(),
    libraries: 'places',
  },
})