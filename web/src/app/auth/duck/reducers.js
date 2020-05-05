import * as types from './types'

const initialState = {
  isAuthenticated: false
}

const AuthReducer = (state = initialState, action) => {
  switch (action.type) {
    case types.LOGIN_SUCCESS:
      return {
        ...state,
        isAuthenticated: true
      }
    case types.LOGIN_FAILURE:
      return {
        ...state,
        isAuthenticated: false
      }
    case types.LOGOUT:
      return {
        ...state,
        isAuthenticated: false
      }
    default:
      return state
  }
}

export default AuthReducer
