import { Bell, LogOut } from 'lucide-react'
import useAuth from '../../hooks/useAuth'
import './TopBar.css'

export default function TopBar() {
  const { user, logout } = useAuth()

  return (
    <header className="topbar">
      <h2 className="topbar-title">Campaign Intelligence</h2>
      <div className="topbar-actions">
        <button className="topbar-btn" title="Notifications">
          <Bell size={20} />
        </button>
        <span className="topbar-user">{user?.username ?? 'User'}</span>
        <button className="topbar-btn" title="Sign out" onClick={logout}>
          <LogOut size={20} />
        </button>
      </div>
    </header>
  )
}
