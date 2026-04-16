<!-- filename: frontend/src/views/HomeView.vue -->
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import api from '@/api'

interface Post {
  id: number
  title: string
  created_at: string
}

const posts = ref<Post[]>([])
const isLoading = ref(true)

onMounted(async () => {
  try {
    const response = await api.get('/posts')
    posts.value = response.data
  } catch (error) {
    console.error('목록 로드 실패:', error)
  } finally {
    isLoading.value = false
  }
})
</script>

<template>
  <h2>게시판</h2>
  <p v-if="isLoading">로딩 중...</p>
  <ul v-else>
    <li v-for="post in posts" :key="post.id">
      <RouterLink :to="`/posts/${post.id}`">
        {{ post.title }}
      </RouterLink>
      <span>{{ new Date(post.created_at).toLocaleDateString() }}</span>
    </li>
  </ul>
  <p v-if="!isLoading && posts.length === 0">
    아직 게시글이 없습니다.
  </p>
  <RouterLink to="/posts/new">새 글 작성</RouterLink>
</template>