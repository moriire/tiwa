<template>
    <RouterView/>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import { useRouter, useRoute, RouterView } from "vue-router";
import { useAuthStore } from "./stores/auth";
import PageHeader from './components/PageHeader.vue';
import PageHero from './components/PageHero.vue';

import { useCategoryStore } from "@/stores/categories";
const categoryStore = useCategoryStore()

const router = useRouter();
const route = useRoute();
const authStore = useAuthStore()
const active = ref(0);

const items = ref([
  {
      label: 'Home',
      icon: 'pi pi-fw pi-home',
      route: '/'
  },
  {
      label: 'Product',
      icon: 'pi pi-fw pi-gift',
      route: '/products'
  },
  {
      label: 'Add Product',
      icon: 'pi pi-fw pi-plus',
      route: '/add-product'
  },
  {
      label: 'Profile',
      icon: 'pi pi-fw pi-user',
      route: '/profile'
  },
  {
      label: 'Upload',
      icon: 'pi pi-fw pi-upload',
      route: '/upload'
  }
]);

onMounted(() => {
  categoryStore.getCategories();
  active.value = items.value.findIndex((item) => route.path === router.resolve(item.route).path);
})

watch(
  route,
  () => {
      active.value = items.value.findIndex((item) => route.path === router.resolve(item.route).path);
  },
  { immediate: true }
);
</script>
