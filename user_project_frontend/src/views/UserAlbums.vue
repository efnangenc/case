<template>
  <MainLayout>
    <template #default>
      <GoHomeLink />
      <!-- <h2 class="text-xl font-bold mb-4">{{ userName }} - Albümler</h2> -->
      <ul class="space-y-4">
        <li v-for="album in albums" :key="album.id">
          <h3 class="text-lg font-semibold">{{ album.title }}</h3>
        </li>
      </ul>
    </template>
  </MainLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
// import { getUserDetail } from '../services/userService'
import { getAlbumsByUser } from '../services/albumService'
import MainLayout from '../layouts/MainLayout.vue'
import GoHomeLink from '../components/GoHome.vue' 

const route = useRoute()
const userId = route.params.id

const userName = ref('')
const albums = ref([])

onMounted(async () => {
  // const user = await getUserDetail(userId)
  // userName.value = user.name

  albums.value = await getAlbumsByUser(userId)
})
</script>
