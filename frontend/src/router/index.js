import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import HomeView from '../views/HomeView.vue'
import PostDetailView from '../views/PostDetailView.vue'
import PostCreateView from '../views/PostCreateView.vue'
import PostEditView from '../views/PostEditView.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import ChatView from '../views/ChatView.vue'

const routes = [
  { path: '/', name: 'home', component: HomeView },
  { path: '/login', name: 'login', component: LoginView },
  { path: '/signup', name: 'signup', component: SignupView },
  {
    path: '/posts/new',
    name: 'post-create',
    component: PostCreateView,
    meta: { requiresAuth: true },
  },
  {
    path: '/posts/:id/edit',
    name: 'post-edit',
    component: PostEditView,
    meta: { requiresAuth: true },
  },
  { path: '/posts/:id', name: 'post-detail', component: PostDetailView },
  { path: '/chat', name: 'chat', component: ChatView },
]

const router = createRouter({ history: createWebHistory(), routes })

router.beforeEach((to, from) => {
  const auth = useAuthStore()

  if (to.meta.requiresAuth && !auth.isLoggedIn) {
    return { name: 'login', query: { redirect: to.fullPath } }
  }
})

export default router
