<template>
  <MainLayout>
    <template #default>
      <GoHomeLink />
      <!-- <h2 class="text-xl font-bold mb-4">{{ userName }} - Albümler</h2> -->
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        <div v-for="album in albums" :key="album.id" class="border rounded-lg shadow bg-white p-4">
          <!-- Fotoğraf grid - 2x2 -->
          <div class="grid grid-cols-2 ">
<!-- 
            <div v-for="photo in album.photos" :key="photo.id" class="w-24 h-24">
              <img :src="photo.url" alt="Fotoğraf" class="object-cover w-full h-full" />
            </div> -->

            <div v-for="photo in album.photos" :key="photo.id" class="w-full h-24">
              <img :src="`https://picsum.photos/id/${photo.id}/150`" alt="Fotoğraf"
                class="object-cover w-full h-full rounded" />
            </div>
          </div>

          <!-- Albüm Adı -->
          <h3 class="text-md font-semibold text-center">{{ album.title }}</h3>
        </div>
      </div>

    </template>
  </MainLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
// import { getUserDetail } from '../services/userService'
import { getAlbumsByUser } from '../services/albumService'
import { getPhotosByAlbum } from '../services/photoService'
import MainLayout from '../layouts/MainLayout.vue'
import GoHomeLink from '../components/GoHome.vue'

const route = useRoute()
const userId = route.params.id

// const userName = ref('')
const albums = ref([])

onMounted(async () => {
  // const user = await getUserDetail(userId)
  // userName.value = user.name

  const userAlbums = await getAlbumsByUser(userId)

  // Her albüm için 4 foto al
  const albumsWithPhotos = await Promise.all(
    userAlbums.map(async (album) => {
      const photos = await getPhotosByAlbum(album.id)
      return {
        ...album,
        photos: photos.slice(0, 4) // sadece ilk 4 foto
      }
    })
  )
  console.log('Albums with photos:', albumsWithPhotos)

  albums.value = albumsWithPhotos
})
</script>
