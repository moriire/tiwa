<template>
     <!-- Start Header/Navigation -->
  <nav class="custom-navbar navbar navbar navbar-expand-md navbar-dark bg-dark" arial-label="Furni navigation bar">

<div class="container">
  
  <a class="navbar-brand" href="index.html">Tiwa <span>'n'</span> Tiwa</a>

  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarsFurni" aria-controls="navbarsFurni" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarsFurni">
    <ul class="custom-navbar-nav navbar-nav ms-auto mb-2 mb-md-0">
      <li  :class="[isActive && 'router-link-active',  isExactActive && 'router-link-exact-active', 'nav-item']" v-for="(item, index) in items" v-bind:key="index">
        <RouterLink class="navbar-brand active" :to="item.route" > {{ item.label }}</RouterLink>
        <!--a class="nav-link" href="index.html">{{ item.label }}</a-->
      </li>
      <!--li><a class="nav-link" href="shop.html">Shop</a></li>
      <li><a class="nav-link" href="about.html">About us</a></li>
      <li><a class="nav-link" href="services.html">Services</a></li>
      <li><a class="nav-link" href="blog.html">Blog</a></li>
      <li class="active"><a class="nav-link" href="contact.html">Contact us</a></li-->
    </ul>

    <ul class="custom-navbar-cta navbar-nav mb-2 mb-md-0 ms-5">
      <li><a class="nav-link" href="#"><img src="/src/assets/images/user.svg"></a></li>
      <li><a class="nav-link" href="cart.html"><img src="/src/assets/images/cart.svg"></a></li>
    </ul>
  </div>
</div>
  
</nav>
<!-- End Header/Navigation -->
<RouterView/>

</template>
    
    <script setup>
    import { ref, onMounted, watch } from "vue";
    import { useRouter, useRoute, RouterView } from "vue-router";
    import { useAuthStore } from "@/stores/auth";
    //import ThemeSwitcher from './components/ThemeSwitcher.vue';
    
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
          label: 'Shop',
          icon: 'pi pi-fw pi-gift',
          route: '/products'
      },
      {
          label: 'About us',
          icon: 'pi pi-fw pi-plus',
          route: '/add-product'
      },
      {
          label: 'Contact',
          icon: 'pi pi-fw pi-user',
          route: '/profile'
      },
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
    
    </style>
    