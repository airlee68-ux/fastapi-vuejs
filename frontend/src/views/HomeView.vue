<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import { useFetch } from '@/composables/useFetch'

const router = useRouter()
const currentPage = ref(1)
const pageSize = ref(10)

const { data, error, loading, execute: fetchPosts } = useFetch('/posts')

async function loadPosts() {
  await fetchPosts({
    params: { page: currentPage.value, size: pageSize.value },
  })
  if (error.value) {
    ElMessage.error('게시글 목록을 불러오지 못했습니다.')
  }
}

onMounted(() => {
  loadPosts()
})

function handlePageChange(page) {
  currentPage.value = page
  loadPosts()
}

function formatDate(row) {
  return new Date(row.created_at).toLocaleDateString()
}

function goToDetail(row) {
  router.push(`/posts/${row.id}`)
}
</script>

<template>
  <div>
    <h2>게시판</h2>
    <el-button type="primary" @click="router.push('/posts/new')">
      새 글 작성
    </el-button>

    <el-table
      :data="data?.items || []"
      v-loading="loading"
      stripe
      style="margin-top: 16px"
      @row-click="goToDetail"
    >
      <el-table-column prop="id" label="번호" width="80" />
      <el-table-column prop="title" label="제목" />
      <el-table-column
        label="작성일"
        width="140"
        :formatter="formatDate"
      />
    </el-table>

    <el-pagination
      v-if="(data?.total || 0) > pageSize"
      layout="prev, pager, next"
      :total="data?.total || 0"
      :page-size="pageSize"
      :current-page="currentPage"
      style="margin-top: 16px; justify-content: center"
      @current-change="handlePageChange"
    />
  </div>
</template>
