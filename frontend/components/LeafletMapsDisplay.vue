 <template>
  <l-map class="maptest" :zoom="zoom" :center="currentLocation">
    <l-tile-layer :url="url"></l-tile-layer>
    <l-marker :lat-lng="currentLocation"></l-marker>
    <template v-for="(polygon, index) in polygons">
      <l-polygon :key="index" :lat-lngs="polygon.latlngs" :color="polygon.color" @click="polygonClick(polygon.id)"></l-polygon>
    </template>
  </l-map>
</template>

 <script>
export default {
  props: {
    events: Array
  },
  data () {
    return {
      currentLocation: {lat:0,lng:0},
      url: 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
      zoom: 17,
      center: [-33.865143, 151.209900],
      markerLatLng: [0, 0],
      polygons: this.getPolygons()
    }
  },
  mounted: function(){
      this.geolocation();
  },
  methods: {
    getPolygons() {
      const test = this.events.map(event => ({
          latlngs: event.geo_fence,
          color: 'green',
          id: event.id
        }))
        return test
    },
    polygonClick(id) {
      this.$router.push({ path: `events/${id}`})
    },
    geolocation(){
      navigator.geolocation.getCurrentPosition((position) => {
        this.currentLocation = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };
      });
    }
	}
};
</script>

<style lang="scss" scoped>
.map{
  height: 100%;
  width: 100%;
}


//

</style>

