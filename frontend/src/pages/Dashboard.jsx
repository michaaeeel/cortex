import { Megaphone, DollarSign, TrendingUp, Eye } from 'lucide-react'
import Card from '../components/ui/Card'
import './Dashboard.css'

const stats = [
  { title: 'Active Campaigns', value: '--', icon: Megaphone, color: '#4f46e5' },
  { title: 'Total Spend', value: '--', icon: DollarSign, color: '#10b981' },
  { title: 'Avg. ROAS', value: '--', icon: TrendingUp, color: '#f59e0b' },
  { title: 'Total Impressions', value: '--', icon: Eye, color: '#6366f1' },
]

export default function Dashboard() {
  return (
    <div>
      <h1 className="page-title">Dashboard</h1>
      <div className="stats-grid">
        {stats.map(({ title, value, icon: Icon, color }) => (
          <Card key={title} title={title} value={value}>
            <div className="stat-icon" style={{ color }}>
              <Icon size={24} />
            </div>
          </Card>
        ))}
      </div>
      <div className="dashboard-placeholder">
        <Card>
          <h3>Performance Overview</h3>
          <p className="placeholder-text">Charts and analytics will appear here once data sources are connected.</p>
        </Card>
      </div>
    </div>
  )
}
