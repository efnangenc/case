
<template>
  <MainLayout>
    <template #default>
      <GoHomeLink />
      <div class="posts">
        <div v-for="post in posts" :key="post.id" class="post-item">
          <h3 class="post-title">{{ post.title }}</h3>
          <p class="post-body">{{ post.body }}</p>
          <button @click="openModal(post)" class="seemore-button">
            See More
            <RightArrowIcon class="rightarrow-icon" />
          </button>
          <hr/>
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
import '../assets/styles/UserPosts.scss'

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
