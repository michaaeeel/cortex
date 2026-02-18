import './LiveBadge.css'

export default function LiveBadge({ isConnected }) {
  return (
    <span className={`live-badge ${isConnected ? 'connected' : 'disconnected'}`}>
      <span className="live-dot" />
      {isConnected ? 'Live' : 'Offline'}
    </span>
  )
}
