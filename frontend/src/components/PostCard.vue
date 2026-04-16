<script setup>
defineProps({
  post: { type: Object, required: true }
})

defineEmits(['delete'])
</script>

<template>
  <div class="post-card">
    <RouterLink :to="`/posts/${post.id}`">
      <h3>{{ post.title }}</h3>
    </RouterLink>
    <p>{{ new Date(post.created_at).toLocaleDateString() }}</p>
    <button @click="$emit('delete', post.id)">삭제</button>
  </div>
</template>
