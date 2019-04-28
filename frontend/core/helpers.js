import Vue from 'vue'
import moment from 'moment'

export const requiredRule = value => value =>
  !!value || Vue.prototype.$messages.Required

export const getExpiryOptions = shouldRemember => {
  const oneHour = moment()
    .add(1, 'hours')
    .toDate()

  let options = {}
  if (!shouldRemember) {
    options.expires = oneHour
  }
  return options
}

/**
 * storeModule
 * @param {*} module
 * @param {*} method
 */
export const storeModule = (moduleName, method) => {
  return `${moduleName}/${method}`
}

export const collides = (geo_fence, latlng) => {
  return (latlng.lat < geo_fence[0].lat && latlng.lat < geo_fence[1].lat
    && latlng.lat > geo_fence[2].lat && latlng.lat > geo_fence[3].lat
    && latlng.lng < geo_fence[1].lng && latlng.lng < geo_fence[2].lng
    && latlng.lng > geo_fence[0].lng && latlng.lng > geo_fence[3].lng)
}
