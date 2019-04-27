import axios from 'axios'

// useful: https://kapeli.com/cheat_sheets/Axios.docset/Contents/Resources/Documents/index

const AUTHORIZATION = 'Authorization'

const ENDPOINT = 'http://ec2-52-63-15-248.ap-southeast-2.compute.amazonaws.com:5000'

export class AuthApi {
  static setAuthorizationHeader(token) {
    axios.defaults.headers.common[AUTHORIZATION] = `Bearer ${token}`
  }

  static removeAuthorizationHeader() {
    delete axios.defaults.headers.common[AUTHORIZATION]
  }

  static async authenticateUser(loginData) {
    return await axios({
      method: 'post',
      url: `${ENDPOINT}/login`,
      data: loginData
    })
  }
}

export class EventsApi {
  static async getEvents() {
    return await axios({
      method: 'get',
      url: `${ENDPOINT}/event`
    });
  }

  static async createEvent(event) {
    return await axios({
      method: 'post',
      url: `${ENDPOINT}/event`,
      data: event
    });
  }
}
