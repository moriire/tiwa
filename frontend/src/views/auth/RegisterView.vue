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
<div style="display:flex; flex-direction: row; justify-content:center; min-height: 60vh; align-items:center;">
  <ui-form item-margin-bottom="16" label-width="80">
  <ui-form-field>
      <ui-textfield outlined input-type="email"
        v-model = "stores.regForm.email"
        required
        helper-text-id="pw-validation-msg"
        :attrs="{autocomplete: 'email'}">
        Email
      </ui-textfield>
    </ui-form-field>
    <ui-form-field>
      <ui-textfield outlined input-type="password"
        required
        v-model="stores.regForm.password1"
        pattern=".{8,}"
        helper-text-id="pw-validation-msg"
        :attrs="{autocomplete: 'current-password'}">
        Password
      </ui-textfield>
    </ui-form-field>
    <ui-form-field>
      <ui-textfield outlined input-type="password"
      v-model="stores.regForm.password2"
        required
        pattern=".{8,}"
        helper-text-id="pw-validation-msg"
        :attrs="{autocomplete: 'password'}">
        Confirm Password
      </ui-textfield>
    </ui-form-field>
    <ui-form-field :class="actionClass">
      <ui-button raised @click="regAction()">Submit</ui-button>
      <!--ui-button outlined>Cancel</ui-button-->
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