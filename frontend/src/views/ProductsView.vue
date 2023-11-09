<template>


		<!-- Start Hero Section -->
			<div class="hero">
				<div class="container">
					<div class="row justify-content-between">
						<div class="col-lg-5">
							<div class="intro-excerpt">
								<h1>Shop</h1>
							</div>
						</div>
						<div class="col-lg-7">
							
						</div>
					</div>
				</div>
			</div>
		<!-- End Hero Section -->

		

		<div class="untree_co-section product-section before-footer-section">
		    <div class="container">
		      	<div class="row">

		      		<!-- Start Column 1 -->
					<div class="col-12 col-md-4 col-lg-3 mb-5"
                    v-for="product in productStore.product_data" v-bind:key="product.id">
						<a class="product-item" href="#">
							<img :src="product.img" class="img-fluid product-thumbnail">
							<h3 class="product-title">{{ product.name }}</h3>
							<strong class="product-price">&#8358; {{ product.price }}</strong>

							<span class="icon-cross">
								<img :src="product.img" class="img-fluid">
							</span>
						</a>
					</div> 
					<!-- End Column 1 -->
						

		      	</div>
		    </div>
		</div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useProductStore } from '@/stores/product';
const productStore = useProductStore();
onMounted(() => {
    productStore.getProducts()
});

const products = ref();
</script>