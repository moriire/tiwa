<script setup>
import { ref } from "vue";
import { useAuthStore } from "@/stores/auth"
//import alertifyjs from '@/alertifyjs';
import { useRoute, RouterLink } from "vue-router";
const labelsType = ref(1);
const route = useRoute();
const stores = useAuthStore();
const loginAction = async () => {
  await stores.login(stores.loginForm.email, stores.loginForm.password)
}
</script>

<template>
  <div class="grid  justify-content-center align-items-center" style="height:90vh;">
     <div class="card col-lg-6 col-sm-10 col-xs-12 p-5">
      
      <div class="p-inputgroup flex-1" style="margin:10px 0;">
        <span class="p-inputgroup-addon">
                <i class="pi pi-user"></i>
        </span>  
        <InputText placeholder="Email" v-model="stores.loginForm.email" />
      </div>
    
      <div class="p-inputgroup flex-1" style="margin:10px 0;">
        <span class="p-inputgroup-addon">
                <i class="pi pi-lock"></i>
        </span>  
        <Password placeholder="Enter Password" v-model="stores.loginForm.password" toggleMask  />
      </div>
      <div class="p-inputgroup flex-1" style="margin:10px 0;">
          <Button type="submit" label="login" @click="loginAction()" raised />
      </div>
      <div class="col-12">
        Dont have an account? <RouterLink to="register"> Sign up</RouterLink>
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