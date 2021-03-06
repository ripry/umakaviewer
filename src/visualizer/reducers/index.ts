import { combineReducers } from 'redux'
import property from './property'
import detail from './detail'
import legend from './legend'
import search from './search'
import tooltip from './tooltip'
import ui from './ui'

const rootReducer = combineReducers({
  property,
  detail,
  legend,
  search,
  tooltip,
  ui,
})

export type RootState = ReturnType<typeof rootReducer>

export default rootReducer
