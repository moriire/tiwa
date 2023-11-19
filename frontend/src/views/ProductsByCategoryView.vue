<template>
  <div>{{ productStore.productbycategory_data }}</div>
  
</template>
<script setup>
import { useProductStore } from "@/stores/product";
import { onMounted } from "vue";
import { useRoute } from "vue-router";
import { ref } from "vue"
const productStore = useProductStore();
const route = useRoute();
const routes = ref(route.params.category)
onMounted(()=>{
  productStore.getProductsByCategory(routes.value)
})
</script>