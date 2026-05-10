import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { BrowserRouter, Route, Routes, Navigate } from 'react-router-dom'
import { PrivateRoute } from './components/PrivateRoute'
import { LoginPage } from './pages/Login/LoginPage'
import { TrainingsPage } from './pages/Trainings/TrainingsPage'
import { TrainingPage } from './pages/Training/TrainingPage'
import { QuizPage } from './pages/Quiz/QuizPage'

const queryClient = new QueryClient()

export default function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route element={<PrivateRoute />}>
            <Route path="/trainings" element={<TrainingsPage />} />
            <Route path="/trainings/:id" element={<TrainingPage />} />
            <Route path="/quizzes/:id" element={<QuizPage />} />
          </Route>
          <Route path="*" element={<Navigate to="/trainings" replace />} />
        </Routes>
      </BrowserRouter>
    </QueryClientProvider>
  )
}
