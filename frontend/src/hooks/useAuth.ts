import { useState } from 'react'
import api from '../lib/api'
import type { TokenResponse } from '../types'

export function useAuth() {
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const isAuthenticated = !!localStorage.getItem('access_token')

  async function login(email: string, password: string): Promise<boolean> {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.post<TokenResponse>('/auth/login', { email, password })
      localStorage.setItem('access_token', data.access_token)
      localStorage.setItem('refresh_token', data.refresh_token)
      return true
    } catch {
      setError('E-mail ou senha inválidos')
      return false
    } finally {
      setLoading(false)
    }
  }

  function logout() {
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    window.location.href = '/login'
  }

  return { login, logout, isAuthenticated, loading, error }
}
