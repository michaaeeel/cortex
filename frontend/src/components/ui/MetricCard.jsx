import Card from './Card'
import TrendBadge from './TrendBadge'

export default function MetricCard({ title, value, trend, invertTrend = false, children }) {
  const displayTrend = trend
    ? invertTrend
      ? { ...trend, direction: trend.direction === 'up' ? 'down' : trend.direction === 'down' ? 'up' : 'neutral' }
      : trend
    : null

  return (
    <Card title={title} value={value}>
      {children}
      {displayTrend && (
        <div className="stat-trend">
          <TrendBadge trend={displayTrend} />
          <span className="trend-label">vs prev period</span>
        </div>
      )}
    </Card>
  )
}
