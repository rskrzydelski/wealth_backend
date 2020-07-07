import React, { Component } from 'react'

import Routes from './app/utils/Routes/routes'
import Bottom from './app/main/Bottom'

class App extends Component {
  render () {
    return (
      <>        
        <Routes />
        <Bottom />
      </>
    )
  }
}

export default App
