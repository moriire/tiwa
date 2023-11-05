<script setup>
import { ref, onMounted } from "vue";
import { useAuthStore } from "@/stores/auth"
//import alertifyjs from '@/alertifyjs';
import { useRoute } from "vue-router";
const labelsType = ref(1);
//const route = useRoute();
const stores = useAuthStore();
//console.log(stores.user.access)
onMounted(()=>{
    stores.getUserProfile()
})
</script>

<template>
  <div class="grid  justify-content-center m-4 p-4" style="height:90vh;">
     <div class="card col-lg-6 col-sm-10 col-xs-12 p-5">
      
      <div class="p-inputgroup flex-1" style="margin:10px 0;">
          <InputText placeholder="Email" v-model = "stores.detail.email" />
      </div>
     <div class="p-inputgroup flex-1" style="margin:10px 0;">
         
         <InputText placeholder="Last Name" v-model = "stores.detail.first_name"/>
     </div>
      <div class="p-inputgroup flex-1" style="margin:10px 0;">
          <InputText placeholder="Last Name" v-model = "stores.detail.last_name" />
      </div>
      <div class="p-inputgroup flex-1" style="margin:10px 0;">
          <Button type="submit" label="Create Product" @click="stores.updateProfile(stores.detail)" raised />
      </div>
  </div>
  </div> 
</template>
<style scoped >
.row {
  display: flex;
  flex-direction: row;
  justify-content: center
}
</style>