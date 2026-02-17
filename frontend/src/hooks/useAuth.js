import { useNavigate } from 'react-router-dom'
import { login as loginApi } from '../services/auth'
import useAuthStore from '../store/authStore'

export default function useAuth() {
  const navigate = useNavigate()
  const { user, accessToken, login: setAuth, logout: clearAuth } = useAuthStore()

  const login = async (username, password) => {
    const { data } = await loginApi(username, password)
    setAuth({ username }, data.access, data.refresh)
    navigate('/')
  }

  const logout = () => {
    clearAuth()
    navigate('/login')
  }

  const isAuthenticated = !!accessToken

  return { user, isAuthenticated, login, logout }
}
