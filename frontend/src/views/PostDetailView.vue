<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '@/api'

const route = useRoute()
const router = useRouter()
const post = ref(null)

onMounted(async () => {
  try {
    const response = await api.get(`/posts/${route.params.id}`)
    post.value = response.data
  } catch (error) {
    console.error('게시글 로드 실패:', error)
    router.push('/')
  }
})

async function deletePost() {
  if (confirm('정말 삭제하시겠습니까?')) {
    await api.delete(`/posts/${route.params.id}`)
    router.push('/')
  }
}
</script>

<template>
  <div v-if="post">
    <h2>{{ post.title }}</h2>
    <img
      v-if="post.image_url"
      :src="`${api.defaults.baseURL}${post.image_url}`"
      :alt="post.title"
      style="max-width: 100%; height: auto;"
    />
    <p>{{ post.content }}</p>
    <p>작성일: {{ new Date(post.created_at).toLocaleDateString() }}</p>
    <RouterLink :to="`/posts/${post.id}/edit`">수정</RouterLink>
    <button @click="deletePost">삭제</button>
    <button @click="router.push('/')">목록으로</button>
  </div>
  <p v-else>로딩 중...</p>
</template>
