import { combineReducers } from 'redux'
import AuthReducer from './app/auth/duck/reducers'
import marketReducer from './app/market/duck/reducers'

const rootReducer = combineReducers({
  authentication: AuthReducer,
  market: marketReducer
})

export default rootReducer
