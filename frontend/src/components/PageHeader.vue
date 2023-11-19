 <script setup>
 import CategoriesNav from "@/components/CategoriesNav.vue";
 import SearchBar from "@/components/SearchBar.vue";
    import { ref, onMounted, watch } from "vue";
    import { useRouter, useRoute, RouterView } from "vue-router";
    import { useAuthStore } from "@/stores/auth";
    import { useProductStore } from '@/stores/product';
    import 'tiny-slider/dist/tiny-slider.css'; // Import Tiny Slider styles
    import { tns } from 'tiny-slider/src/tiny-slider';
    const productStore = useProductStore();
    const router = useRouter();
    const route = useRoute();
    const authStore = useAuthStore()
    const active = ref(0);
    const uniqueCartItems = (d) => {
        return new Set(d).values()
    }
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
    const toggleSidebar= () =>{
            sidebarVisible.value = !sidebarVisible;
    }
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
        <!-- Start Header Middle -->
        <div class="header-middle">
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-lg-3 col-md-3 col-7">
                        <!-- Start Header Logo -->
                        <a class="navbar-brand" href="index.html">
                            <img src="/src/assets/images/logo/logo.svg" alt="Logo">
                        </a>
                        <!-- End Header Logo -->
                    </div>
                    <div class="col-lg-5 col-md-7 d-xs-none">
                        <SearchBar></SearchBar>
                    </div>
                    <div class="col-lg-4 col-md-2 col-5">
                        <div class="middle-right-area">
                            <div class="nav-hotline">
                                <i class="lni lni-phone"></i>
                                <h3>Hotline:
                                    <span>(+100) 123 456 7890</span>
                                </h3>
                            </div>
                            <div class="navbar-cart">
                                <div class="wishlist">
                                    <a href="javascript:void(0)">
                                        <i class="lni lni-heart"></i>
                                        <span class="total-items">0</span>
                                    </a>
                                </div>
                                <div class="cart-items">
                                    <a href="javascript:void(0)" class="main-btn">
                                        <i class="lni lni-cart"></i>
                                        <span class="total-items">{{  productStore.selectedCount }}</span>
                                    </a>
                                    <!-- Shopping Item -->
                                    <div class="shopping-item">
                                        <div class="dropdown-cart-header">
                                            <span>{{  productStore.selectedCount }} Items</span>
                                            <a href="cart.html">View Cart</a>
                                        </div>
                                        <ul class="shopping-list">
                                            <li v-for="(cart, index) in uniqueCartItems(productStore.selectedProducts)" v-bind:key="index">
                                                <a href="javascript:void(0)" class="remove" title="Remove this item"><i
                                                        class="lni lni-close"></i></a>
                                                <div class="cart-img-head">
                                                    <a class="cart-img" href="product-details.html"><img
                                                            :src="cart.images[0].img" alt="#"></a>
                                                </div>

                                                <div class="content">
                                                    <h4><a href="product-details.html">
                                                            {{ cart.product.name }}</a></h4>
                                                    <p class="quantity">1x - <span class="amount">{{ cart.product.price }}</span></p>
                                                </div>
                                            </li>
                                           
                                        </ul>
                                        <div class="bottom">
                                            <div class="total">
                                                <span>Total</span>
                                                <span class="total-amount">$134.00</span>
                                            </div>
                                            <div class="button">
                                                <a href="checkout.html" class="btn animate">Checkout</a>
                                            </div>
                                        </div>
                                    </div>
                                    <!--/ End Shopping Item -->
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- End Header Middle -->
        <!-- Start Header Bottom -->
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-8 col-md-6 col-12">
                    <div class="nav-inner">
                        <!-- Start Mega Category Menu -->
                        
                         <CategoriesNav />
                        <!-- End Mega Category Menu -->
                        <!-- Start Navbar -->
                        <nav class="navbar navbar-expand-lg">
                            <button class="navbar-toggler mobile-menu-btn" type="button" data-bs-toggle="collapse"
                                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                                aria-expanded="false" aria-label="Toggle navigation">
                                <span class="toggler-icon"></span>
                                <span class="toggler-icon"></span>
                                <span class="toggler-icon"></span>
                            </button>
                            <div class="collapse navbar-collapse sub-menu-bar" id="navbarSupportedContent">
                                <ul id="nav" class="navbar-nav ms-auto">
                                    <li class="nav-item" v-for="(item, index) in items" v-bind:key="index">
                                    <RouterLink :to="item.route" aria-label="Toggle navigation">{{ item.label }}</RouterLink>
                                    </li>
                                   
                                </ul>
                            </div> <!-- navbar collapse -->
                        </nav>
                        <!-- End Navbar -->
                    </div>
                </div>
                <div class="col-lg-4 col-md-6 col-12">
                    <!-- Start Nav Social -->
                    <div class="nav-social">
                        <h5 class="title">Follow Us:</h5>
                        <ul>
                            <li>
                                <a href="javascript:void(0)"><i class="lni lni-facebook-filled"></i></a>
                            </li>
                            <li>
                                <a href="javascript:void(0)"><i class="lni lni-twitter-original"></i></a>
                            </li>
                            <li>
                                <a href="javascript:void(0)"><i class="lni lni-instagram"></i></a>
                            </li>
                            <li>
                                <a href="javascript:void(0)"><i class="lni lni-skype"></i></a>
                            </li>
                        </ul>
                    </div>
                    <!-- End Nav Social -->
                </div>
            </div>
        </div>
        <!-- End Header Bottom -->
    </header>
    <!-- End Header Area -->
</template>