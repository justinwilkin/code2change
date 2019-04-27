import { EventsApi } from '../../core/Api';
import {
  EVENT,
  NAME,
  DESCRIPTION,
  LOCATION,
  DATE,
  TYPE,
  URL_INFO,
  GEO_FENCE,
  SUBMIT,
  SUCCESS,
  ERROR
} from './methods';

export const state = () => ({
  status: '',
  event: {
    name: '',
    date: '',
    location: '',
    description: '',
    url_info: '',
    geo_fence: [],
    event_type: ''
  }
});

export const getters = {
  [EVENT]: state => state.event,
  [NAME]: state => state.event.name,
  [DESCRIPTION]: state => state.event.description,
  [LOCATION]: state => state.event.location,
  [DATE]: state => state.event.date,
  [TYPE]: state => state.event.event_type,
  [URL_INFO]: state => state.event.url_info,
  [GEO_FENCE]: state => state.event.geo_fence
}

export const mutations = {
  [EVENT]: (state, value) => {
    state.event = value;
  },
  [NAME]: (state, value) => {
    state.event.name = value;
  },
  [DESCRIPTION]: (state, value) => {
    state.event.description = value;
  },
  [LOCATION]: (state, value) => {
    state.event.location = value;
  },
  [DATE]: (state, value) => {
    state.event.date = value;
  },
  [TYPE]: (state, value) => {
    state.event.event_type = value;
  },
  [URL_INFO]: (state, value) => {
    state.event.url_info = value;
  },
  [GEO_FENCE]: (state, value) => {
    state.event.geo_fence = value;
  },

  [SUBMIT]: state => {
    state.status = 'loading';
  },
  [SUCCESS]: state => {
    state.status = 'success';
  },
  [ERROR]: state => {
    state.status = 'error';
  }
};

export const actions = {
  [SUBMIT]: ({ commit, dispatch, state }) =>
    new Promise(async (resolve, reject) => {
      commit(SUBMIT);
      try {
        const response = await EventsApi.createEvent(state.event);
        commit(SUCCESS);
        resolve(response);
      } catch (e) {
        commit(ERROR);
        reject(e);
      }
    })
}
