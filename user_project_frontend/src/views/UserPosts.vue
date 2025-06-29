<!-- src/views/UserPosts.vue -->
<template>
  <MainLayout>
    <template #default>
      <GoHomeLink />
      <div class="space-y-4">
        <div v-for="post in posts" :key="post.id" class="p-4 gap-4 rounded-lg  bg-white flex flex-col justify-between h-48">
          <h3 class="text-lg font-semibold ">{{ post.title }}</h3>
          <p class="text-sm text-gray-600 w-2/5 break-words">{{ post.body }}</p>
          <button @click="openModal(post)" class="text-gray-600 mr-8 gap-8 hover:underline text-sm mt-2 self-end flex items-center gap-1">
            See More
            <RightArrowIcon class="h-6 w-6 text-gray-400" />
          </button>
          <hr class="border border-gray-200" />
        </div>
      
        <!-- Modal -->
        <PostModal v-if="selectedPost" :show="showModal" :post="selectedPost" @close="closeModal" />
      </div>
    </template>

  </MainLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { getPostsByUser } from '../services/postService'
import MainLayout from '../layouts/MainLayout.vue'
import GoHomeLink from '../components/GoHome.vue'
import PostModal from "../components/PostCommentsModal.vue";
import RightArrowIcon from '../assets/icons/right-arrow.svg'

const route = useRoute()
const userId = route.params.id

const userName = ref('')
const posts = ref([])
const selectedPost = ref(null);
const showModal = ref(false);

onMounted(async () => {
  posts.value = await getPostsByUser(userId)
})

const openModal = (post) => {
  selectedPost.value = post;
  showModal.value = true;
};

const closeModal = () => {
  showModal.value = false;
};

</script>
