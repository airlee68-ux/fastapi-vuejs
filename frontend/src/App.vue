<script setup>
import { useAuthStore } from '@/stores/auth'
import { storeToRefs } from 'pinia'

const auth = useAuthStore()
const { isLoggedIn } = storeToRefs(auth)
</script>

<template>
  <header>
    <h1>FastAPI + Vue 게시판</h1>
    <nav>
      <RouterLink to="/">홈</RouterLink>
      <RouterLink to="/chat">채팅</RouterLink>
      <RouterLink to="/posts/new" v-if="isLoggedIn">
        새 글 작성
      </RouterLink>
      <template v-if="isLoggedIn">
        <button @click="auth.logout()">로그아웃</button>
      </template>
      <template v-else>
        <RouterLink to="/login">로그인</RouterLink>
        <RouterLink to="/signup">회원가입</RouterLink>
      </template>
    </nav>
  </header>
  <main>
    <RouterView />
  </main>
</template>
