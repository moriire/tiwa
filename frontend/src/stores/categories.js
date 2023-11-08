import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import router from "@/router";
import { useAuthStore } from './auth'
import axios from 'axios';

const BASE = import.meta.env.VITE_BACKEND_API_URL;
export const useCategoryStore = defineStore('categories', () => {
  const category_data = ref({ category:"", name:"", discount: 0, price: 0 });
  const categories = ref([]);
  const options  = computed(() => categories.value.map(x=>{
    return {label: x.name, value: x.id}
  }
  ))
  const getCategories = async () => {
    try {
      const res = await axios.get(`${BASE}/api/category/`)
      categories.value = res.data
      console.log(options.value)
    } catch(error){
      console.log(error)
    }
  };

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
  return { getCategories, CreateProduct, categories, options, category_data, options }
})
