import api from './api'

export const getCampaignInsights = (campaignId, days = 30) =>
  api.post(`/campaigns/${campaignId}/insights/`, null, { params: { days } })

export const getDashboardInsights = (dashboardData) =>
  api.post('/analytics/metrics/dashboard/insights/', dashboardData)
