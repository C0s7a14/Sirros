import api from '../lib/api'
import type { Quiz } from '../types'

export const quizzesService = {
  list: () => api.get<Quiz[]>('/quizzes').then((r) => r.data),
  get: (id: string) => api.get<Quiz>(`/quizzes/${id}`).then((r) => r.data),
}
