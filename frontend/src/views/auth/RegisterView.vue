<script setup>
import { ref } from "vue";
import { useAuthStore } from "@/stores/auth"
//import alertifyjs from '@/alertifyjs';
import { useRoute } from "vue-router";
const labelsType = ref(1);
const route = useRoute();
const stores = useAuthStore();
const regAction = async () => {
  await stores.register({email: stores.regForm.email, password1: stores.regForm.password1, password2: stores.regForm.password2})
}
</script>
<template>
<div class="grid  justify-content-center align-items-center" style="height:90vh;">
     <div class="card col-lg-6 col-sm-10 col-xs-12 p-5">
      <div class="p-inputgroup flex-1" style="margin:10px 0;">
         
         <InputText placeholder="First Name" v-model="stores.regForm.first_name"/>
     </div>
      <div class="p-inputgroup flex-1" style="margin:10px 0;">
          <InputText placeholder="Last Name" v-model = "stores.regForm.last_name" />
      </div>
      <div class="p-inputgroup flex-1" style="margin:10px 0;">
       
        <InputText placeholder="Email" v-model="stores.regForm.email" />
      </div>
      <div class="p-inputgroup flex-1" style="margin:10px 0;">
        
        <Password placeholder="Password" v-model="stores.regForm.password1" toggleMask  />
      </div>
      <div class="p-inputgroup flex-1" style="margin:10px 0;">
        
        <Password placeholder="Confirm Password" v-model="stores.regForm.password2" toggleMask  />
      </div>
      <div class="p-inputgroup flex-1" style="margin:10px 0;">
          <Button type="submit" label="Sign up" @click="regAction()" raised />
      </div>
      <div class="col-12">
        Already have an account? <RouterLink to="login">Login</RouterLink>
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