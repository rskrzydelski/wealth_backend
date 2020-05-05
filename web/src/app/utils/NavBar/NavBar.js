import React from 'react'

import { Nav, Navbar } from 'react-bootstrap'
import { Link } from 'react-router-dom'
import { NavStyle } from './styles'

function NavBar (props) {
  return (
    <NavStyle>
      <Navbar expand='lg'>
        <Navbar.Brand href='/'>Wealthy app</Navbar.Brand>
        <Navbar.Toggle aria-controls='basic-navbar-nav' className='navbar-toggler navbar-toggler-right custom-toggler' />
        <Navbar.Collapse id='basic-navbar-nav'>
          {!props.auth ? <Nav className='ml-auto'>
            <Nav.Item>
              <Nav.Link><Link to='/login'>Login</Link></Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link><Link to='/register'>Sign up</Link></Nav.Link>
            </Nav.Item>
          </Nav>
            : <Nav className='ml-auto'>
              <Nav.Item>
                <Nav.Link><Link to='/'>Dashboard</Link></Nav.Link>
              </Nav.Item>
              <Nav.Item>
                <Nav.Link><Link to='/gold'>Gold</Link></Nav.Link>
              </Nav.Item>
              <Nav.Item>
                <Nav.Link><Link to='/silver'>Silver</Link></Nav.Link>
              </Nav.Item>
              <Nav.Item>
                <Nav.Link><Link to='/cash'>Cash</Link></Nav.Link>
              </Nav.Item>
              <Nav.Item>
                <Nav.Link><Link to='/logout'>Logout</Link></Nav.Link>
              </Nav.Item>
            </Nav>}
        </Navbar.Collapse>
      </Navbar>
    </NavStyle>
  )
}

export default NavBar
