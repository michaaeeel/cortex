import { useParams } from 'react-router-dom'
import { useCampaign } from '../hooks/useCampaigns'
import Card from '../components/ui/Card'
import LoadingSpinner from '../components/ui/LoadingSpinner'

export default function CampaignDetail() {
  const { id } = useParams()
  const { data: campaign, isLoading } = useCampaign(id)

  if (isLoading) return <LoadingSpinner />

  return (
    <div>
      <h1 className="page-title">{campaign?.name || 'Campaign'}</h1>
      <div className="stats-grid">
        <Card title="Status" value={campaign?.status} />
        <Card title="Platform" value={campaign?.platform} />
        <Card title="Budget" value={campaign?.budget ? `$${campaign.budget}` : '--'} />
      </div>
      <Card>
        <h3>Metrics</h3>
        <p className="placeholder-text">Campaign metrics will appear here once data is synced.</p>
      </Card>
    </div>
  )
}
