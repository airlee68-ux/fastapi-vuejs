<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const seconds = ref(0)
let timer = null

onMounted(() => {
  timer = setInterval(() => {
    seconds.value++
  }, 1000)
})

onUnmounted(() => {
  clearInterval(timer)
  console.log('타이머가 정리되었습니다')
})
</script>

<template>
  <p>경과 시간: {{ seconds }}초</p>
</template>
