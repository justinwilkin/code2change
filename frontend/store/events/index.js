import { EventsApi } from '../../core/Api'
import {
  REQUEST,
  SUCCESS,
  ERROR,
  EVENTS,
  CLEAR,
  EVENT_BY_ID
} from './methods'

export const state = () => ({
  status: '',
  events: []
})

export const getters = {
  [EVENTS]: state => state.events,
  [EVENT_BY_ID]: state => id => state.events.find(event => event.id === id)
}

export const mutations = {
  [REQUEST]: state => {
    state.status = 'loading'
  },

  [SUCCESS]: (state, { events }) => {
    state.status = 'success'
    state.events = events
  },

  [ERROR]: state => {
    state.status = 'error'
  },

  [CLEAR]: state => {
    state.status = ''
    state.events = ''
  }
}

export const actions = {
  [REQUEST]: ({ commit, dispatch }) =>
    new Promise(async (resolve, reject) => {
      commit(REQUEST);
      try {
        const response = await EventsApi.getEvents();
        commit(SUCCESS, { events: response.data });
        resolve(response);
      } catch (e) {
        commit(ERROR);
        reject(e);
      }
    })
}
