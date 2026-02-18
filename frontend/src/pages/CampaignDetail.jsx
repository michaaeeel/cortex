import { useMutation, useQuery } from '@tanstack/react-query'
import { useParams } from 'react-router-dom'
import { useCampaign } from '../hooks/useCampaigns'
import Card from '../components/ui/Card'
import InsightsCard from '../components/ui/InsightsCard'
import LoadingSpinner from '../components/ui/LoadingSpinner'
import MetricCard from '../components/ui/MetricCard'
import { getCampaignAnalytics } from '../services/analytics'
import { getCampaignInsights } from '../services/insights'
import { fmt } from '../utils/format'
import './CampaignDetail.css'

export default function CampaignDetail() {
  const { id } = useParams()
  const { data: campaign, isLoading } = useCampaign(id)
  const { data: analytics, isLoading: analyticsLoading } = useQuery({
    queryKey: ['campaign-analytics', id],
    queryFn: () => getCampaignAnalytics(id).then((res) => res.data),
    enabled: !!id,
  })

  const insightsMutation = useMutation({
    mutationFn: () => getCampaignInsights(id).then((res) => res.data),
  })

  if (isLoading) return <LoadingSpinner />

  return (
    <div>
      <h1 className="page-title">{campaign?.name || 'Campaign'}</h1>

      <InsightsCard
        summary={insightsMutation.data?.summary}
        isLoading={insightsMutation.isPending}
        error={insightsMutation.error?.response?.data?.error || (insightsMutation.error ? 'Failed to generate insights' : null)}
        onGenerate={() => insightsMutation.mutate()}
      />

      <div className="stats-grid">
        <Card title="Status" value={campaign?.status} />
        <Card title="Platform" value={campaign?.platform} />
        <Card title="Budget" value={campaign?.budget ? `$${campaign.budget}` : '--'} />
      </div>

      <h2 className="section-title">
        Analytics
        {analytics?.period_days && (
          <span className="period-label">Last {analytics.period_days} days</span>
        )}
      </h2>

      {analyticsLoading ? (
        <LoadingSpinner />
      ) : (
        <div className="metrics-detail-grid">
          <MetricCard title="Impressions" value={fmt(analytics?.impressions)} />
          <MetricCard title="Clicks" value={fmt(analytics?.clicks)} />
          <MetricCard title="CTR" value={analytics?.ctr !== null ? `${analytics?.ctr}%` : '--'} trend={analytics?.trends?.ctr} />
          <MetricCard title="Conversions" value={fmt(analytics?.conversions)} trend={analytics?.trends?.conversion_rate} />
          <MetricCard title="Spend" value={fmt(analytics?.spend, '$')} trend={analytics?.trends?.spend} />
          <MetricCard title="Revenue" value={fmt(analytics?.revenue, '$')} trend={analytics?.trends?.revenue} />
          <MetricCard title="ROAS" value={analytics?.roas !== null ? `${analytics?.roas}x` : '--'} trend={analytics?.trends?.roas} />
          <MetricCard title="CPA" value={analytics?.cpa !== null ? fmt(analytics?.cpa, '$') : '--'} trend={analytics?.trends?.cpa} invertTrend />
          <MetricCard title="CPC" value={analytics?.cpc !== null ? fmt(analytics?.cpc, '$') : '--'} trend={analytics?.trends?.cpc} invertTrend />
        </div>
      )}
    </div>
  )
}
