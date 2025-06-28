import { createRouter, createWebHistory } from 'vue-router'
import UserList from '../views/UserList.vue'
import UserTodos from '../views/UserTodos.vue'
import UserPosts from '../views/UserPosts.vue'
import UserAlbums from '../views/UserAlbums.vue'

const routes = [
  {
    path: '/',
    name: 'UserList',
    component: UserList,
  },
  {
    path: '/user/:id/todos',
    name: 'UserTodos',
    component: UserTodos,
  },
  {
    path: '/user/:id/posts',
    name: 'UserPosts',
    component: UserPosts,
  },
  {
    path: '/user/:id/albums',
    name: 'UserAlbums',
    component: UserAlbums,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
