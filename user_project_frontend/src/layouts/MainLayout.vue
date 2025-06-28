<!-- src/components/MainLayout.vue -->
<template>
  <div class="flex min-h-screen">
    <Sidebar :collapsed="collapsed" @toggle="toggleSidebar" />
    
     <!-- <div :class="[collapsed ? 'ml-16' : 'ml-64']" class="transition-all duration-300 flex-1 p-4"> -->
        <main class="flex-1 p-6 bg-gray-50 overflow-auto">
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
