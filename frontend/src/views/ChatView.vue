<script setup>
import { ref, onMounted } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useWebSocket } from '@/composables/useWebSocket'

const authStore = useAuthStore()

const wsUrl = (import.meta.env.VITE_API_URL || 'http://localhost:8000')
  .replace('http', 'ws') + '/ws/chat'

const { messages, isConnected, connect, sendMessage } = useWebSocket(wsUrl)
const newMessage = ref('')

function handleSend() {
  if (newMessage.value.trim()) {
    sendMessage({
      username: authStore.username,
      content: newMessage.value,
      timestamp: new Date().toISOString()
    })
    newMessage.value = ''
  }
}

onMounted(() => connect())
</script>

<template>
  <div class="chat-container">
    <h2>채팅</h2>
    <p>{{ isConnected ? '연결됨' : '연결 끊김' }}</p>

    <div class="messages">
      <div v-for="(msg, index) in messages" :key="index">
        <strong>{{ msg.username }}</strong>: {{ msg.content }}
      </div>
    </div>

    <form @submit.prevent="handleSend">
      <input v-model="newMessage" placeholder="메시지를 입력하세요" />
      <button type="submit" :disabled="!isConnected">전송</button>
    </form>
  </div>
</template>
