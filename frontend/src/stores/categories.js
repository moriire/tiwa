import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useAuthStore } from './auth'
import axios from 'axios';
const BASE = "http://127.0.0.1:8000";
export const useCategoryStore = defineStore('category', () => {
  //const count = ref(0)
  const categoryData = ref([])
  const auth = useAuthStore()
  //const doubleCount = computed(() => count.value * 2)

  const categories = async () => {
    try{
      const res = await axios.get(`${BASE}/api/category/`)
      categoryData.value = res.data
      console.log(categoryData.value)
    } catch(error){
      console.log(error)
    }
   
  };
  
  return { categories, categoryData }
})
