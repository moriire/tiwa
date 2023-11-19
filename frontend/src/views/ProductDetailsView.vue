<template>

    <!-- Start Breadcrumbs -->
    <div class="breadcrumbs">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6 col-md-6 col-12">
                    <div class="breadcrumbs-content">
                        <h1 class="page-title">{{ singleProductItem.product.category.name }}</h1>
                    </div>
                </div>
                <div class="col-lg-6 col-md-6 col-12">
                    <ul class="breadcrumb-nav">
                        <li><a href="index.html"><i class="lni lni-home"></i> Home</a></li>
                        <li><a href="index.html">Shop</a></li>
                        <li>{{ singleProductItem.product.name }}</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    <!-- End Breadcrumbs -->
    <!-- Start Item Details -->
<section v-if="loading" class="preloader">

        <div class="preloader-inner">
            <div class="preloader-icon">
                <span></span>
                <span></span>
            </div>
        </div>
          
</section>

    <section class="item-details section">
        <div class="container">
            <div class="top-area">
            
                <div class="row align-items-center" >
                    <div class="col-lg-6 col-md-12 col-12">
                        <div class="product-images">
                            <main id="gallery" ref="gallerySlider">
                                <div class="main-img">
                                    <img :src="singleProductItem.images[0].img" id=".current" alt="#">
                                </div>
                                <div class="images">
                                    <img  v-for="img in singleProductItem.images" :src="img.img" v-bind:key="img.id" class="img" alt="#">
                                </div>
                            </main>
                        </div>
                    </div>
                    <div class="col-lg-6 col-md-12 col-12">
                        <div class="product-info" >
                            <h2 class="title">{{ singleProductItem.product.name }}</h2>
                            <p class="category"><i class="lni lni-tag"></i> {{ singleProductItem.product.category.name }}:<a href="javascript:void(0)">{{ singleProductItem.product.category.name }}</a></p>
                            <h3 class="price">&#8358;{{ singleProductItem.product.discounted_price }}<span>&#8358; {{ singleProductItem.product.price }} </span></h3>
                            <p class="info-text">{{ singleProductItem.product.desc }}.</p>
                            <div class="row">
                                <div class="col-lg-4 col-md-4 col-12">
                                <div class="form-group">
                                        <label for="color">Amount</label>
                                        <input type="number" :v-model="price" v-bind:value="singleProductItem.product.discounted_price" class="form-control" id="color" readonly >
                                    </div>
                                </div>
                                <div class="col-lg-4 col-md-4 col-12">
                                    <div class="form-group quantity">
                                        <label for="count">Quantity</label>
                                        <input v-model="quantity" class="form-control" type="number" id="count" v-bind:min="1" v-bind:max="12" >
                                        
                                    </div>
                                </div>
                                <div class="col-lg-4 col-md-4 col-12">
                                    <div class="form-group quantity">
                                        <label for="total">Total</label>
                                        <input class="form-control" id="total" type="number" readonly :value="quantity*price">
                                        
                                    </div>
                                </div>
                            </div>
                            <div class="bottom-content">
                                <div class="row align-items-end">
                                    <div class="col-12">
                                        <div class="button cart-button">
                                            <button class="btn btn-block" style="width: 100%;">Add to Cart</button>
                                        </div>
                                    </div>
                                    
                                    
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!--div class="product-details-info">
                <div class="single-block">
                    <div class="row">
                        <div class="col-lg-6 col-12">
                            <div class="info-body custom-responsive-margin">
                                <h4>Details</h4>
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
                                    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
                                    exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute
                                    irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat.</p>
                                <h4>Features</h4>
                                <ul class="features">
                                    <li>Capture 4K30 Video and 12MP Photos</li>
                                    <li>Game-Style Controller with Touchscreen</li>
                                    <li>View Live Camera Feed</li>
                                    <li>Full Control of HERO6 Black</li>
                                    <li>Use App for Dedicated Camera Operation</li>
                                </ul>
                            </div>
                        </div>
                        <div class="col-lg-6 col-12">
                            <div class="info-body">
                                <h4>Specifications</h4>
                                <ul class="normal-list">
                                    <li><span>Weight:</span> 35.5oz (1006g)</li>
                                    <li><span>Maximum Speed:</span> 35 mph (15 m/s)</li>
                                    <li><span>Maximum Distance:</span> Up to 9,840ft (3,000m)</li>
                                    <li><span>Operating Frequency:</span> 2.4GHz</li>
                                    <li><span>Manufacturer:</span> GoPro, USA</li>
                                </ul>
                                <h4>Shipping Options:</h4>
                                <ul class="normal-list">
                                    <li><span>Courier:</span> 2 - 4 days, $22.50</li>
                                    <li><span>Local Shipping:</span> up to one week, $10.00</li>
                                    <li><span>UPS Ground Shipping:</span> 4 - 6 days, $18.00</li>
                                    <li><span>Unishop Global Export:</span> 3 - 4 days, $25.00</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div-->
        </div>
    </section>
    <!--section v-else>loading ........... {{ singleProductItem }}</section-->
    <!-- End Item Details -->
</template>
<script setup>
import axios from "axios"
import { useProductStore } from "@/stores/product";
import { ref, onMounted, watchEffect, watch, onBeforeMount,  onServerPrefetch} from "vue";
import { RouterLink, useRoute } from "vue-router";

const BASE = import.meta.env.VITE_BACKEND_API_URL;
const route = useRoute();
const loading = ref(false);
const singleProductItem = ref(null);
const param = ref(route.params.pk);

        const getSingleProduct = async (b)=>{
            loading.value = true;
             try {
                  const res = await axios.get(`${BASE}/api/products/${b}/`)
                  singleProductItem.value = await res.data
              } catch(errors){
                  console.log(errors)
                  alert(errors)
              } finally{
                loading.value = false
              }
          };
          onMounted(getSingleProduct(param.value));
watch(()=>{route.params, getSingleProduct})
onMounted(()=>{
   
    document.addEventListener('DOMContentLoaded', function() {
        if (gallerySlider.value) {
        const current = document.getElementById("current");
        const opacity = 0.6;
        const imgs = document.querySelectorAll(".img");
        imgs.forEach(img => {
            img.addEventListener("click", (e) => {
                //reset opacity
                imgs.forEach(img => {
                    img.style.opacity = 1;
                });
                current.src = e.target.src;
                //adding class 
                //current.classList.add("fade-in");
                //opacity
                e.target.style.opacity = opacity;
            });
        });
    }
    })
    })
const quantity = ref(1)
const price = ref(0)
</script>
<style scoped>
.preloader-false{
    opacity: 0;
    display: none;
}
</style>