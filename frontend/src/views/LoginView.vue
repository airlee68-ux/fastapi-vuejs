<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const auth = useAuthStore()
const username = ref('')
const password = ref('')
const errorMessage = ref('')
const isSubmitting = ref(false)

async function handleLogin() {
  isSubmitting.value = true
  errorMessage.value = ''
  try {
    await auth.login(username.value, password.value)
    router.push('/')
  } catch (error) {
    errorMessage.value =
      error.response?.data?.detail || '로그인에 실패했습니다.'
  } finally {
    isSubmitting.value = false
  }
}
</script>

<template>
  <h2>로그인</h2>
  <form @submit.prevent="handleLogin">
    <div>
      <label>아이디</label>
      <input v-model="username" required />
    </div>
    <div>
      <label>비밀번호</label>
      <input v-model="password" type="password" required />
    </div>
    <p v-if="errorMessage" style="color: red">{{ errorMessage }}</p>
    <button type="submit" :disabled="isSubmitting">
      {{ isSubmitting ? '로그인 중...' : '로그인' }}
    </button>
  </form>
  <p>계정이 없으신가요? <RouterLink to="/signup">회원가입</RouterLink></p>
</template>
