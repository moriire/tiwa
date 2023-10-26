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
<div style="display:flex; flex-direction: row; justify-content:center; min-height: 60vh; align-items:center;">
  <ui-form item-margin-bottom="16" label-width="80">
  <ui-form-field>
      <ui-textfield outlined input-type="email"
        v-model = "stores.detail.email"
        required
        readonly
        helper-text-id="pw-validation-msg"
        :attrs="{autocomplete: 'email'}">
        Email
      </ui-textfield>
    </ui-form-field>
    <ui-form-field>
      <ui-textfield outlined input-type="text"
        required
        v-model="stores.detail.first_name"
        helper-text-id="pw-validation-msg"
        :attrs="{autocomplete: 'first-name'}">
        Fisrt Name:
      </ui-textfield>
    </ui-form-field>
    <ui-form-field>
      <ui-textfield outlined input-type="text"
      v-model="stores.detail.last_name"
        required
        helper-text-id="pw-validation-msg"
        :attrs="{autocomplete: 'last-name'}">
        Last Name:
      </ui-textfield>
    </ui-form-field>
    <ui-form-field :class="actionClass">
      <ui-button raised @click="stores.updateProfile(stores.detail)">Update Profile</ui-button>
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