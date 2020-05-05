import React, { Component } from 'react'
import { Card } from 'react-bootstrap'
import styled from 'styled-components'

import gold_ico from '../../static/images/gold_ico.png'
import silver_ico from '../../static/images/silver_ico.png'
import switzland_ico from '../../static/images/switzerland-ico.png'
import dollar_ico from '../../static/images/dollar_ico.png'
import euro_ico from '../../static/images/euro-ico.png'

import { marketPriceUrl } from '../../../api/routes'
import * as api from '../../../api/api'

const CardMarketStyle = styled.div`
  padding-top: 20px;
  padding-bottom: 20px;
  padding-right: 20px;
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
    font-size: 13px;
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

class MarketPrices extends Component {
  constructor (props) {
    super(props)
    this.getMarketData = this.getMarketData.bind(this)
    this.state = {
      trigger_market_data_time_s: 10,
      gold_price: '...',
      silver_price: '...',
      usdpln: '...',
      eurpln: '...',
      chfpln: '...'
    }
  }

  componentDidMount () {
    const timer = this.state.trigger_market_data_time_s * 1000
    this.myInterval = setInterval(this.getMarketData, timer)
  }

  async getMarketData () {
    const data = await api.get(marketPriceUrl())
    if (data.gold === 0 || data.silver === 0) {
      this.setState({
        gold_price: '...',
        silver_price: '...',
        usdpln: '...',
        eurpln: '...',
        chfpln: '...'
      })
    } else {
      this.setState({
        gold_price: data.gold,
        silver_price: data.silver,
        usdpln: data.usdpln,
        eurpln: data.eurpln,
        chfpln: data.chfpln
      })
    }
  }

  render () {
    const currencyLeadItems = {
      usd: 'USD',
      chf: 'CHF',
      eur: 'EUR'
    }
    return (
      <CardMarketStyle>
        <Card className="text-center">
          <Card.Body>
            <Card.Title><img src={gold_ico} alt='' style={{ height: '40px' }} /> <span style={{ color: 'gold' }}>{this.state.gold_price}</span> <span style={{color: '#68e25f' }}>$</span></Card.Title>
          </Card.Body>
        </Card>
        <Card className="text-center">
          <Card.Body>
            <Card.Title><img src={silver_ico} alt='' style={{ height: '50px' }} /> <span style={{ color: '#d5dde0' }}>{this.state.silver_price}</span> <span style={{ color: '#68e25f' }}>$</span></Card.Title>
          </Card.Body>
        </Card>
        {localStorage.my_currency !== 'USD'
          ? <Card className="text-center">
            <Card.Body>
              <Card.Title><img src={dollar_ico} alt='' style={{ height: '30px' }} /><span>{currencyLeadItems.usd}</span>/<span>{localStorage.my_currency}</span> <span style={{ color: '#68e25f'}}>{this.state.usdpln}</span> <span>{localStorage.my_currency}</span></Card.Title>
            </Card.Body>
          </Card>
          : ''}
        {localStorage.my_currency !== 'CHF'
          ? <Card className="text-center">
            <Card.Body>
              <Card.Title><img src={switzland_ico} alt='' style={{ height: '20px' }} /> {currencyLeadItems.chf}/{localStorage.my_currency} <span style={{ color: 'red' }}>{this.state.chfpln}</span> {localStorage.my_currency}</Card.Title>
            </Card.Body>
          </Card>
          : ''}
        {localStorage.my_currency !== 'EUR'
          ? <Card className="text-center">
            <Card.Body>
              <Card.Title><img src={euro_ico} alt='' style={{ height: '28px' }} /> {currencyLeadItems.eur}/{localStorage.my_currency} <span style={{ color: '#00b1e2' }}>{this.state.eurpln}</span> {localStorage.my_currency}</Card.Title>
            </Card.Body>
          </Card>
          : ''}
      </CardMarketStyle>
    )
  }
}

export default MarketPrices
