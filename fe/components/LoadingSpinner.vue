<!-- components/LoadingSpinner.vue -->
<template>
  <div class="spinner-container">
    <div class="spinner">
      <div class="spinner-ring"></div>
      <p>Processing Video Analysis</p>
    </div>
  </div>
</template>

<style scoped>
.spinner-container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 2rem;
}
.spinner {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.spinner-ring {
  border: 6px solid #eee;
  border-top: 6px solid #333;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;
}
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}
</style>
