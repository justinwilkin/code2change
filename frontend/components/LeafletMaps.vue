 <template>
  <l-map style="height: 100%; width: 100%" :zoom="zoom" :center="center" @click='addPoint'>
    <l-tile-layer :url="url"></l-tile-layer>
    <l-polygon :lat-lngs="polygon.latlngs" :color="polygon.color"></l-polygon>
  </l-map>
</template>
 
 <script>
export default {
  data () {
    return {
      url: 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
      zoom: 8,
      center: [47.413220, -1.319482],
      markerLatLng: [47.313220, -1.319482],
      polygon: {
        latlngs: [],
        color: 'green'
      },
    };
  },
  methods: {
		addPoint(event) {
      if(this.polygon.latlngs.length == 4){
      	this.polygon.latlngs = []
      }
      this.polygon.latlngs.push(event.latlng);
      console.log(this.polygon.latlngs)
		}
	}
};
</script>
 
 <style>
</style>
 