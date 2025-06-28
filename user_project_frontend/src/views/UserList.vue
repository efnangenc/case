<template>
  <div>
    <h1 class="bg-red-400 p-5">Kullanıcı Listesi</h1>
    <div v-if="users.length === 0">Yükleniyor...</div>
    <ul>
      <li v-for="user in users" :key="user.id">
        <router-link :to="`/user/${user.id}`">{{ user.name }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getUsers } from '../services/userService'

const users = ref([])

onMounted(async () => {
  users.value = await getUsers()
})
</script>
