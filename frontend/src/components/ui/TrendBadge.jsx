export default function TrendBadge({ trend }) {
  if (!trend) return null
  const { direction, change_pct } = trend
  if (direction === 'neutral') return <span className="trend neutral">--</span>
  const arrow = direction === 'up' ? '\u2191' : '\u2193'
  const cls = direction === 'up' ? 'trend up' : 'trend down'
  return <span className={cls}>{arrow} {Math.abs(change_pct)}%</span>
}
