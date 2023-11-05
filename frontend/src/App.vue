<template>
    <Toolbar>
    <template #start>
        <Button icon="pi pi-plus" class="mr-2" />
    </template>
    <template #center>
      <TabMenu v-model:activeIndex="active" :model="items">
          <template #item="{ label, item, props }">
              <router-link v-if="item.route" v-slot="routerProps" :to="item.route" custom>
                  <a :href="routerProps.href" v-bind="props.action" @click="($event) => routerProps.navigate($event)" @keydown.enter.space="($event) => routerProps.navigate($event)">
                      <span v-bind="props.icon" />
                      <span v-bind="props.label">{{ label }}</span>
                  </a>
              </router-link>
          </template>
      </TabMenu>
    </template>
    <template #end>
        <SplitButton :label="authStore.isAuthenticated?'Loggedin':'Login'" icon="pi pi-check" :model="authStore.isAuthenticated?loggedin:loggedout"></SplitButton>
    </template>
    </Toolbar>
    <RouterView/>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import { useRouter, useRoute, RouterView } from "vue-router";
import { useAuthStore } from "./stores/auth";
const router = useRouter();
const route = useRoute();
const authStore = useAuthStore()
const active = ref(0);
const loggedout = ref([
  {
      label: 'Login',
      icon: 'pi pi-fw pi-home',
      route: '/'
  },
  {
      label: 'Sign up',
      icon: 'pi pi-fw pi-home',
      route: '/'
  },
  {
      label: 'Forgot Password',
      icon: 'pi pi-fw pi-gift',
      route: '/products'
  },
]);
const loggedin = ref([
  {
      label: 'Profile',
      icon: 'pi pi-fw pi-user',
      route: '/profile'
  },
  {
      label: 'Change Password',
      icon: 'pi pi-fw pi-lock',
      route: '/products'
  },
  {
      label: 'Logout',
      icon: 'pi pi-fw pi-user',
      route: '/profile'
  },
  {
      label: 'Upload',
      icon: 'pi pi-fw pi-upload',
      route: '/upload'
  }
]);
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
<style>
#app{
    height: 100vh;
}
</style>
