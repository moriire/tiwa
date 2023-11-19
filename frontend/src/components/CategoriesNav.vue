<template>
<div class="mega-category-menu">
                            <span class="cat-button"><i class="lni lni-menu"></i>All Categories</span>
                            <ul class="sub-category">
                                <li  v-for="cat in categoryStore.categories" v-bind:key="cat.id">
                                    <RouterLink :to="{'name': 'products-by-category', 'params': {'category':cat.name}}">{{ cat.name }}</RouterLink>  
                                </li>
                            </ul>
                        </div>
</template>
<script setup>
import { useCategoryStore } from "@/stores/categories";
const categoryStore = useCategoryStore()
</script>