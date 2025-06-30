<template>
  <MainLayout>
    <template #default>
      <div class="goAlbums">
        <LeftArrowIcon class="leftarrow-icon" />
        <button @click="goBack" class="goBack-button">
          Go Albums
        </button>
      </div>

      <div class="album-detail">
        <div class="album-details">
          <div v-for="photo in photos" :key="photo.id" class="album-photo-item">
            <img :src="`https://picsum.photos/id/${photo.id}/150`" alt="Fotoğraf" class="album-images" />
          </div>
        </div>
      </div>


    </template>
  </MainLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getPhotosByAlbum } from '../services/photoService'
import MainLayout from '../layouts/MainLayout.vue'
import LeftArrowIcon from '../assets/icons/left-arrow.svg'
import '../assets/styles/AlbumDetail.scss'

const route = useRoute()
console.log('route.params:', route.params)
const albumId = route.params.id
console.log('Album ID:', albumId)

const photos = ref([])
const albumTitle = ref('')

onMounted(async () => {
  console.log('Album ID:', albumId)
  const result = await getPhotosByAlbum(albumId)
  console.log('Photos:', result)
  photos.value = result
  albumTitle.value = result.length > 0 ? `#${albumId}` : 'Unknown Album'
})

const router = useRouter()
function goBack() {
  router.back()
}
</script>
