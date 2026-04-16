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

async function handleSignup() {
  isSubmitting.value = true
  errorMessage.value = ''
  try {
    await auth.register(username.value, password.value)
    router.push('/login')
  } catch (error) {
    errorMessage.value =
      error.response?.data?.detail || '회원가입에 실패했습니다.'
  } finally {
    isSubmitting.value = false
  }
}
</script>

<template>
  <h2>회원가입</h2>
  <form @submit.prevent="handleSignup">
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
      {{ isSubmitting ? '가입 중...' : '회원가입' }}
    </button>
  </form>
  <p>이미 계정이 있으신가요? <RouterLink to="/login">로그인</RouterLink></p>
</template>
