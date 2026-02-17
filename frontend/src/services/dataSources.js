import api from './api'

export const getDataSources = (params) => api.get('/data-sources/', { params })
export const getDataSource = (id) => api.get(`/data-sources/${id}/`)
export const createDataSource = (data) => api.post('/data-sources/', data)
export const deleteDataSource = (id) => api.delete(`/data-sources/${id}/`)
