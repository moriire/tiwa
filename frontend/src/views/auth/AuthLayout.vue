<template>
    <!-- Start Header/Navigation -->
<!--nav class="custom-navbar navbar navbar navbar-expand-md navbar-dark bg-dark" arial-label="Furni navigation bar">

<div class="container">
    <a class="navbar-brand" href="index.html">Furni<span>.</span></a>

    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarsFurni" aria-controls="navbarsFurni" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarsFurni">
        <ul class="custom-navbar-nav navbar-nav ms-auto mb-2 mb-md-0">
            <li class="nav-item" >
                <a class="nav-link" href="index.html">uuuuu</a>
            </li>
            <li><a class="nav-link" href="shop.html">Shop</a></li>
            <li><a class="nav-link" href="about.html">About us</a></li>
            <li><a class="nav-link" href="services.html">Services</a></li>
            <li><a class="nav-link" href="blog.html">Blog</a></li>
            <li><a class="nav-link" href="contact.html">Contact us</a></li>
        </ul>

        <ul class="custom-navbar-cta navbar-nav mb-2 mb-md-0 ms-5">
            <li><a class="nav-link" href="#"><img src="/src/assets/images/user.svg"></a></li>
            <li><a class="nav-link" href="cart.html"><img src="/src/assets/images/cart.svg"></a></li>
        </ul>
    </div>
</div>
    
</nav-->

<RouterView />
<!-- End Header/Navigation -->
    <!--Toolbar>
        
        <template #start>
           <div>
            logo
           </div>
           
        </template>
        <template #end>
            <ThemeSwitcher />
            <div class="card relative z-2">
                <Menubar :model="items" />
            </div>
           
        </template>
    </Toolbar>
    <Toolbar>
        <template #center>
          <TabMenu v-model:activeIndex="active" :model="items" style="margin:0;">
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
        
    </Toolbar-->
  
    </template>
    <script setup>
    import { ref, onMounted, watch } from "vue";
    import { useRouter, useRoute, RouterView } from "vue-router";
    import { useAuthStore } from "@/stores/auth";
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
    const toggleSidebar= () =>{
            sidebarVisible.value = !sidebarVisible;
    }
    </script>

    