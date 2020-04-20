import React, { Component } from 'react'
import { Redirect } from 'react-router-dom'

import * as api from '../../../api/api'
import { registerUrl } from '../../../api/routes'

import { Container, TitleHeader, TextInput, Button } from './styles'

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
        ? <Redirect to='/login' />
        : <Container>
          <TitleHeader>Registration</TitleHeader>
          <label>
          Username:
            <TextInput
              type='text'
              name='username'
              value={this.state.register_data.username}
              onChange={this.handleChange}
            />
          </label>
          <br />
          <label>
            Email:
            <TextInput
              type='email'
              name='email'
              value={this.state.register_data.email}
              onChange={this.handleChange}
            />
          </label>
          <br />
          <label>
            Password:
            <TextInput
              type='password'
              name='password'
              value={this.state.register_data.password1}
              onChange={this.handleChange}
            />
          </label>
          <label>
            Password2:
            <TextInput
              type='password'
              name='password2'
              value={this.state.register_data.password2}
              onChange={this.handleChange}
            />
          </label>
          <label>
            My currency:
            <TextInput
              type='text'
              name='my_currency'
              value={this.state.register_data.my_currency}
              onChange={this.handleChange}
            />
          </label>
          <Button onClick={this.handleReg}>Register</Button>
        </Container>
    )
  }
}

export default RegUser
