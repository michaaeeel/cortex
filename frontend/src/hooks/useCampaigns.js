import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import * as campaignsApi from '../services/campaigns'

export function useCampaigns(params) {
  return useQuery({
    queryKey: ['campaigns', params],
    queryFn: () => campaignsApi.getCampaigns(params).then((res) => res.data),
  })
}

export function useCampaign(id) {
  return useQuery({
    queryKey: ['campaigns', id],
    queryFn: () => campaignsApi.getCampaign(id).then((res) => res.data),
    enabled: !!id,
  })
}

export function useCreateCampaign() {
  const queryClient = useQueryClient()
  return useMutation({
    mutationFn: campaignsApi.createCampaign,
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['campaigns'] }),
  })
}
