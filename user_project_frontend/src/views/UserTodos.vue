<template>
  <div>
    <h2>{{ userName }} - Görev Listesi</h2>
    <ul>
      <li v-for="todo in todos" :key="todo.id">
        <input type="checkbox" :checked="todo.completed" disabled />
        {{ todo.title }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { getUserDetail } from '../services/userService'
import { getTodosByUser } from '../services/todoService'

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
