import { storeModule } from '../../core/helpers'

const MODULE = 'event'
export const EVENT = `event`
export const NAME = `name`
export const DESCRIPTION = `description`
export const LOCATION = `location`
export const DATE = `date`
export const TYPE = 'type'
export const URL_INFO = 'url_info'
export const GEO_FENCE = 'geo_fence'
export const SUBMIT = 'submit'
export const SUCCESS = 'success'
export const ERROR = 'error'

export const eventModule = method => storeModule(MODULE, method)
