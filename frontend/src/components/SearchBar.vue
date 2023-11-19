<template>
    <!-- Start Main Menu Search -->
    <div class="main-menu-search">
                            <!-- navbar search start -->
                            <div class="navbar-search search-style-5">
                                <div class="search-select">
                                    <div class="select-position">
                                        <select id="select1" v-model="category">
                                            <option selected disabled>All</option>
                                            <option :value="cat.id" v-for="cat in categoryStore.categories" v-bind:key="cat.id">{{ cat.name }}</option>
                                        </select>
                                    </div>
                                </div>
                                <div class="search-input">
                                    <input type="text" placeholder="Search" v-model="product">
                                </div>
                                <div class="search-btn">
                                    <button  @click="console.log('hello')"><i class="lni lni-search-alt"></i></button>
                                </div>
                            </div>
                            <!-- navbar search Ends -->
                        </div>
                        <!-- End Main Menu Search -->
</template>
<script setup>
import { useCategoryStore } from "@/stores/categories";
import { ref } from "vue";
const categoryStore = useCategoryStore();
const category = ref("")
const product = ref("")
</script>