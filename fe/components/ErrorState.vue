<template>
  <div class="error-state">
    <div class="error-content">
      <i class="fas fa-exclamation-circle"></i>
      <h3>Analysis Error</h3>
      <p>{{ message }}</p>
      <button class="button retry-btn" @click="$emit('retry')">Try Again</button>
    </div>
  </div>
</template>

<script setup>
defineProps({ message: String });
</script>