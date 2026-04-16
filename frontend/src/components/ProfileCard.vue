<template>
  <div :class="{ card: true, 'card-active': isOnline }">
    <img :src="avatarUrl" :alt="name + ' 프로필'" />
    <h3>{{ name }}</h3>
    <p>{{ role }}</p>
    <p :style="{ color: isOnline ? 'green' : 'gray' }">
      {{ isOnline ? '온라인' : '오프라인' }}
    </p>
    <p>게시글 {{ postCount }}개</p>
    <button
      :disabled="!isOnline"
      @click="postCount++"
    >
      글쓰기
    </button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const name = ref('정우진')
const role = ref('프론트엔드 개발자')
const avatarUrl = ref('https://i.pravatar.cc/100')
const isOnline = ref(true)
const postCount = ref(42)
</script>

<style scoped>
.card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 16px;
  text-align: center;
  max-width: 250px;
}
.card-active { border-color: green; }
.card img { border-radius: 50%; }
</style>
