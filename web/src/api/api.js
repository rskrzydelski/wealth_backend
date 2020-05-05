const apiCall = (url, method, body, resolve, reject) =>
  fetch(url, {
    method: method,
    headers: {
      'Content-Type': 'application/json; charset=utf-8'
    },
    body: JSON.stringify(body)
  }).then(response => {
    response.json()
      .then(json => resolve(json))
  }).catch( error => console.error(error))

export const get = url =>
  new Promise(
    (resolve, reject) => {
      fetch(url, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json; charset=utf-8',
          'Authorization': 'JWT ' + localStorage.token
        }
      })
        .then(response => response.json())
        .then(json => resolve(json))
        .catch( error => console.error(error))
    }
  )

export const post = (url, body) =>
  new Promise(
    (resolve, reject) => apiCall(url, 'POST', body, resolve, reject)
  )

export const put = (url, body) =>
  new Promise(
    (resolve, reject) => apiCall(url, 'PUT', body, resolve, reject)
  )

export const del = url =>
  new Promise(
    (resolve, reject) => {
      fetch(url, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json; charset=utf-8'
        }
      }).then(response => {
        if (response.ok) {
          resolve(response)
        } else {
          reject(response)
        }
      })
    }
  )
