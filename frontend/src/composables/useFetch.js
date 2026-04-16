import { ref } from 'vue'
import api from '@/api'

export function useFetch(url, options = {}) {
  const data = ref(null)
  const error = ref(null)
  const loading = ref(false)

  async function execute(overrideOptions = {}) {
    loading.value = true
    error.value = null
    try {
      const config = { ...options, ...overrideOptions }
      const response = await api.request({
        url,
        method: config.method || 'get',
        params: config.params,
        data: config.body,
      })
      data.value = response.data
      return response.data
    } catch (err) {
      error.value = err.response?.data?.detail || err.message
      throw err
    } finally {
      loading.value = false
    }
  }

  return { data, error, loading, execute }
}
