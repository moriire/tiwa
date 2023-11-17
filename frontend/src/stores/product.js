import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import router from "@/router";
import { useAuthStore } from './auth'
import axios from 'axios';

const BASE = import.meta.env.VITE_BACKEND_API_URL;
export const useProductStore = defineStore('product', () => {
    const category_data = ref({ category:"", name:"", discount: 0, price: 0 });
    const product_data = ref({});
  const categories = ref([]);
  const options  = computed(() => categories.value.map(x=>{
    return {label: x.name, value: x.id}
  }
  ))
	const CreateProduct = async ()=>{
    const auth = JSON.parse(localStorage.getItem("user"))
		try {
      if(auth.user){
        category_data.value["user"]= auth.user.id
      }else{
        alert("you need to login first")
      }
			const res = await axios.post(`${BASE}/api/product/`, category_data.value)
			console.log(res.data);
      router.push("/upload");
		} catch(errors){
			console.log(errors)
			//return errors.response
		}
	};

    const getProducts = async ()=>{
        const auth = JSON.parse(localStorage.getItem("user"))
            try {
    
                const res = await axios.get(`${BASE}/api/products/`)
                product_data.value = res.data
            } catch(errors){
                console.log(errors)
                //return errors.response
            }
        };
        const selectedProducts = ref([]);
        const selectedCount = ref(0);
        const selectProduct = (d) => {
            selectedProducts.value.push(d)
            selectedCount.value=+new Set(selectedProducts.value).size
        };

        const singleProductItem = ref({
          product:{},
          images: [],
          category:{}
        });
        const getSingleProduct = async (pk)=>{
          //const auth = JSON.parse(localStorage.getItem("user"))
              try {
                  const res = await axios.get(`${BASE}/api/products/${pk}/`)
                  singleProductItem.value = await res.data
                  //alert(singleProductItem)
              } catch(errors){
                  console.log(errors)
                  alert(errors)
                  //return errors.response
              }
          };

  return { CreateProduct, getProducts, category_data, product_data, selectedProducts, selectedCount, selectProduct, getSingleProduct, singleProductItem }
})
