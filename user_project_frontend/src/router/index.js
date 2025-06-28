import { createRouter, createWebHistory } from 'vue-router'
import UserList from '../views/UserList.vue'
import UserDetail from '../views/UserDetail.vue'
import UserTodos from '../views/UserTodos.vue'

const routes = [
  { path: '/', name: 'UserList', component: UserList },
  { path: '/user/:id', name: 'UserDetail', component: UserDetail },
  { path: '/user/:id/todos', name: 'UserTodos', component: UserTodos}
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
