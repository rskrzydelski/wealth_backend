const serverUrl = 'http://127.0.0.1:8000'
const apiEntry = '/api/v1/'

export const loginUrl = () => `${serverUrl}${apiEntry}auth/login/`
export const logoutUrl = () => `${serverUrl}${apiEntry}auth/logout/`
export const registerUrl = () => `${serverUrl}${apiEntry}auth/registration/`

export const marketPriceUrl = () => `${serverUrl}${apiEntry}market`

// dashboard endpoints
export const getMetalUrl = (name, sum) => `${serverUrl}${apiEntry}resources/metals?name=${name}&sum=${sum}`
export const getMetalWalletUrl = (name) => `${serverUrl}${apiEntry}wallet/metal/${name}`
export const getCashlWalletUrl = () => `${serverUrl}${apiEntry}wallet/cash`
export const getFortuneUrl = () => `${serverUrl}${apiEntry}wallet`
