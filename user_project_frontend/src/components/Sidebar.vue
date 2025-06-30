<template>
    <div :class="['sidebar', collapsed ? 'sidebar-collapsed' : 'sidebar-expanded']">
        <button class="toggle-button" @click="$emit('toggle')">☰</button>

        <nav v-if="!collapsed">
            <ul>
                <!-- Anasayfadayken -->
                <li v-if="isHomePage">
                    <router-link to="/" class="menu-link">
                        <UsersIcon class="menu-icon" />
                        <span>Users</span>
                    </router-link>
                </li>

                <!-- Diğer sayfalardayken -->
                <template v-else>

                    <div v-if="user" class="user-info">
                        <!-- <img src="https://via.placeholder.com" alt="Avatar"
                            class="w-12 h-12 rounded-full border flex-shrink-0" /> -->
                        <div>
                            <UserIcon class="user-icon" />
                        </div>

                        <div class="user-info-text">
                            <p>{{ user.name }}</p>
                            <p>{{ user.email }}</p>
                        </div>
                    </div>
                    <hr />
                    <div class="menu">
                        <li>
                            <router-link :to="`/user/${userId}/todos`" class="menu-link">
                                <TodosIcon class="menu-icon" />
                                <span>Todos</span>
                            </router-link>
                        </li>

                        <li>
                            <router-link :to="`/user/${userId}/posts`" class="menu-link">
                                <PostsIcon class="menu-icon" />
                                <span>Posts</span>
                            </router-link>
                        </li>

                        <li>
                            <router-link :to="`/user/${userId}/albums`" class="menu-link">
                                <AlbumsIcon class="menu-icon" />
                                <span>Albums</span>
                            </router-link>
                        </li>
                    </div>
                    <div class="sidebar-logo">
                        <img :src="N2MobileLogo" alt="N2 Mobile Logo" />
                    </div>
                </template>
            </ul>
        </nav>
    </div>
</template>


<script setup>
import { computed, onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import { getUserDetail } from '../services/userService'
import UsersIcon from '../assets/icons/users.svg'
import TodosIcon from '../assets/icons/todos.svg'
import PostsIcon from '../assets/icons/posts.svg'
import AlbumsIcon from '../assets/icons/albums.svg'
import UserIcon from '../assets/icons/user-circle.svg'
import N2MobileLogo from '../assets/icons/logo.png'
import '../assets/styles/Sidebar.scss'

defineProps(['collapsed'])
defineEmits(['toggle'])

const route = useRoute()
const isHomePage = computed(() => route.path === '/')
const userId = computed(() => route.params.id)
const user = ref([])

onMounted(async () => {
    if (!userId.value) return

    try {
        user.value = await getUserDetail(userId.value)
    } catch (error) {
        console.error('Kullanıcı bilgileri alınamadı:', error)
    }
})

</script>
