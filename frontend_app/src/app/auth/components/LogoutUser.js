import React, { Component } from 'react'
import { Redirect } from 'react-router-dom'
import { connect } from 'react-redux'

import * as api from '../../../api/api'
import { logoutUrl } from '../../../api/routes'
import * as actions from '../duck/actions'

class LogoutUser extends Component {
  constructor (props) {
    super(props)
    this.handleLogout = this.handleLogout.bind(this)
  }

  async handleLogout () {
    this.props.logout()
    localStorage.clear()
    const status = await api.post(logoutUrl(), {})
  }

  componentDidMount () {
    this.handleLogout()
  }

  render () {
    return (
      <div>
        <Redirect to='/login' />
      </div>
    )
  }
}

function mapDispatchToProps (dispatch) {
  return {
    logout: () => dispatch(actions.logout())
  }
}

export default connect(null, mapDispatchToProps)(LogoutUser)
