<script setup>
import { onMounted, ref } from 'vue'
import Earth from './components/Earth.vue'
import UI from './components/UI.vue'

const showOverlay = ref(true);
// const emit = defineEmits(['data']);

onMounted(() => {
  setTimeout(() => {
    showOverlay.value = false;
  }, 1000)
})

const eventData = ref(null);

const handleData = (data) => {
  eventData.value = data;
}
</script>

<template>
  <transition name="overlay-fade">
    <div id="overlay" v-if="showOverlay"></div>
  </transition>
  <UI @update-scene="handleData" :emit="emit"/>
  <Earth :scene-data="eventData"/>
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
