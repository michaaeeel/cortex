export function fmt(value, prefix = '') {
  if (value === null || value === undefined) return '--'
  if (typeof value === 'number') {
    if (value >= 1_000_000) return `${prefix}${(value / 1_000_000).toFixed(1)}M`
    if (value >= 1_000) return `${prefix}${(value / 1_000).toFixed(1)}K`
    return `${prefix}${value.toLocaleString()}`
  }
  return `${prefix}${value}`
}
