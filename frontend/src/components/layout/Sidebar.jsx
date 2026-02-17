import {
  BarChart3,
  Database,
  FileText,
  LayoutDashboard,
  Megaphone,
  Settings,
} from 'lucide-react'
import { NavLink } from 'react-router-dom'
import './Sidebar.css'

const navItems = [
  { to: '/', icon: LayoutDashboard, label: 'Dashboard' },
  { to: '/campaigns', icon: Megaphone, label: 'Campaigns' },
  { to: '/reports', icon: FileText, label: 'Reports' },
  { to: '/data-sources', icon: Database, label: 'Data Sources' },
  { to: '/settings', icon: Settings, label: 'Settings' },
]

export default function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="sidebar-brand">
        <BarChart3 size={28} />
        <span>Cortex</span>
      </div>
      <nav className="sidebar-nav">
        {navItems.map(({ to, icon: Icon, label }) => (
          <NavLink
            key={to}
            to={to}
            end={to === '/'}
            className={({ isActive }) =>
              `sidebar-link ${isActive ? 'active' : ''}`
            }
          >
            <Icon size={20} />
            <span>{label}</span>
          </NavLink>
        ))}
      </nav>
    </aside>
  )
}
