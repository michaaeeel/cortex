import { Link } from 'react-router-dom'
import { useCampaigns } from '../hooks/useCampaigns'
import LoadingSpinner from '../components/ui/LoadingSpinner'
import './Campaigns.css'

const statusColors = {
  draft: '#64748b',
  active: '#10b981',
  paused: '#f59e0b',
  completed: '#6366f1',
}

export default function Campaigns() {
  const { data, isLoading } = useCampaigns()

  return (
    <div>
      <div className="page-header">
        <h1 className="page-title">Campaigns</h1>
        <button className="btn-primary">New Campaign</button>
      </div>

      {isLoading ? (
        <LoadingSpinner />
      ) : (
        <div className="table-container">
          <table className="data-table">
            <thead>
              <tr>
                <th>Name</th>
                <th>Status</th>
                <th>Platform</th>
                <th>Budget</th>
                <th>Created</th>
              </tr>
            </thead>
            <tbody>
              {data?.results?.length ? (
                data.results.map((campaign) => (
                  <tr key={campaign.id}>
                    <td>
                      <Link to={`/campaigns/${campaign.id}`}>{campaign.name}</Link>
                    </td>
                    <td>
                      <span
                        className="status-badge"
                        style={{ backgroundColor: statusColors[campaign.status] }}
                      >
                        {campaign.status}
                      </span>
                    </td>
                    <td>{campaign.platform}</td>
                    <td>{campaign.budget ? `$${campaign.budget}` : '--'}</td>
                    <td>{new Date(campaign.created_at).toLocaleDateString()}</td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan={5} className="empty-state">No campaigns yet</td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      )}
    </div>
  )
}
