import React, { Component } from 'react'
import { Card, CardDeck } from 'react-bootstrap'
import styled from 'styled-components'

import MarketPrices from '../market/components/MarketPrices'
import gold_bars from '../static/images/gold_bars.jpg'
import silver_bars from '../static/images/silver_bars.jpg'
import my_cash from '../static/images/my_cash.jpeg'
import dollar from '../static/images/dollar.jpg'
import euro from '../static/images/euro.jpg'
import franc from '../static/images/franc.jpg'
import { getMetalUrl, getMetalWalletUrl, getCashlWalletUrl, getFortuneUrl } from '../../api/routes'
import * as api from '../../api/api'

const CardMarketStyle = styled.div`
  padding-top: 20px;
  padding-bottom: 20px;
  padding-right: 20px;
  padding-left: 20px;
  display: flex;
  flex-direction: row;
  justify-content: space-around;

  .card {
    display: flex;
    flex-direction: column;
    background: #2b353f;
    margin-left: 10px;
    margin-right: 10px;
  }
  .card-title {
    font-size: 20px;
  }
  .card-text {
    font-size: 15px;
  }
  .card-body {
    background: #2b353f;
    -ms-flex: 1 1 auto;
    flex: 1 1 auto;
    padding: 0.7rem;
    font-size: 10px;
    font-family: 'Courgette', cursive;
  }
`

const CardFortuneStyle = styled.div`
  color: white;
  padding-top: 20px;
  padding-bottom: 20px;
  padding-right: 20px;
  padding-left: 20px;

  .card-body {
    background: #2b353f;
    font-family: 'Courgette', cursive;
  }
  .card-footer {
    background: #2b353f;
  }
`

class Dashboard extends Component {
  constructor (props) {
    super(props)
    this.getMetalData = this.getMetalData.bind(this)
    this.state = {
      gold: {
        total_amount: '...',
        total_cash_spend: '...',
        unit: 'oz',
        total_cash: '...',
        profit: '...'
      },
      silver: {
        total_amount: '...',
        total_cash_spend: '...',
        unit: 'oz',
        total_cash: '...',
        profit: '...'
      },
      cash: {
        my_cash: '...'
      },
      fortune: {
        my_fortune: '...'
      }
    }
  }

  async getMetalData () {
    const gold = await api.get(getMetalUrl('gold', 'true'))
    const goldSum = await api.get(getMetalWalletUrl('gold'))
    const silver = await api.get(getMetalUrl('silver', 'true'))
    const silverSum = await api.get(getMetalWalletUrl('silver'))
    const cashSum = await api.get(getCashlWalletUrl())
    const fortune = await api.get(getFortuneUrl())

    const metals = {
      gold: {
        total_amount: gold[0].total_amount,
        total_cash_spend: gold[0].total_cash_spend,
        unit: gold[0].unit,
        total_cash: goldSum.total_cash,
        profit: goldSum.profit
      },
      silver: {
        total_amount: silver[0].total_amount,
        total_cash_spend: silver[0].total_cash_spend,
        unit: silver[0].unit,
        total_cash: silverSum.total_cash,
        profit: silverSum.profit
      }
    }
    const myCash = cashSum.cash
    const f = fortune.my_fortune
    this.setState({
      gold: metals.gold,
      silver: metals.silver,
      my_cash: myCash,
      my_fortune: f
    })
  }

  componentDidMount () {
    const timer = 10 * 1000
    this.myInterval = setInterval(this.getMetalData, timer)
  }

  render () {
    return (
      <>
        <MarketPrices />
        <CardMarketStyle>
          <CardDeck>
            <Card>
              <Card.Img variant='top' src={gold_bars} style={{ height: '180px' }} />
              <Card.Body>
                <Card.Title>My gold</Card.Title>
                <Card.Text>
                Amount: {this.state.gold.total_amount} {this.state.gold.unit}<br />
                Cash spend: {this.state.gold.total_cash_spend} {localStorage.my_currency}<br />
                Value: {this.state.gold.total_cash} {localStorage.my_currency}<br />
                Profit: {this.state.gold.profit} {localStorage.my_currency}<br />
                </Card.Text>
              </Card.Body>
            </Card>
            <Card>
              <Card.Img variant='top' src={silver_bars} style={{ height: '180px' }} />
              <Card.Body>
                <Card.Title>My silver</Card.Title>
                <Card.Text>
                Amount: {this.state.silver.total_amount} {this.state.silver.unit}<br />
                Cash spend: {this.state.silver.total_cash_spend} {localStorage.my_currency}<br />
                Value: {this.state.silver.total_cash} {localStorage.my_currency}<br />
                Profit: {this.state.silver.profit} {localStorage.my_currency}<br />
                </Card.Text>
              </Card.Body>
            </Card>
            <Card>
              <Card.Img variant='top' src={my_cash} style={{ height: '180px' }} />
              <Card.Body>
                <Card.Title>My cash</Card.Title>
                <Card.Text>
                My cash: {this.state.my_cash} {localStorage.my_currency}<br />
                </Card.Text>
              </Card.Body>
            </Card>
            <Card>
              <Card.Img variant='top' src={dollar} style={{ height: '180px' }} />
              <Card.Body>
                <Card.Title>My dollar</Card.Title>
                <Card.Text>
                My USD: 0 USD<br />
                </Card.Text>
              </Card.Body>
            </Card>
            <Card>
              <Card.Img variant='top' src={euro} style={{ height: '180px' }} />
              <Card.Body>
                <Card.Title>My euro</Card.Title>
                <Card.Text>
                My EUR: 0 PLN<br />
                </Card.Text>
              </Card.Body>
            </Card>
            <Card>
              <Card.Img variant='top' src={franc} style={{ height: '180px' }} />
              <Card.Body>
                <Card.Title>My franc</Card.Title>
                <Card.Text>
                My CHF: 0 PLN<br />
                </Card.Text>
              </Card.Body>
            </Card>
          </CardDeck>
        </CardMarketStyle>
        <CardFortuneStyle>
          <Card className='text-center'>
            <Card.Body>
              <Card.Title>My fortune {this.state.my_fortune} {localStorage.my_currency}</Card.Title>
            </Card.Body>
            <Card.Footer className='text-muted'></Card.Footer>
          </Card>
        </CardFortuneStyle>
      </>
    )
  }
}

export default Dashboard
