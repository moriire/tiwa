<template>
<!-- Start Popular Product -->
<div class="popular-product mb-2">
			<div class="container">
				<div class="row">

					<div 
                    v-for="cat in categoryStore.categories"
                    v-bind:key="cat.id"
                    class="col-12 col-md-6 col-lg-4 mb-4 mb-lg-0">
						<div class="product-item-sm d-flex">
							<div class="thumbnail">
								<img :src="cat.thumb" alt="Image" class="img-fluid">
								<!--img src="/src/assets/images/product-1.png" alt="Image" class="img-fluid"-->
							</div>
							<div class="pt-3">
								<h3>{{ cat.name }}</h3>
								<p>{{ cat.desc || 'No description assined to catgory!!!' }} </p>
								<p><a href="#">View Products</a></p>
							</div>
						</div>
					</div>

					<div class="col-12 col-md-6 col-lg-4 mb-4 mb-lg-0">
						<div class="product-item-sm d-flex">
							<div class="thumbnail">
								<img src="/src/assets/images/product-3.png" alt="Image" class="img-fluid">
							</div>
							<div class="pt-3">
								<h3>Ergonomic Chair</h3>
								<p>Donec facilisis quam ut purus rutrum lobortis. Donec vitae odio </p>
								<p><a href="#">Read More</a></p>
							</div>
						</div>
					</div>

				</div>
			</div>
		</div>
		<!-- End Popular Product -->

</template>
<script setup>
import { useCategoryStore } from "@/stores/categories";
const categoryStore = useCategoryStore()
</script>