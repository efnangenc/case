<template>
  <MainLayout>
    <template #default>
      <GoHomeLink />
      <div class="albums">
        <div v-for="album in albums" :key="album.id" class="album-item">
          <router-link :to="`/albums/${album.id}`">
            <div class="photo-grid">
              <!-- <div v-for="photo in album.photos" :key="photo.id" class="photo-item">
                <img :src="photo.thumbnailUrl" alt="Fotoğraf" class="images" />
              </div> -->

              <div v-for="photo in album.photos" :key="photo.id" class="photo-item">
                <img :src="`https://picsum.photos/id/${photo.id}/150`" alt="Fotoğraf" class="images" />
              </div>
            </div>

            <h3 class="album-title">{{ album.title }}</h3>
          </router-link>
        </div>
      </div>
    </template>
  </MainLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { getAlbumsByUser } from '../services/albumService'
import { getPhotosByAlbum } from '../services/photoService'
import MainLayout from '../layouts/MainLayout.vue'
import GoHomeLink from '../components/GoHome.vue'
import '../assets/styles/UserAlbums.scss'

const route = useRoute()
const userId = route.params.id

const albums = ref([])

onMounted(async () => {
  const userAlbums = await getAlbumsByUser(userId)
  console.log('Kullanıcının Albümleri:', userAlbums)

  // Her albüm için 4 foto alınıyor
  const albumsWithPhotos = await Promise.all(
    userAlbums.map(async (album) => {
      const photos = await getPhotosByAlbum(album.id)
        console.log(`Album ${album.id} photos:`, photos)
      return {
        ...album,
        photos: photos.slice(0, 4)

      }
    })
  )
  albums.value = albumsWithPhotos
})
</script>
