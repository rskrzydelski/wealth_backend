import React, { Component } from 'react'

import { connect } from 'react-redux'
import { BrowserRouter as Router, Route, Switch, Redirect } from 'react-router-dom'

import NavBar from '../NavBar/NavBar'

import LoginUser from '../../auth/components/LoginUser'
import LogoutUser from '../../auth/components/LogoutUser'
import RegUser from '../../auth/components/RegUser'

import Dashboard from '../../main/Dashboard'
import NotFound from '../../main/NotFound'

import Gold from '../../resources/components/Gold'
import Silver from '../../resources/components/Silver'
import Cash from '../../resources/components/Cash'

const PrivateRoutes = ({ component: Component, auth }) => (
  <Route render={props => auth === true
    ? <Component auth={auth} {...props} />
    : <Redirect to={{ pathname: '/register' }} />}
  />
)

class Routes extends Component {
  render () {
    return (
      <>
        <Router>
          <NavBar auth={this.props.isAuth} />
          <Switch>
            <Route path='/login' render={(props) => (<LoginUser {...props} />)} />
            <Route path='/register' render={(props) => (<RegUser {...props} />)} />
            <Route path='/logout' render={(props) => (<LogoutUser {...props} />)} />

            <PrivateRoutes exact path='/' auth={this.props.isAuth} component={Dashboard} />
            <PrivateRoutes exact path='/gold' auth={this.props.isAuth} component={Gold} />
            <PrivateRoutes exact path='/silver' auth={this.props.isAuth} component={Silver} />
            <PrivateRoutes exact path='/cash' auth={this.props.isAuth} component={Cash} />
            <Route component={NotFound} />
          </Switch>
        </Router>
      </>
    )
  }
}

function mapStateToProps (state) {
  const { authentication } = state
  return { isAuth: authentication.isAuthenticated }
}

export default connect(mapStateToProps, null)(Routes)
