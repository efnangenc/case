<template>
  <div v-if="show" class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
    <div class="bg-white rounded-2xl shadow-lg max-w-4xl w-full h-4/6 p-6 relative flex flex-col">

      <div class="my-4">
        <h2 class="text-2xl font-semibold mb-2">{{ post.title }}</h2>
        <!-- Kapat Butonu -->
        <button @click="$emit('close')" class="absolute top-10 right-6">
          <CloseIcon class="h-8 w-8" />
        </button>
      </div>

      <!-- İçerik: Post ve Yorumlar -->
      <div class="grid grid-cols-2 gap-10 flex-1 overflow-hidden">
        <!-- Post -->
        <div class="overflow-y-auto pr-2 pl-4">

          <p class="text-gray-700 whitespace-pre-line">{{ post.body }}</p>
        </div>

        <!-- Yorumlar -->
        <div class="overflow-y-auto pl-2">
          <h3 class="text-xl font-semibold mb-4">Comments</h3>
          <div v-if="loading" class="text-gray-500">Loading...</div>
          <div v-else-if="comments.length === 0" class="text-gray-500">Comment Not Found.</div>
          <ul v-else class="space-y-4">
            <li v-for="comment in comments" :key="comment.id" class="border-b pb-4">
              <div class="flex gap-4 items-start">
                <div>
                  <UserIcon class="w-16 h-16 text-gray-400" />
                </div>
                <div class="space-y-1">
                  <p class="text-sm font-medium text-gray-800">{{ comment.email }}</p>
                  <p class="text-sm text-gray-700">{{ comment.body }}</p>
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
