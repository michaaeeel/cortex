import { Database } from 'lucide-react'
import Card from '../components/ui/Card'

const sourceTypes = [
  { type: 'google_ads', label: 'Google Ads', description: 'Import campaign data from Google Ads' },
  { type: 'meta_ads', label: 'Meta Ads', description: 'Import campaign data from Facebook & Instagram' },
  { type: 'google_analytics', label: 'Google Analytics', description: 'Import web analytics data' },
]

export default function DataSources() {
  return (
    <div>
      <div className="page-header">
        <h1 className="page-title">Data Sources</h1>
        <button className="btn-primary">Connect Source</button>
      </div>

      <div className="stats-grid">
        {sourceTypes.map(({ type, label, description }) => (
          <Card key={type}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 12, marginBottom: 8 }}>
              <Database size={20} style={{ color: 'var(--color-primary)' }} />
              <h3 style={{ fontSize: '1rem', fontWeight: 600 }}>{label}</h3>
            </div>
            <p style={{ color: 'var(--color-text-muted)', fontSize: '0.85rem' }}>{description}</p>
            <button
              style={{
                marginTop: 16,
                padding: '6px 14px',
                border: '1px solid var(--color-border)',
                borderRadius: 'var(--radius)',
                background: 'none',
                fontSize: '0.85rem',
              }}
            >
              Connect
            </button>
          </Card>
        ))}
      </div>
    </div>
  )
}
