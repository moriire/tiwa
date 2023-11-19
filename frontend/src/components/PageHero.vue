<template>
    <!-- Start Hero Area -->
    <!--section class="hero-area">
        <div class="container">
            <div class="row">
                <div class="col-lg-8 col-12 custom-padding-right">
                    <div class="slider-head" >

                        
                        <div class="hero-slider" ref="heroSlider">
                        
                            <div 
                            class="single-slider" v-for="product in products" v-bind:key="product.product.id" 
                                :style="`background-image: url(${product.images[0].img });`">
                                <div class="content">
                                    <h2>
                                        <span>{{ product.product.name }}</span>
                                    </h2>
                                    <p>{{ product.product.name }}</p>
                                    <h3><span>Now Only</span> ${{ product.product.discounted_price }}</h3>
                                    <div class="button">
                                        <a href="product-grids.html" class="btn">Shop Now</a>
                                    </div>
                                </div>
                            </div>
                           
                           
                        </div>
                        
                    </div>
                </div>
                <div class="col-lg-4 col-12">
                    <div class="row">
                        <div class="col-lg-12 col-md-6 col-12 md-custom-padding">
                            
                            <div class="hero-small-banner"
                                style="background-image: url(src/assets/images/hero/slider-bnr.jpg);">
                                <div class="content">
                                    <h2>
                                        <span>New line required</span>
                                        iPhone 12 Pro Max
                                    </h2>
                                    <h3>$259.99</h3>
                                </div>
                            </div>
                            
                        </div>
                        <div class="col-lg-12 col-md-6 col-12">
                            
                            <div class="hero-small-banner style2">
                                <div class="content">
                                    <h2>Weekly Sale!</h2>
                                    <p>Saving up to 50% off all online store items this week.</p>
                                    <div class="button">
                                        <a class="btn" href="product-grids.html">Shop Now</a>
                                    </div>
                                </div>
                            </div>
                            
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section-->
    <!-- End Hero Area -->
</template>
<script setup>
import { tns } from 'tiny-slider/src/tiny-slider';
import { ref, onMounted, watch, nextTick } from "vue"; 
import { useProductStore } from "@/stores/product";
const heroSlider = ref(null);
const productStore = useProductStore();
const products = productStore.getClassedProduct

onMounted(() => {
    document.addEventListener('DOMContentLoaded', function() {
    if (heroSlider.value) {
      tns({
        container: heroSlider.value,
        slideBy: 'page',
        autoplay: true,
        autoplayButtonOutput: false,
        mouseDrag: true,
        gutter: 0,
        items: 1,
        nav: false,
        controls: true,
        controlsText: ['<i class="lni lni-chevron-left"></i>', '<i class="lni lni-chevron-right"></i>'],
    });
    }
})
}) 
</script>
