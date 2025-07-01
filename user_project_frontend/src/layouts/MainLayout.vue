<!-- src/components/MainLayout.vue -->
<template>
  <div class="flex min-h-screen">
    <Sidebar :collapsed="collapsed" @toggle="toggleSidebar" />
        <main class="flex-1 p-10 bg-gray-50 overflow-auto">
      <slot />
        </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Sidebar from '../components/Sidebar.vue'

const collapsed = ref(false)
const toggleSidebar = () => {
  collapsed.value = !collapsed.value
}
</script>
