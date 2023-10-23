<script setup>
import { ref } from "vue";
import { useAuthStore } from "@/stores/auth"
//import alertifyjs from '@/alertifyjs';
import { useRoute } from "vue-router";
const labelsType = ref(1);
const route = useRoute();
const stores = useAuthStore();
const loginAction = async () => {
  await stores.login(stores.loginForm.email, stores.loginForm.password)
}
</script>

<template>
<div style="display:flex; flex-direction: row; justify-content:center; min-height: 60vh; align-items:center;">
  <ui-form item-margin-bottom="16" label-width="80" >
  <ui-form-field>
      <ui-textfield outlined input-type="email"
        required
        v-model="stores.loginForm.email"
        helper-text-id="pw-validation-msg"
        :attrs="{autocomplete: 'email'}">
        Email
      </ui-textfield>
    </ui-form-field>
    <ui-form-field>
      <ui-textfield outlined input-type="password"
        required
        v-model="stores.loginForm.password"
        pattern=".{8,}"
        helper-text-id="pw-validation-msg"
        :attrs="{autocomplete: 'current-password'}">
        Password
      </ui-textfield>
    </ui-form-field>
    <ui-form-field >
      <ui-button raised @click="loginAction()">Submit</ui-button>
      <ui-button outlined>Cancel</ui-button>
    </ui-form-field>
  </ui-form>
</div>
</template>

<style scoped >
.row {
  display: flex;
  flex-direction: row;
  justify-content: center
}
</style>