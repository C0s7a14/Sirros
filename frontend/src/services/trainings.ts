import api from '../lib/api'
import type { Training, TrainingDocument } from '../types'

export const trainingsService = {
  list: () => api.get<Training[]>('/trainings').then((r) => r.data),
  get: (id: string) => api.get<Training>(`/trainings/${id}`).then((r) => r.data),
  create: (data: { title: string; description: string }) =>
    api.post<Training>('/trainings', data).then((r) => r.data),
  uploadDocument: (trainingId: string, file: File) => {
    const form = new FormData()
    form.append('file', file)
    return api
      .post<TrainingDocument>(`/trainings/${trainingId}/documents`, form)
      .then((r) => r.data)
  },
}
