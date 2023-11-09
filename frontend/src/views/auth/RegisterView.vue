<script setup>
import { ref } from "vue";
import { useAuthStore } from "@/stores/auth"
//import alertifyjs from '@/alertifyjs';
import { RouterLink, useRoute } from "vue-router";
const labelsType = ref(1);
const route = useRoute();
const stores = useAuthStore();
const regAction = async () => {
  await stores.register({email: stores.regForm.email, password1: stores.regForm.password1, password2: stores.regForm.password2})
}
</script>
<template>
<div class="container">
      <div class="row justify-content-center align-items-center vh-100">


        <div class="card col-md-4 col-lg-6  bg-dark p-4">
          <h2 class="text-center text-light">Sign up</h2>
          <form @submit.prevent="regAction()">
            <div class="row">
              <div class="col-6">
                <div class="form-group">
                  <input type="text" class="form-control" placeholder="First Name" id="fname" v-model = "stores.regForm.first_name" required>
                </div>
              </div>
              <div class="col-6">
                <div class="form-group">
                  <input type="text" class="form-control" placeholder="Last Name" id="lname" v-model = "stores.regForm.last_name" required>
                </div>
              </div>
            </div>
            <div class="form-group mt-4">
              <input type="email" class="form-control" id="email" placeholder="Email" v-model = "stores.regForm.email" required>
            </div>
            <div class="form-group mt-4">
              <input type="password" class="form-control" id="password1" placeholder="Password" v-model = "stores.regForm.password1" required>
            </div>
            <div class="form-group mt-4">
              <input type="password" class="form-control" id="password2" placeholder="Confirm Password" v-model = "stores.regForm.password1" required>
            </div>
            <div class="form-group mt-4 text-center">
              <button type="submit" class="btn btn-primary-hover-outline btn-primary"  >Register</button>
            </div>
            <div class="form-group mt-4 text-center text-light">Already have an account? <span> <RouterLink class="text-decoration-none" :to="{name:'login'}" >Login</RouterLink></span></div>
          </form>

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