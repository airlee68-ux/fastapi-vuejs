import { ref, onUnmounted } from 'vue'

export function useWebSocket(url) {
  const socket = ref(null)
  const messages = ref([])
  const isConnected = ref(false)

  let reconnectTimer = null

  function connect() {
    socket.value = new WebSocket(url)

    socket.value.onopen = () => {
      isConnected.value = true
    }

    socket.value.onmessage = (event) => {
      messages.value.push(JSON.parse(event.data))
    }

    socket.value.onclose = () => {
      isConnected.value = false
      reconnectTimer = setTimeout(connect, 3000)
    }
  }

  function disconnect() {
    if (reconnectTimer) {
      clearTimeout(reconnectTimer)
      reconnectTimer = null
    }
    if (socket.value) {
      socket.value.close()
      socket.value = null
    }
  }

  function sendMessage(data) {
    if (socket.value && isConnected.value) {
      socket.value.send(JSON.stringify(data))
    }
  }

  onUnmounted(() => disconnect())

  return { messages, isConnected, connect, disconnect, sendMessage }
}
