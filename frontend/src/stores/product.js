import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import router from "@/router";
import { useAuthStore } from './auth'
import axios from 'axios';
const BASE = "http://127.0.0.1:8000";
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
    
                const res = await axios.get(`${BASE}/api/product/`)
                product_data.value = res.data
            } catch(errors){
                console.log(errors)
                //return errors.response
            }
        };
  return { CreateProduct, getProducts, category_data, product_data }
})
