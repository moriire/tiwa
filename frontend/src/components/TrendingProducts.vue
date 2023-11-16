<template>
<!-- Start Trending Product Area -->
    <section class="trending-product section" style="margin-top: 12px;">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <div class="section-title">
                        <h2>Trending Product</h2>
                        <p>There are many variations of passages of Lorem Ipsum available, but the majority have
                            suffered alteration in some form.</p>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-3 col-md-6 col-12"
                 v-for="product in productStore.product_data" v-bind:key="product.product.id">
                    <!-- Start Single Product -->
                    <div class="single-product" >
                        <div class="product-image">
                            <img :src="product.images[0].img" alt="#">
                            <span class="sale-tag" v-show="product.product.discount>0">-25%</span>
                            <div class="button">
                                <a type="button" @click="productStore.selectProduct(product)" class="btn"><i class="lni lni-cart"></i> Add to Cart</a>
                            </div>
                        </div>
                        <div class="product-info">
                            <span class="category">{{ product.product.category.name }}</span>
                            <h4 class="title">
                                <a href="product-grids.html">{{ product.product.name }}</a>
                            </h4>
                            <ul class="review">
                                <li><i class="lni lni-star-filled"></i></li>
                                <li><i class="lni lni-star-filled"></i></li>
                                <li><i class="lni lni-star-filled"></i></li>
                                <li><i class="lni lni-star-filled"></i></li>
                                <li><i class="lni lni-star-filled"></i></li>
                                <li><span>5.0 Review(s)</span></li>
                            </ul>
                            <div class="price"> 
                                <span>&#8358;{{ product.product.price }}</span>
                            </div>
                        </div>
                    </div>
                    <!-- End Single Product -->
                </div>
            </div>
        </div>
    </section>
    <!-- End Trending Product Area -->
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useProductStore } from '@/stores/product';
const productStore = useProductStore();
onMounted(() => {
    productStore.getProducts()
});
</script>