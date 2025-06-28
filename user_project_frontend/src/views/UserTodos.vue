<!-- src/views/user/UserTodos.vue -->
<template>
  <MainLayout>
    <template #default>
        <GoHomeLink />
      <h2 class="text-xl font-bold mb-4">{{ userName }} - Görev Listesi</h2>
      <ul class="space-y-2">
        <li v-for="todo in todos" :key="todo.id" class="flex items-center gap-2">
          <input type="checkbox" :checked="todo.completed" disabled />
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
