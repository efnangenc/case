<template>
    <div :class="['bg-neutral-200 text-white transition-all duration-300 min-h-screen', collapsed ? 'w-16' : 'w-64']">
        <button class="p-2" @click="$emit('toggle')">☰</button>




        <nav v-if="!collapsed">
            <ul>
                <!-- Anasayfa için ikon + metin birlikte router-link içinde -->
                <li v-if="isHomePage">
                    <router-link to="/"
                        class="flex items-center space-x-3 px-4 py-2 text-purple-400 hover:bg-neutral-300 rounded">
                        <UsersIcon class="h-6 w-6 text-gray-400" />
                        <span>Users</span>
                    </router-link>
                </li>

                <!-- Diğer sayfalarda gösterilecek menüler -->
                <template v-else>

                    <div v-if="user"
                        class="flex flex-col sm:flex-row items-center sm:items-start p-5 rounded space-y-4 sm:space-y-0 sm:space-x-4">
                        <img src="https://via.placeholder.com" alt="Avatar"
                            class="w-12 h-12 rounded-full border flex-shrink-0" />

                        <div class="flex-1 text-center sm:text-left">
                            <p class="text-sm mb-2">{{ user.name }}</p>
                            <p class="text-sm mb-2">{{ user.email }}</p>
                        </div>
                    </div>
                    <hr />
                    <!-- <li>
                        <router-link to="/" class="flex items-center space-x-3 px-4 py-2 hover:bg-gray-700 rounded">
                            <UsersIcon class="h-6 w-6 text-gray-400" />
                            <span>Ana Sayfa</span>
                        </router-link>
                    </li> -->

                    <li>
                        <router-link :to="`/user/${userId}/todos`"
                            class="flex items-center space-x-3 px-4 py-2 hover:bg-gray-700 rounded">
                            <TodosIcon class="h-6 w-6 text-gray-400" />
                            <span>Todos</span>
                        </router-link>
                    </li>

                    <li>
                        <router-link :to="`/user/${userId}/posts`"
                            class="flex items-center space-x-3 px-4 py-2 hover:bg-gray-700 rounded">
                            <PostsIcon class="h-6 w-6 text-gray-400" />
                            <span>Posts</span>
                        </router-link>
                    </li>

                    <li>
                        <router-link :to="`/user/${userId}/albums`"
                            class="flex items-center space-x-3 px-4 py-2 hover:bg-gray-700 rounded">
                            <AlbumsIcon class="h-6 w-6 text-gray-400" />
                            <span>Albums</span>
                        </router-link>
                    </li>
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
