import Vue from 'vue'
import * as VueGoogleMaps from 'vue2-google-maps'
 
Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyC7ojzhbZ8GpcmCaKoDY2cUsVRDMq3R1YI',
    libraries: 'places',
  },
})