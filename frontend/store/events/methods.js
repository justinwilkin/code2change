import { storeModule } from '../../core/helpers'

const MODULE = 'events'
export const REQUEST = `request`
export const SUCCESS = `success`
export const ERROR = `error`
export const EVENTS = 'events'
export const CLEAR = 'clear'
export const EVENT_BY_ID = 'getEventById'

export const eventsModule = method => storeModule(MODULE, method)
