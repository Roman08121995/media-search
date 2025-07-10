<template>
  <div class="relative max-w-2xl mx-auto">
    <!-- Search Input -->
    <UInput
      v-model="searchQuery"
      placeholder="Search videos, audio, images..."
      icon="i-heroicons-magnifying-glass"
      size="xl"
      autofocus
      :ui="{
        rounded: 'rounded-full',
        padding: {
          xl: 'px-5 py-3'
        }
      }"
    >
      <!-- Voice Search Button -->
      <template #trailing>
        <UButton
          color="gray"
          variant="ghost"
          icon="i-heroicons-microphone"
          :padded="false"
          @click="startVoiceSearch"
        />
      </template>
    </UInput>

    <!-- Search Filters (Will implement later) -->
    <div v-if="showFilters" class="mt-2">
      <!-- Filter components will go here -->
    </div>
  </div>
</template>

<script setup>
const searchQuery = ref('')
const showFilters = ref(false)

// Voice search mock function
const startVoiceSearch = () => {
  alert('Voice search would activate here')
}
</script>

<style scoped>
/* Custom focus styles */
:deep(.ui-input) {
  transition: box-shadow 0.2s ease;
}
:deep(.ui-input:focus) {
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
}
</style>