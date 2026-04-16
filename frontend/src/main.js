import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import ko from 'element-plus/dist/locale/ko.mjs'

const pinia = createPinia()

createApp(App)
  .use(pinia)
  .use(router)
  .use(ElementPlus, { locale: ko })
  .mount('#app')
