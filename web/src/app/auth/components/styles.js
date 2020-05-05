import styled from 'styled-components'

export const TitleHeader = styled.h4`
  text-align: center;
  margin-right: 20px;
`

export const Container = styled.div`
  background: #2b2e39;
  margin: 0 auto;
  width: 80%;
  max-width: 600px;
  padding: 14px;
  border-radius: 14px;
  margin-top: 14px;
`

export const TextInput = styled.input`
  padding: 5px;
  font-size: .7em;
  background: #232632;
  color: #d3d4d6;
  width: 100%;
  margin-right: 7px;
  margin-bottom: 10px;
  border: 0px;
  -webkit-apperance: none;
`

export const Button = styled.button`
  background: #232632;
  color: #00a7fa;
  width: 30%;
  height: 32px;
  font-size: 0.9em;
  border: 2px;
  margin-top: 10px;
  margin-bottom: 10px;
  margin-right: 10px;
  margin-left: 10px;
  display: block;
  max-width: 300px;
  margin: auto;
  justify-content: center;
  align-items: center;
  &:hover { background: #555; }
`
