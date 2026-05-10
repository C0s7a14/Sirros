import { useParams } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { quizzesService } from '../../services/quizzes'

export function QuizPage() {
  const { id } = useParams<{ id: string }>()

  const { data: quiz, isLoading } = useQuery({
    queryKey: ['quiz', id],
    queryFn: () => quizzesService.get(id!),
    enabled: !!id,
  })

  if (isLoading) return <p className="p-8 text-gray-500">Carregando...</p>
  if (!quiz) return <p className="p-8 text-red-500">Quiz não encontrado.</p>

  return (
    <div className="p-8 max-w-2xl mx-auto space-y-4">
      <h1 className="text-2xl font-semibold text-gray-800">{quiz.title}</h1>
      <p className="text-sm text-gray-400">Quiz ID: {quiz.id}</p>
    </div>
  )
}
