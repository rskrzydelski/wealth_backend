import React, { Component } from 'react'
import { connect } from 'react-redux'

import * as api from '../../../api/api'
import { loginUrl } from '../../../api/routes'
import * as actions from '../duck/actions'

import { Row, Col, Form, Welcome, Paragraf } from './styles'
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
      <Row>
        <Col size={1}>
          <Form>
            <AuthForm btn_label='Login' labels={loginLabels} handleConfirm={this.onHandleLogin} />
          </Form>
        </Col>
        <Col size={3}>
          <Welcome>
            <Paragraf>Wealth is application for store resources such as gold, silver, cash.</Paragraf>
            <Paragraf>You can add your gold, silver and cash, see current price, see how money you spend</Paragraf>
            <Paragraf>on particular resource or on all resources and finally see your profit or your lost.</Paragraf>
            <Paragraf>Currently you can choose following currencies: PLN, USD, CHF, EUR.</Paragraf>
          </Welcome>
        </Col>
      </Row>
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
