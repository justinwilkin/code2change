 <template>
  <l-map class="map" :zoom="zoom" :center="currentLocation" @click='addPoint'>
    <l-tile-layer :url="url"></l-tile-layer>
    <l-polygon :lat-lngs="polygon.latlngs" :color="polygon.color" b></l-polygon>
        <l-marker :lat-lng="currentLocation" ></l-marker>
  </l-map>
</template>
 
 <script>
export default {
  data () {
    return {
      currentLocation: {lat:0,lng:0},
      url: 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
      zoom: 17,
      center: [0, 0],
      markerLatLng: [0, 0],
      polygon: {
        latlngs: [],
        color: 'green'
      }
    };
  },
  mounted: function(){
      this.geolocation();
  },
  methods: {
		addPoint(event) {
      if(this.polygon.latlngs.length == 4){
      	this.polygon.latlngs = []
      }
      this.polygon.latlngs.push(event.latlng);
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
height: 100%; width: 100%
}
</style>
 