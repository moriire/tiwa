<script setup>
import { ref } from "vue";
import { useAuthStore } from "@/stores/auth"
import { useRoute, RouterLink } from "vue-router";
const labelsType = ref(1);
const route = useRoute();
const stores = useAuthStore();
const loginAction = async () => {
  await stores.login(stores.loginForm.email, stores.loginForm.password)
}
</script>

<template>
   <div class="container">
      <div class="row justify-content-center align-items-center vh-100">


        <div class="card col-md-4 col-lg-6 col-10 bg-dark p-4">
          <h2 class="text-center text-light">Login</h2>
          <form @submit.prevent="loginAction()" >
          
            <div class="form-group">
              <!--label class="text-black" for="email">Email Address</label-->
              <input type="email" class="form-control" id="email" placeholder="Email" v-model="stores.loginForm.email" required>
            </div>
            <div class="form-group mt-4">
              <!--label class="text-black" for="password2">Password</label-->
              <input type="password" class="form-control" id="password" placeholder="Password" v-model = "stores.regForm.password1" required >
            </div>
            <div class="form-group mt-2 text-end">
              <RouterLink class="text-decoration-none" :to="{name:'register'}" >Forgot Password ?</RouterLink>
            </div>
            <div class="form-group mt-4 text-center">
              <button type="submit" class="btn btn-primary-hover-outline btn-primary mx-auto px-auto"  >Login</button>
            </div>
            <div class="form-group mt-4 text-center text-light">Don't have an account yet? <span> <RouterLink class="text-decoration-none" :to="{name:'register'}" >Sign up</RouterLink></span></div>
          </form>

        </div>

      </div>

</div>
</template>

<style scoped >
</style>