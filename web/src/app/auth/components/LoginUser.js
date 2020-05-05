import React, { Component } from 'react'
import { connect } from 'react-redux'

import * as api from '../../../api/api'
import { loginUrl } from '../../../api/routes'
import * as actions from '../duck/actions'

import { Container } from './styles'
import { loginLabels } from './labels'
import AuthForm from './AuthFrom'

class LoginUser extends Component {
  constructor (props) {
    super(props)
    this.onHandleLogin = this.onHandleLogin.bind(this)
  }

  async onHandleLogin (value) {
    const { history } = this.props
    const res = await api.post(loginUrl(), value)
    console.log(res)
    if (Boolean(res.token)) {
      localStorage.setItem('token', res.token)
      localStorage.setItem('username', res.user.username)
      localStorage.setItem('email', res.user.email)
      this.props.loginSuccess()
      history.push('/')
    } else if (Boolean(res.non_field_errors)) {
      localStorage.clear()
      this.props.loginFailure()
      alert(res.non_field_errors)
    }
  }

  render () {
    return (
      <Container>
        <AuthForm title='Login' labels={loginLabels} handleConfirm={this.onHandleLogin} />
      </Container>
    )
  }
}

function mapStateToProps (state) {
  return {

  }
}

function mapDispatchToProps (dispatch) {
  return {
    loginSuccess: () => dispatch(actions.loginSuccess()),
    loginFailure: () => dispatch(actions.loginFailure())
  }
}

export default connect(null, mapDispatchToProps)(LoginUser)
