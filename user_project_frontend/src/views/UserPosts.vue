<!-- src/views/UserPosts.vue -->
<template>
  <MainLayout>
    <template #default>
      <GoHomeLink />
      <ul class="space-y-4">
        <li v-for="post in posts" :key="post.id">
          <h3 class="text-lg font-semibold">{{ post.title }}</h3>
          <p>{{ post.body }}</p>
        </li>
      </ul>
    </template>
  </MainLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
// import { getUserDetail } from '../services/userService'
import { getPostsByUser } from '../services/postService'
import MainLayout from '../layouts/MainLayout.vue'
import GoHomeLink from '../components/GoHome.vue' 

const route = useRoute()
const userId = route.params.id

const userName = ref('')
const posts = ref([])

onMounted(async () => {
  // const user = await getUserDetail(userId)
  // userName.value = user.name
  posts.value = await getPostsByUser(userId)
})
</script>
