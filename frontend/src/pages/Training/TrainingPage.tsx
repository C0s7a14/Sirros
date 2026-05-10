import { useRef, useState } from 'react'
import { useParams } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { trainingsService } from '../../services/trainings'

export function TrainingPage() {
  const { id } = useParams<{ id: string }>()
  const fileRef = useRef<HTMLInputElement>(null)
  const [uploading, setUploading] = useState(false)
  const [uploadMsg, setUploadMsg] = useState<string | null>(null)

  const { data: training, isLoading } = useQuery({
    queryKey: ['training', id],
    queryFn: () => trainingsService.get(id!),
    enabled: !!id,
  })

  async function handleUpload(e: React.ChangeEvent<HTMLInputElement>) {
    const file = e.target.files?.[0]
    if (!file || !id) return
    setUploading(true)
    setUploadMsg(null)
    try {
      await trainingsService.uploadDocument(id, file)
      setUploadMsg('PDF enviado! Processamento em andamento.')
    } catch {
      setUploadMsg('Erro ao enviar PDF.')
    } finally {
      setUploading(false)
    }
  }

  if (isLoading) return <p className="p-8 text-gray-500">Carregando...</p>
  if (!training) return <p className="p-8 text-red-500">Treinamento não encontrado.</p>

  return (
    <div className="p-8 max-w-2xl mx-auto space-y-6">
      <h1 className="text-2xl font-semibold text-gray-800">{training.title}</h1>
      <p className="text-gray-600">{training.description}</p>

      <div className="border border-dashed border-gray-300 rounded-lg p-6 text-center space-y-3">
        <p className="text-sm text-gray-500">Adicionar PDF ao treinamento</p>
        <input ref={fileRef} type="file" accept=".pdf" className="hidden" onChange={handleUpload} />
        <button
          onClick={() => fileRef.current?.click()}
          disabled={uploading}
          className="bg-indigo-600 text-white px-4 py-2 rounded-lg text-sm hover:bg-indigo-700 disabled:opacity-50"
        >
          {uploading ? 'Enviando...' : 'Selecionar PDF'}
        </button>
        {uploadMsg && <p className="text-sm text-gray-600">{uploadMsg}</p>}
      </div>
    </div>
  )
}
