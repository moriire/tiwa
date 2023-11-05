<script setup>
import {onMounted, ref, computed } from "vue";
import { useAuthStore } from "@/stores/auth"
//import alertifyjs from '@/alertifyjs';
import { useCategoryStore } from "@/stores/categories"
import { useProductStore } from "@/stores/product"
import { useRoute } from "vue-router";
const discount = ref(0);
//const options = ref([]);
const category = ref('');
const controls = {
        rtl: false,
        customColor: false,
        disabled: false
      };
const labelsType = ref(1);
const route = useRoute();
const stores = useAuthStore();
const productStore = useProductStore()
const cats = useCategoryStore();
const loginAction = async () => {
  await stores.login(stores.loginForm.email, stores.loginForm.password)
};
const onSelected=(category)=> {
      category = category.value
    }
onMounted(()=>{
  productStore.getProducts()
  cats.getCategories()
})
</script>

<template>

  <div class="grid  justify-content-center m-4 p-4" style="height:90vh;">
     <div class="card col-lg-6 col-sm-10 col-xs-12 p-5">
      
      <div class="p-inputgroup flex-1" style="margin:10px 0;">
        <TreeSelect v-model="category" :options="cats.options" placeholder="Select Category" class="md:w-20rem w-full" />
      </div>
      
      <div class="p-inputgroup flex-1" style="margin:10px 0;">
         
          <InputText placeholder="Product Name" v-model = "stores.detail.name"/>
      </div>
      <div class="p-inputgroup flex-1" style="margin:10px 0;">
          <span class="p-inputgroup-addon">&#8358;</span>
          <InputNumber placeholder="Price" v-model = "stores.detail.price" />
          <span class="p-inputgroup-addon">.00</span>
      </div>
      <div class="p-inputgroup flex-1" style="margin:10px 0;">
          <span class="p-inputgroup-addon">$</span>
          <InputNumber placeholder="Discount" v-model = "stores.detail.discount" />
          <span class="p-inputgroup-addon">%</span>
      </div>
      <div class="p-inputgroup flex-1" style="margin:10px 0;">
          <Textarea placeholder="Product Description" />
      </div>
      <div class="p-inputgroup flex-1" style="margin:10px 0;">
          
          <InputSubmit  />
      </div>
      <div class="p-inputgroup flex-1" style="margin:10px 0;">
          <Button type="submit" label="Create Product" @click="cats.CreateProduct()" raised />
      </div>
  </div>
  <div class="card col-lg-6 col-sm-10 col-xs-12 .align-items-center p-5">
      <DataTable :value="productStore.product_data" tableStyle="min-width: 50rem">
          <Column field="name" header="Name"></Column>
          <Column field="category.name" header="Category"></Column>
          <Column field="price" header="Price"></Column>
          <Column field="discount" header="Discount"></Column>
      </DataTable>
  </div>
 
  </div>  
</template>

<style scoped >

</style>

