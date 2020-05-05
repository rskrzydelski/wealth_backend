import styled from 'styled-components'

export const NavStyle = styled.div`
  .navbar {
    background-color: black;
  }
  .navbar-brand {
    color: white;
    font-family: 'Indie Flower', cursive;
    &:hover {
      color: gold;
    }
  }
  a, .navbar-nav .nav-link {
    color: gold;
    font-family: 'Courgette', cursive;
    &:hover {
      text-decoration: none;
      color: white;
    }
  }
  .custom-toggler.navbar-toggler {
    border-color: black;
  }
  .custom-toggler .navbar-toggler-icon {
    background-image: url("data:image/svg+xml;charset=utf8,%3Csvg viewBox='0 0 32 32' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath stroke='gold' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 8h24M4 16h24M4 24h24'/%3E%3C/svg%3E");
  }
`
