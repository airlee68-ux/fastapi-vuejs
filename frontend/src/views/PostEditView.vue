<script setup>
import { ref, reactive, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import api from '@/api'

const route = useRoute()
const router = useRouter()
const formRef = ref(null)
const isSubmitting = ref(false)

const form = reactive({
  title: '',
  content: '',
})

const rules = {
  title: [
    { required: true, message: '제목을 입력해주세요', trigger: 'blur' },
    { min: 2, max: 100, message: '2~100자로 입력해주세요', trigger: 'blur' },
  ],
  content: [
    { required: true, message: '내용을 입력해주세요', trigger: 'blur' },
  ],
}

onMounted(async () => {
  try {
    const response = await api.get(`/posts/${route.params.id}`)
    form.title = response.data.title
    form.content = response.data.content
  } catch (error) {
    ElMessage.error('게시글을 불러오지 못했습니다.')
    router.push('/')
  }
})

async function handleSubmit() {
  const valid = await formRef.value.validate().catch(() => false)
  if (!valid) return

  isSubmitting.value = true
  try {
    await api.put(`/posts/${route.params.id}`, {
      title: form.title,
      content: form.content,
    })
    ElMessage.success('게시글이 수정되었습니다.')
    router.push(`/posts/${route.params.id}`)
  } catch (error) {
    ElMessage.error('게시글 수정에 실패했습니다.')
  } finally {
    isSubmitting.value = false
  }
}
</script>

<template>
  <div>
    <h2>게시글 수정</h2>
    <el-form
      ref="formRef"
      :model="form"
      :rules="rules"
      label-position="top"
    >
      <el-form-item label="제목" prop="title">
        <el-input v-model="form.title" maxlength="100" show-word-limit />
      </el-form-item>
      <el-form-item label="내용" prop="content">
        <el-input
          v-model="form.content"
          type="textarea"
          :rows="8"
        />
      </el-form-item>
      <el-form-item>
        <el-button
          type="primary"
          :loading="isSubmitting"
          @click="handleSubmit"
        >
          수정
        </el-button>
        <el-button @click="router.back()">취소</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
