<script setup>
import { ref } from 'vue';
import { defineEmits } from 'vue';

const input = ref('');
const isLoading = ref(false);

const emit = defineEmits(['update-scene']);

const fetchData = async () => {
  if (input.value) {
    try {
      isLoading.value = true;

      const response = await fetch("http://localhost:3000/events?" + new URLSearchParams({
        start: input.value
      }).toString());
      const data = await response.json();
      emit('update-scene', data);

      isLoading.value = false;
    } catch (error) {
      console.error("Error");
    }
  }
}
</script>

<template>
    <transition name="fade">
      <div>
        <div id="loading-container" v-if="isLoading">
          <object
            id="loading"
            data="loading.svg"
            title="Loading..."
          ></object>
          <h2>Loading Events. This may take a minute...</h2>
        </div>
        <div id="ui">
          <h1>Terre</h1>
          <input type="text" v-model="input" @keyup.enter="fetchData" placeholder="Enter Year"/>
        </div>
      </div>
    </transition>
</template>

<style scoped>
#loading-container {
  position: fixed;

  width: 100vw;
  height: 100vh;

  background-color: rgba(0,0,0,0.75);

  display: flex;
  flex-direction: column;

  align-items: center;
  justify-content: center;

  text-align: center;
}

@keyframes rotation {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(359deg);
  }
}


#loading {
  width: 100px;
  animation: rotation 2s infinite linear;
}

#ui {
  position: fixed;
  margin: 1rem;
}

.h1 {
    font-size: 4vw;
    margin: 0;
}

input {
  background-color: rgba(255,255,255,0.5);
  border: 0px;
  padding: 0.5rem;
  font-size: 1rem;
  border-radius: 0.5rem;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>