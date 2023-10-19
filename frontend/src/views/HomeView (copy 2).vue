<script setup>
import { ref } from "vue";
const labelsType = ref(1);
    

</script>

<template>
  <ui-image-list :text-protection="labelsType === 2">
  <ui-image-item
    v-for="i in 15"
    :key="i"
    bg-image="/src/assets/photos/sample.jpg"
  >
    <ui-image-text v-if="labelsType">Text label</ui-image-text>
  </ui-image-item>
</ui-image-list>

</template>
<style scoped lang="scss">
@use '@material/image-list' with (
  $standard-gutter-size: 4px,
  $masonry-gutter-size: 16px,
  $icon-size: 24px,
  $text-protection-background-color: rgba(0, 0, 0, 0.6),
  $text-protection-height: 48px,
  $text-protection-horizontal-padding: 16px,
  $shape-radius: 0
);

</style>