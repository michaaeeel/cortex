import { useNavigate } from 'react-router-dom'
import api from '../services/api'
import { login as loginApi } from '../services/auth'
import useAuthStore from '../store/authStore'

export default function useAuth() {
  const navigate = useNavigate()
  const { user, accessToken, refreshToken, login: setAuth, logout: clearAuth } = useAuthStore()

  const login = async (username, password) => {
    const { data } = await loginApi(username, password)
    setAuth(
      { username: data.username, email: data.email, role: data.role, organization: data.organization },
      data.access,
      data.refresh,
    )
    navigate('/')
  }

  const logout = async () => {
    if (refreshToken) {
      try {
        await api.post('/api/v1/auth/logout/', { refresh: refreshToken })
      } catch {
        // best-effort — clear locally regardless
      }
    }
    clearAuth()
    navigate('/login')
  }

  const isAuthenticated = !!accessToken

  return { user, isAuthenticated, login, logout }
}
