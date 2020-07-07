import React, { Component } from 'react'
import { Redirect } from 'react-router-dom'

import * as api from '../../../api/api'
import { registerUrl } from '../../../api/routes'
import { registerLabels } from './labels'
import AuthForm from './AuthFrom'

import { Row, Col, Form, Welcome, Paragraf } from './styles'

class RegUser extends Component {
  constructor (props) {
    super(props)
    this.handleReg = this.handleReg.bind(this)
    this.handleChange = this.handleChange.bind(this)
    this.state = {
      register_data: { username: '', email: '', password: '', password2: '', my_currency: '' },
      register_success: false
    }
  }

  async handleReg (event) {
    const regUser = await api.post(registerUrl(), this.state.register_data)
    regUser.key !== undefined ? alert('User registered successfully') : alert('Register error')
    if (regUser.key !== undefined) {
      this.setState({
        register_success: true
      })
      localStorage.setItem('my_currency', this.state.register_data.my_currency)
    }
    this.setState({
      register_data: { username: '', email: '', password: '', password2: '', my_currency: '' }
    })
  }

  handleChange (event) {
    const r = this.state.register_data
    r[event.target.name] = event.target.value
    this.setState({ register_data: r })
  }

  render () {
    return (
      this.state.register_success === true
        ? <Redirect to='/login' /> :
        <Row>
          <Col size={1}>
            <Form>
              <AuthForm btn_label='Register' labels={registerLabels} handleConfirm={this.onHandleLogin} />
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

export default RegUser
