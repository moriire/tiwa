<script setup>
import { ref } from "vue";
import { useAuthStore } from "@/stores/auth"
//import alertifyjs from '@/alertifyjs';
import { useRoute } from "vue-router";
const options = ref([]);
//const options = options;
const category = ref('');
const controls = {
        rtl: false,
        customColor: false,
        disabled: false
      };
const labelsType = ref(1);
const route = useRoute();
const stores = useAuthStore();
const loginAction = async () => {
  await stores.login(stores.loginForm.email, stores.loginForm.password)
};
const onSelected=(category)=> {
      category = category.value;
    }
</script>

<template>
<div style="display:flex; flex-direction: row; justify-content:center; min-height: 60vh; align-items:center;">
  <ui-form item-margin-bottom="16" label-width="80" >
    <ui-form-field>
        <ui-select outlined
        id="full-func-js-select"
        v-model="category"
        :options="options"
        :class="{ 'demo-select-custom-colors': controls.customColor }"
        :disabled="controls.disabled"
        @selected="onSelected($event)"
        >
            
        </ui-select>
    </ui-form-field>
  <ui-form-field>
      <ui-textfield outlined input-type="text"
        required
        v-model="name"
        helper-text-id="pw-validation-msg"
        :attrs="{autocomplete: 'product-name'}">
        Product Name:
      </ui-textfield>
    </ui-form-field>
    <ui-form-field>
      <ui-textfield outlined input-type="Number"
        required
        v-model="price"
        pattern=".{8,}"
        helper-text-id="pw-validation-msg"
        :attrs="{autocomplete: 'price'}">
        Product Price
      </ui-textfield>
    </ui-form-field>
    <ui-form-field>
        <!--ui-slider v-model="value3" type="discrete" :step="10"></ui-slider-->
        <ui-slider
        v-model="discount"
        type="discrete"
        :step="10"
        with-tick-marks
        ></ui-slider>
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