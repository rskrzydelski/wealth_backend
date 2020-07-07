import React, { Component } from 'react'
import { TitleHeader, TextInput, Button, Label } from './styles'

class AuthForm extends Component {
  constructor (props) {
    super(props)
    this.handleChange = this.handleChange.bind(this)
    this.state = {}
  }

  handleChange (event) {
    const st = this.state
    const stateName = event.target.name
    const stateVaue = event.target.value
    st[stateName] = stateVaue
    this.setState(st)
  }

  render () {
    const { labels } = this.props
    const { btn_label } = this.props
    const { handleConfirm } = this.props
    const lbs = labels.map((lb) => {
      return (
        <>
          <Label>
            <TextInput
              type={lb.type}
              name={lb.name}
              placeholder={lb.placeholder}
              value={this.state[lb.name]}
              onChange={this.handleChange}
            />
          </Label>
          <br />
        </>
      )
    }
    )

    return (
      <>
        {lbs}
        <Button onClick={() => handleConfirm(this.state)}>{btn_label}</Button>
      </>
    )
  }
}

export default AuthForm
