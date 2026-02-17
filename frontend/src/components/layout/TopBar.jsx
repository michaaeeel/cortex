import { Bell } from 'lucide-react'
import './TopBar.css'

export default function TopBar() {
  return (
    <header className="topbar">
      <h2 className="topbar-title">Campaign Intelligence</h2>
      <div className="topbar-actions">
        <button className="topbar-btn" title="Notifications">
          <Bell size={20} />
        </button>
      </div>
    </header>
  )
}
