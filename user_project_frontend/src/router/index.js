import { createRouter, createWebHistory } from 'vue-router'
import UserList from '../views/UserList.vue'
import UserTodos from '../views/UserTodos.vue'
import UserPosts from '../views/UserPosts.vue'
import UserAlbums from '../views/UserAlbums.vue'
import AlbumDetail from '../views/AlbumDetail.vue'

const routes = [
  {
    path: '/',
    name: 'UserList',
    component: UserList,
  },
  {
    path: '/users/:id/todos',
    name: 'UserTodos',
    component: UserTodos,
  },
  {
    path: '/users/:id/posts',
    name: 'UserPosts',
    component: UserPosts,
  },
  {
    path: '/users/:id/albums',
    name: 'UserAlbums',
    component: UserAlbums,
  },
  {
    path: '/albums/:id',
    name: 'AlbumDetail',
    component: AlbumDetail
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
