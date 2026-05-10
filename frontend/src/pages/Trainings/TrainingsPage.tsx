import { useQuery } from '@tanstack/react-query'
import { Link } from 'react-router-dom'
import { trainingsService } from '../../services/trainings'

export function TrainingsPage() {
  const { data: trainings, isLoading } = useQuery({
    queryKey: ['trainings'],
    queryFn: trainingsService.list,
  })

  if (isLoading) return <p className="p-8 text-gray-500">Carregando...</p>

  return (
    <div className="p-8 max-w-2xl mx-auto">
      <h1 className="text-2xl font-semibold text-gray-800 mb-6">Treinamentos</h1>
      <ul className="space-y-3">
        {trainings?.map((t) => (
          <li key={t.id}>
            <Link
              to={`/trainings/${t.id}`}
              className="block bg-white border border-gray-200 rounded-lg px-4 py-3 hover:border-indigo-400 transition"
            >
              <p className="font-medium text-gray-800">{t.title}</p>
              <p className="text-sm text-gray-500 mt-1">{t.description}</p>
            </Link>
          </li>
        ))}
        {trainings?.length === 0 && (
          <p className="text-gray-400 text-sm">Nenhum treinamento cadastrado.</p>
        )}
      </ul>
    </div>
  )
}
