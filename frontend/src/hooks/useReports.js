import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import * as reportsApi from '../services/reports'

export function useReports(params) {
  return useQuery({
    queryKey: ['reports', params],
    queryFn: () => reportsApi.getReports(params).then((res) => res.data),
  })
}

export function useGenerateReport() {
  const queryClient = useQueryClient()
  return useMutation({
    mutationFn: (id) => reportsApi.generateReport(id),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['reports'] }),
  })
}
