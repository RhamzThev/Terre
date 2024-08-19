<script setup>
import { ref } from "vue";

const popup = ref(true);

</script>

<template>
    <transition name="fade">
      <div v-if="popup" class="backdrop"></div>
    </transition>

    <transition name="fade">
        <div v-if="popup" class="outer-paper">
            <div class="inner-paper">
                <h1 class="title">Welcome to Terre</h1>
                <p class="subtitle">This project is a work in progress. Closing this popup will showcase an interactive depiction of Earth.</p>
                <button @click="popup = false" class="close">Close</button>
            </div>
        </div>
    </transition>
</template>

<style scoped>
.backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 900;
}

.outer-paper {
    position: absolute;

    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);

    mask-size: 100% 100%;
    mask-repeat: no-repeat;

    background-color: black;
    mask-image: url("../../public/paper.svg");

    width: 50vw;
    height: 35vw;

    display: flex;

    align-items: center;
    justify-content: center;
    z-index: 1000;
}

.inner-paper {
    width: 40vw;
    height:25vw;
    border: 0.75vw solid var(--fore);
    text-align: center;

    display: flex;
    flex-direction: column;

    align-items: center;
    justify-content: center;}

.title {
    font-size: 4vw;
    margin: 0;
}

.subtitle {
    font-size: 2vw;
    width: 30vw;
}

.close {
    font-size: 2vw;
    padding: 1vw 4vw;
    transition: 0.25s ease;
}

.close:hover {
    background-color: rgb(112, 100, 83);
    transform: scale(0.9);
}

.close:active {
    background-color: white;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>