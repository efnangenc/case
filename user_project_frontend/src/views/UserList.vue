<template>
  <MainLayout>
    <template #default>
      <div>
        <h1 class="bg-red-400 p-5 text-white text-2xl font-semibold">Kullanıcı Listesi</h1>
        <div v-if="users.length === 0" class="p-4">Yükleniyor...</div>

        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 p-4">
          <router-link v-for="user in users" :key="user.id" :to="`/user/${user.id}/todos`"
            class="block p-4 border rounded-lg shadow hover:shadow-lg transition-shadow bg-white text-gray-800">


            <div
              class="flex flex-col sm:flex-row items-center sm:items-start p-5 rounded space-y-4 sm:space-y-0 sm:space-x-4">
              <!-- Resim/Avatar -->
              <img src="https://via.placeholder.com/80" alt="Avatar"
                class="w-32 h-32 rounded-full border flex-shrink-0" />

              <!-- İçerik -->
              <div class="flex-1 p-4 text-center sm:text-left">
                <h2 class="text-lg font-bold mb-2">{{ user.name }}</h2>
                <p class="text-sm text-gray-600">{{ user.email }}</p>
                <p class="text-sm text-gray-600">{{ user.phone }}</p>
              </div>

            </div>


            
            <!-- Location başlığı ve ikon -->
            <div class="flex items-center space-x-2 mt-2 text-gray-500">
               <LocationIcon class="h-5 w-5 text-gray-400" />
              <span class="font-bold">LocationnAmakısahalii:</span>
            </div>
            <p class="text-sm text-gray-500">{{ user.address.city }}</p>

            <!-- Company başlığı ve ikon -->
            <div class="flex items-center space-x-2 mt-2 text-gray-500">
               <CompanyIcon class="h-5 w-5 text-gray-400" />
              <span class="font-bold">Company:</span>
            </div>
            <p class="text-sm text-gray-500">{{ user.company.name }}</p>


            <!-- Website başlığı ve ikon -->
            <div class="flex items-center space-x-2 mt-2 text-gray-500">
               <WebsiteIcon class="h-5 w-5 text-gray-400" />
              <span class="font-bold">Website:</span>
            </div>
             <p class="text-sm text-gray-500">Website: {{ user.website }}</p>
          </router-link>
        </div>
      </div>
    </template>
  </MainLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getUsers } from '../services/userService'
import MainLayout from '../layouts/MainLayout.vue'
import CompanyIcon from '../assets/icons/company.svg'
import LocationIcon from '../assets/icons/location.svg'
import WebsiteIcon from '../assets/icons/website.svg'

const users = ref([])

onMounted(async () => {
  users.value = await getUsers()
})
</script>
