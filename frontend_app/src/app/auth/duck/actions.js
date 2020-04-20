import * as types from './types'

export const loginSuccess = () => {
  return {
    type: types.LOGIN_SUCCESS
  }
}

export const loginFailure = () => {
  return {
    type: types.LOGIN_FAILURE
  }
}

export const logout = () => {
  return {
    type: types.LOGOUT
  }
}
