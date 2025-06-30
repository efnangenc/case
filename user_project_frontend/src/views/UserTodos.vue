
<template>
  <MainLayout>
    <template #default>
        <GoHomeLink />
      <ul class="todos">
        <li v-for="todo in todos" :key="todo.id" class="item">
          <input class="checkbox" type="checkbox" :checked="todo.completed" />
          <span>{{ todo.title }}</span>
        </li>
      </ul>
    </template>
  </MainLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { getUserDetail } from '../services/userService'
import { getTodosByUser } from '../services/todoService'
import MainLayout from '../layouts/MainLayout.vue'
import GoHomeLink from '../components/GoHome.vue' 
import '../assets/styles/UserTodos.scss'

const route = useRoute()
const userId = route.params.id

const userName = ref('')
const todos = ref([])

onMounted(async () => {
  const user = await getUserDetail(userId)
  userName.value = user.name

  todos.value = await getTodosByUser(userId)
})
</script>
