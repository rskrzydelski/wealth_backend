const serverUrl = 'http://127.0.0.1:8000'
const apiEntry = '/api/v1/'

// authentication endpoints
export const loginUrl = () => `${serverUrl}${apiEntry}auth/jwt/create/`
export const TokenRefresh = () => `${serverUrl}${apiEntry}auth/jwt/refresh/`
export const logoutUrl = () => `${serverUrl}${apiEntry}auth/logout/`
export const registerUrl = () => `${serverUrl}${apiEntry}auth/users/`

// market endpoints
export const marketPriceUrl = () => `${serverUrl}${apiEntry}market`

// resources endpoints
export const getMetalUrl = (name, sum) => `${serverUrl}${apiEntry}resources/metals?name=${name}&sum=${sum}`
export const getMetalWalletUrl = (name) => `${serverUrl}${apiEntry}wallet/metal/${name}`
export const getCashlWalletUrl = () => `${serverUrl}${apiEntry}wallet/cash`
export const getFortuneUrl = () => `${serverUrl}${apiEntry}wallet`

// wallet endpoints
