import { Sparkles } from 'lucide-react'
import './InsightsCard.css'

export default function InsightsCard({ summary, isLoading, error, onGenerate }) {
  return (
    <div className="insights-card">
      <div className="insights-header">
        <Sparkles size={20} className="insights-icon" />
        <h3>AI Insights</h3>
      </div>
      {error && (
        <p className="insights-error">{error}</p>
      )}
      {isLoading ? (
        <div className="insights-loading">
          <div className="insights-pulse" />
          <p>Generating insights...</p>
        </div>
      ) : summary ? (
        <p className="insights-text">{summary}</p>
      ) : (
        <div className="insights-empty">
          <p>Get AI-powered analysis of your performance data.</p>
          <button className="insights-btn" onClick={onGenerate}>
            <Sparkles size={16} />
            Generate Insights
          </button>
        </div>
      )}
    </div>
  )
}
