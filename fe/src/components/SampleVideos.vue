<template>
  <div class="mt-10">
    <h2 class="text-2xl font-semibold mb-4">Main Data</h2>
    <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
      <div v-for="video in videos" :key="video.title" class="bg-white p-4 rounded-xl shadow">
        <video :src="video.src" controls preload="metadata" class="rounded-md w-full" />
        <div class="mt-2 text-sm">
          <p class="font-medium">{{ video.title }}</p>
          <p class="text-gray-500">{{ video.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const videos = [
  {
    title: 'Effortless English',
    src: '../sample/effortless english.mp4',
    description: 'Listening #Studying'
  },
  {
    title: 'Project Recording',
    src: '../sample/linkedin scraping.mp4',
    description: 'Live #CCTV'
  },
  {
    title: 'Rain Footage',
    src: '../sample/rain.mp4',
    description: 'Weather #NightVision'
  }
]
</script>