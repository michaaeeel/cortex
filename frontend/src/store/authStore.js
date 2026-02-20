import { create } from 'zustand'

function loadUser() {
  try {
    const raw = localStorage.getItem('cortex_user')
    return raw ? JSON.parse(raw) : null
  } catch {
    return null
  }
}

const useAuthStore = create((set) => ({
  user: loadUser(),
  accessToken: localStorage.getItem('accessToken'),
  refreshToken: localStorage.getItem('refreshToken'),

  login: (user, accessToken, refreshToken) => {
    localStorage.setItem('accessToken', accessToken)
    localStorage.setItem('refreshToken', refreshToken)
    localStorage.setItem('cortex_user', JSON.stringify(user))
    set({ user, accessToken, refreshToken })
  },

  logout: () => {
    localStorage.removeItem('accessToken')
    localStorage.removeItem('refreshToken')
    localStorage.removeItem('cortex_user')
    set({ user: null, accessToken: null, refreshToken: null })
  },
}))

export default useAuthStore
