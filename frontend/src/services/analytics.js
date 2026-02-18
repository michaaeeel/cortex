import api from './api'

export const getDashboardAnalytics = (days = 30) =>
  api.get('/analytics/metrics/dashboard/', { params: { days } })

export const getCampaignAnalytics = (campaignId, days = 30) =>
  api.get(`/campaigns/${campaignId}/analytics/`, { params: { days } })
