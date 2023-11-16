 <script setup>
    import { ref, onMounted, watch } from "vue";
    import { useRouter, useRoute, RouterView } from "vue-router";
    import { useAuthStore } from "@/stores/auth";
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
          label: 'About Us',
          icon: 'pi pi-fw pi-plus',
          route: '/add-product'
      },
      {
          label: 'Contact',
          icon: 'pi pi-fw pi-user',
          route: '/profile'
      },/*
      {
          label: 'Upload',
          icon: 'pi pi-fw pi-upload',
          route: '/upload'
      }*/
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

<template>
 <!-- Start Header Area -->
    <header class="header navbar-area">
        <!-- Start Topbar -->
        <div class="topbar">
            <div class="container">
                <div class="row align-items-center justify-content-between">
                    <!--div class="col-lg-4 col-md-4 col-12">
                        <div class="top-left">
                            <ul class="menu-top-link">
                                <li>
                                    <div class="select-position">
                                        <select id="select4">
                                            <option value="0" selected>$ USD</option>
                                            <option value="1">€ EURO</option>
                                            <option value="2">$ CAD</option>
                                            <option value="3">₹ INR</option>
                                            <option value="4">¥ CNY</option>
                                            <option value="5">৳ BDT</option>
                                        </select>
                                    </div>
                                </li>
                                <li>
                                    <div class="select-position">
                                        <select id="select5">
                                            <option value="0" selected>English</option>
                                            <option value="1">Español</option>
                                            <option value="2">Filipino</option>
                                            <option value="3">Français</option>
                                            <option value="4">العربية</option>
                                            <option value="5">हिन्दी</option>
                                            <option value="6">বাংলা</option>
                                        </select>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </div-->
                    <div class="col-lg-4 col-md-4 col-12">
                        <div class="top-middle">
                            <ul class="useful-links">
                                <li v-for="(item, index) in items" v-bind:key="index" >
                                    <RouterLink :to="item.route">{{ item.label }}</RouterLink>
                                </li>
                            </ul>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-4 col-12">
                        <div class="top-end">
                            <div class="user">
                                <i class="lni lni-user"></i>
                                Hello
                            </div>
                            <ul class="user-login">
                                <li>
                                    <RouterLink to="/auth/login">Sign In</RouterLink>
                                </li>
                                <li>
                                    <RouterLink :to="{'name': 'register'}">Register</RouterLink>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- End Topbar -->
    </header>
    <!-- End Header Area -->
</template>