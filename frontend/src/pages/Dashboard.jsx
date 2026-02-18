import { useMutation, useQuery } from '@tanstack/react-query'
import { DollarSign, Eye, Megaphone, MousePointerClick, TrendingUp } from 'lucide-react'
import { useEffect, useState } from 'react'
import InsightsCard from '../components/ui/InsightsCard'
import LiveBadge from '../components/ui/LiveBadge'
import LoadingSpinner from '../components/ui/LoadingSpinner'
import MetricCard from '../components/ui/MetricCard'
import useWebSocket from '../hooks/useWebSocket'
import { getDashboardAnalytics } from '../services/analytics'
import { getDashboardInsights } from '../services/insights'
import { fmt } from '../utils/format'
import './Dashboard.css'

export default function Dashboard() {
  const { data, isLoading } = useQuery({
    queryKey: ['dashboard-analytics'],
    queryFn: () => getDashboardAnalytics().then((res) => res.data),
  })

  const { isConnected, lastMessage } = useWebSocket()
  const [liveMetrics, setLiveMetrics] = useState({})

  useEffect(() => {
    if (!lastMessage) return
    setLiveMetrics((prev) => ({
      ...prev,
      [lastMessage.campaign_id]: lastMessage,
    }))
  }, [lastMessage])

  const liveTotals = Object.values(liveMetrics).reduce(
    (acc, m) => ({
      impressions: acc.impressions + (m.impressions || 0),
      clicks: acc.clicks + (m.clicks || 0),
      conversions: acc.conversions + (m.conversions || 0),
      spend: acc.spend + (m.spend || 0),
      revenue: acc.revenue + (m.revenue || 0),
    }),
    { impressions: 0, clicks: 0, conversions: 0, spend: 0, revenue: 0 }
  )

  const hasLiveData = Object.keys(liveMetrics).length > 0
  const impressions = hasLiveData ? liveTotals.impressions : data?.impressions
  const clicks = hasLiveData ? liveTotals.clicks : data?.clicks
  const spend = hasLiveData ? liveTotals.spend : data?.spend
  const revenue = hasLiveData ? liveTotals.revenue : data?.revenue
  const conversions = hasLiveData ? liveTotals.conversions : data?.conversions
  const ctr = impressions ? ((clicks / impressions) * 100).toFixed(2) : null
  const roas = spend ? (revenue / spend).toFixed(2) : null
  const cpa = conversions ? (spend / conversions).toFixed(2) : null

  const insightsMutation = useMutation({
    mutationFn: (dashboardData) =>
      getDashboardInsights(dashboardData).then((res) => res.data),
  })

  if (isLoading) return <LoadingSpinner />

  return (
    <div>
      <div className="page-header">
        <h1 className="page-title">Dashboard</h1>
        <LiveBadge isConnected={isConnected} />
      </div>

      <InsightsCard
        summary={insightsMutation.data?.summary}
        isLoading={insightsMutation.isPending}
        error={insightsMutation.error?.response?.data?.error || (insightsMutation.error ? 'Failed to generate insights' : null)}
        onGenerate={() => data && insightsMutation.mutate(data)}
      />

      <div className="stats-grid">
        <MetricCard title="Active Campaigns" value={data ? `${data.active_campaigns}` : '--'}>
          <div className="stat-icon" style={{ color: '#4f46e5' }}><Megaphone size={24} /></div>
        </MetricCard>
        <MetricCard title="Total Spend" value={fmt(spend, '$')} trend={data?.trends?.spend}>
          <div className="stat-icon" style={{ color: '#10b981' }}><DollarSign size={24} /></div>
        </MetricCard>
        <MetricCard title="ROAS" value={roas !== null ? `${roas}x` : '--'}>
          <div className="stat-icon" style={{ color: '#f59e0b' }}><TrendingUp size={24} /></div>
        </MetricCard>
        <MetricCard title="Total Impressions" value={fmt(impressions)} trend={data?.trends?.impressions}>
          <div className="stat-icon" style={{ color: '#6366f1' }}><Eye size={24} /></div>
        </MetricCard>
      </div>

      <div className="metrics-grid">
        <MetricCard title="Click-Through Rate" value={ctr !== null ? `${ctr}%` : '--'} trend={data?.trends?.clicks}>
          <div className="stat-icon" style={{ color: '#8b5cf6' }}><MousePointerClick size={24} /></div>
        </MetricCard>
        <MetricCard title="Cost Per Acquisition" value={cpa !== null ? fmt(parseFloat(cpa), '$') : '--'} />
        <MetricCard title="Revenue" value={fmt(revenue, '$')} trend={data?.trends?.revenue} />
      </div>

      {hasLiveData && (
        <div className="live-feed">
          <h3 className="section-title">Live Feed</h3>
          <div className="table-container">
            <table className="data-table">
              <thead>
                <tr>
                  <th>Campaign</th>
                  <th>Impressions</th>
                  <th>Clicks</th>
                  <th>Conversions</th>
                  <th>Spend</th>
                  <th>Revenue</th>
                  <th>CTR</th>
                  <th>ROAS</th>
                </tr>
              </thead>
              <tbody>
                {Object.entries(liveMetrics).map(([id, m]) => (
                  <tr key={id}>
                    <td>Campaign #{id}</td>
                    <td>{fmt(m.impressions)}</td>
                    <td>{fmt(m.clicks)}</td>
                    <td>{fmt(m.conversions)}</td>
                    <td>{fmt(m.spend, '$')}</td>
                    <td>{fmt(m.revenue, '$')}</td>
                    <td>{m.ctr != null ? `${m.ctr.toFixed(2)}%` : '--'}</td>
                    <td>{m.roas != null ? `${m.roas.toFixed(2)}x` : '--'}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </div>
  )
}
