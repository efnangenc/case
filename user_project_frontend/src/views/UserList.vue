<template>
  <MainLayout>
    <template #default>
      <div>
        <h1 class="userlist-title">All Users</h1>
        <div v-if="users.length === 0">Loading...</div>

        <div class="user-cards">
          <router-link v-for="user in users" :key="user.id" :to="`/user/${user.id}/todos`" class="cards-item">
            <div class="card-info">
              <!-- Resim/Avatar -->
              <div>
                <UserIcon class="allusers-icon" />
              </div>
              <!-- İçerik -->
              <div class="card-user-info">
                <h2>{{ user.name }}</h2>
                <p>{{ user.email }}</p>
                <p>{{ user.phone }}</p>
              </div>
            </div>

            <div class="userdetail-info">
              <!-- Location başlığı ve ikon -->
              <div class="detail-info">
                <LocationIcon class="info-icon" />
                <span>Location:</span>
              </div>
              <p>
                {{ user.address.street }}, {{ user.address.suite }},<br />
                {{ user.address.city }} - {{ user.address.zipcode }}
              </p>
              <!-- Company başlığı ve ikon -->
              <div class="detail-info">
                <CompanyIcon class="info-icon" />
                <span>Company:</span>
              </div>
              <p>{{ user.company.name }}</p>


              <!-- Website başlığı ve ikon -->
              <div class="detail-info">
                <WebsiteIcon class="info-icon" />
                <span>Website:</span>
              </div>
              <p>Website: {{ user.website }}</p>
            </div>

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
import UserIcon from '../assets/icons/user-circle.svg'
import '../assets/styles/UserList.scss'

const users = ref([])

onMounted(async () => {
  users.value = await getUsers()
})
</script>
