<template>
  <div v-if="show" class="modal">
    <div class="modal-item">

      <div class="my-4">
        <h2 class="modal-post-title">{{ post.title }}</h2>
        <!-- Kapat Butonu -->
        <button @click="$emit('close')">
          <CloseIcon class="close-icon" />
        </button>
      </div>

      <!-- İçerik: Post ve Yorumlar -->
      <div class="contents">
        <!-- Post -->
        <div class="modal-post">

          <p class="modal-post-body">{{ post.body }}</p>
        </div>

        <!-- Yorumlar -->
        <div class="comments">
          <h3 class="comments-title">Comments</h3>
          <div v-if="loading">Loading...</div>
          <div v-else-if="comments.length === 0">Comment Not Found.</div>
          <ul v-else class="comment-item">
            <li v-for="comment in comments" :key="comment.id" class="border-b pb-4">
              <div class="flex gap-4 items-start ">
                <div>
                  <UserIcon class="comment-user-icon" />
                </div>
                <div>
                  <p class="comment-email">{{ comment.email }}</p>
                  <p class="comment-body">{{ comment.body }}</p>
                </div>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>



<script setup>
import { ref, watch } from 'vue'
import { getCommentsByPost } from '../services/commentService'
import CloseIcon from '../assets/icons/x.svg'
import UserIcon from '../assets/icons/user-circle.svg'
import '../assets/styles/PostCommentsModal.scss'

const props = defineProps({
  show: Boolean,
  post: Object,
});
const emit = defineEmits(["close"]);

const comments = ref([])
const loading = ref(false)

// watch yerine senin anlayacağın tarzda:
const loadComments = async () => {
  if (props.post?.id) {
    loading.value = true
    comments.value = await getCommentsByPost(props.post.id)
    loading.value = false
  }
}

// Bu fonksiyonu modal her açıldığında çağır
watch(() => props.show, (newVal) => {
  if (newVal) {
    loadComments()
  }
})

</script>
