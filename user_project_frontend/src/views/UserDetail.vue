<!---->
<template>
  <div v-if="user">
    <h2>{{ user.name }}</h2>
    <p>{{ user.email }}</p>
    <!-- Buraya tabs veya nav ile: posts, albums, todos eklenebilir -->
    <li>
      <router-link :to="`/user/${user.id}/todos`">todo list</router-link>
    </li>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { getUserDetail } from '../services/userService'

const route = useRoute()
const user = ref(null)

onMounted(async () => {
  user.value = await getUserDetail(route.params.id)
})
</script>
