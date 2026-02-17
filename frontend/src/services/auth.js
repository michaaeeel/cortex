import api from './api'

export const login = (username, password) =>
  api.post('/auth/token/', { username, password })

export const refreshToken = (refresh) =>
  api.post('/auth/token/refresh/', { refresh })
