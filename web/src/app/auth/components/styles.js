import styled from 'styled-components'

export const Grid = styled.div`

`

export const Row = styled.div`
  display: flex;
`

export const Col = styled.div`
  flex: ${(props) => props.size};
`

export const Form = styled.div`
  background: #2b2e39;
  text-align: center;
  border-radius: 14px;
  margin-top: 20px;
  margin-bottom: 20px;
  margin-left: 20px;
  margin-right: 10px;
`
export const Welcome = styled.div`
  background: #111519;
  margin-right: 10px;
  margin-top: 50px;
  margin-left: 50px;
`

export const TitleHeader = styled.h1`
  font-size: 20px;
`
export const Label = styled.label`
  margin-top: 10px;
  font-size: 14px;
`

export const TextInput = styled.input`
  padding: 5px;
  border-radius: 10px;
  font-size: 12px;
  background: #232632;
  color: #d3d4d6;
  width: 100%;
  margin-right: 7px;
  margin-bottom: 10px;
  text-algin: center;
`

export const Button = styled.button`
  background: #232632;
  border-radius: 10px;
  color: gold;
  width: 30%;
  height: 32px;
  font-size: 0.9em;
  margin: 10px auto;
  justify-content: center;
  align-items: center;
  border: 1px solid gold;
  &:hover { background: #555; }
`

export const Container = styled.div`

`

export const Paragraf = styled.p`
  font-size: 15px;
  font-family: 'Courgette', cursive;
`
