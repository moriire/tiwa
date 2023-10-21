<script setup>
import { ref } from "vue";
import { VueperSlides, VueperSlide } from "vueperslides"
const labelsType = ref(1);
const slides = [
  {
    title: 'Aso Oke',
    content: 'This video is autoplayed, played in loop, has no controls and is not reacting to user interactions.',
    image: "/src/assets/photos/sample.jpg",
    
  },
  {
    title: 'Blossoming flower',
    content: 'This video is played once, has controls and is reacting to user interactions.',
    image: "/src/assets/photos/sample.jpg",
    
  }
]
</script>

<template>
 <vueper-slides autoplay>
  <vueper-slide v-for="(slide, i) in slides"
    :key="id"
    :title="slide.title"
    :content="slide.content"
    />
  <template #pause>
    <i class="icon pause_circle_outline"></i>
  </template>
</vueper-slides>
  <ui-image-list :text-protection="labelsType === 2">
  <ui-image-item
    v-for="i in 15"
    :key="i"
    bg-image="/src/assets/photos/sample.jpg"
    style="width: 230px; margin: 8px;"
  >
    <ui-image-text v-if="labelsType">Text label</ui-image-text>
  </ui-image-item>
</ui-image-list>

</template>
<style scoped>
.vueperslides__bullet .default {
  background-color: rgba(0, 0, 0, 0.3);
  border: none;
  box-shadow: none;
  transition: 0.3s;
  width: 16px;
  height: 16px;
}

.vueperslides__bullet--active .default {background-color: #42b983;}

.vueperslides__bullet span {
  display: block;
  color: #fff;
  font-size: 10px;
  opacity: 0.8;
}
</style>