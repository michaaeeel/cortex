import { useReports } from '../hooks/useReports'
import LoadingSpinner from '../components/ui/LoadingSpinner'

const statusColors = {
  pending: '#64748b',
  processing: '#f59e0b',
  completed: '#10b981',
  failed: '#ef4444',
}

export default function Reports() {
  const { data, isLoading } = useReports()

  return (
    <div>
      <div className="page-header">
        <h1 className="page-title">Reports</h1>
        <button className="btn-primary">Generate Report</button>
      </div>

      {isLoading ? (
        <LoadingSpinner />
      ) : (
        <div className="table-container">
          <table className="data-table">
            <thead>
              <tr>
                <th>Title</th>
                <th>Type</th>
                <th>Status</th>
                <th>Created</th>
              </tr>
            </thead>
            <tbody>
              {data?.results?.length ? (
                data.results.map((report) => (
                  <tr key={report.id}>
                    <td>{report.title}</td>
                    <td style={{ textTransform: 'capitalize' }}>{report.report_type}</td>
                    <td>
                      <span
                        className="status-badge"
                        style={{ backgroundColor: statusColors[report.status] }}
                      >
                        {report.status}
                      </span>
                    </td>
                    <td>{new Date(report.created_at).toLocaleDateString()}</td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan={4} className="empty-state">No reports generated yet</td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      )}
    </div>
  )
}
