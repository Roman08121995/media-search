<template>
  <div class="modal">
    <div class="modal-content">
      <div class="modal-header">
        <h2>Analysis Report</h2>
        <button class="close-button" @click="$emit('close')">×</button>
      </div>
      <div class="modal-body">
        <p>Details will be shown here for video ID: {{ videoId }}</p>
      </div>
      <div class="modal-footer">
        <button class="download-button" disabled>
          <span class="button-content">
            <i class="fas fa-download"></i>
            Download Report
          </span>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({ videoId: String });
</script>