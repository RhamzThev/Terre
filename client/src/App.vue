<script setup>
import { onMounted, ref } from 'vue'
import Earth from './components/Earth.vue'
import WIP from './components/WIP.vue'

const showOverlay = ref(true);

onMounted(() => {
  setTimeout(() => {
    showOverlay.value = false;
  }, 1000)
})
</script>

<template>
  <transition name="overlay-fade">
    <div id="overlay" v-if="showOverlay"></div>
  </transition>
  <WIP />
  <Earth />
</template>

<style scoped>
#overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: black;
  z-index: 9999;
}

.overlay-fade-enter-active, .overlay-fade-leave-active {
  transition: opacity 3s ease;
}
.overlay-fade-enter, .overlay-fade-leave-to {
  opacity: 0;
}
</style>
