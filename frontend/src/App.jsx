import { Navigate, Outlet, Route, Routes } from 'react-router-dom'
import AppLayout from './components/layout/AppLayout'
import CampaignDetail from './pages/CampaignDetail'
import Campaigns from './pages/Campaigns'
import Dashboard from './pages/Dashboard'
import DataSources from './pages/DataSources'
import Login from './pages/Login'
import Reports from './pages/Reports'
import Settings from './pages/Settings'
import useAuthStore from './store/authStore'

function ProtectedRoute() {
  const accessToken = useAuthStore((s) => s.accessToken)
  return accessToken ? <Outlet /> : <Navigate to="/login" replace />
}

function App() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route element={<ProtectedRoute />}>
        <Route element={<AppLayout />}>
          <Route path="/" element={<Dashboard />} />
          <Route path="/campaigns" element={<Campaigns />} />
          <Route path="/campaigns/:id" element={<CampaignDetail />} />
          <Route path="/reports" element={<Reports />} />
          <Route path="/data-sources" element={<DataSources />} />
          <Route path="/settings" element={<Settings />} />
        </Route>
      </Route>
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  )
}

export default App
