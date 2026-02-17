import api from './api'

export const getReports = (params) => api.get('/reports/', { params })
export const getReport = (id) => api.get(`/reports/${id}/`)
export const createReport = (data) => api.post('/reports/', data)
export const generateReport = (id) => api.post(`/reports/${id}/generate/`)
