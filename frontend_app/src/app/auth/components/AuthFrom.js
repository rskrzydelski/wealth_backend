import React, { Component } from 'react'
import { TitleHeader, TextInput, Button } from './styles'

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
    const { title } = this.props
    const { handleConfirm } = this.props

    const lbs = labels.map((lb) => {
      return (
        <>
          <label>
            {lb.title}
            <TextInput
              type={lb.type}
              name={lb.name}
              value={this.state[lb.name]}
              onChange={this.handleChange}
            />
          </label>
          <br />
        </>
      )
    }
    )

    return (
      <>
        <TitleHeader>{title}</TitleHeader>
        {lbs}
        <Button onClick={() => handleConfirm(this.state)}>{title}</Button>
      </>
    )
  }
}

export default AuthForm
