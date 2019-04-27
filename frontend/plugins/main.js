import Vue from 'vue'
import * as VueGoogleMaps from 'vue2-google-maps'
 
Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyD8DPDTZUYDzF_XgLXD7JaUUcNcv-xc-nY',
    libraries: 'places',
  },
})