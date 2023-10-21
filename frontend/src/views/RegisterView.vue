<script setup>
import { ref } from "vue";
const labelsType = ref(1);
    

</script>

<template>
<div style="display:flex; flex-direction: row; justify-content:center; min-height: 60vh; align-items:center;">
  <ui-form item-margin-bottom="16" label-width="80">
  <ui-form-field>
      <ui-textfield outlined input-type="email"
        required
        helper-text-id="pw-validation-msg"
        :attrs="{autocomplete: 'email'}">
        Email
      </ui-textfield>
    </ui-form-field>
    <ui-form-field>
      <ui-textfield outlined input-type="password"
        required
        pattern=".{8,}"
        helper-text-id="pw-validation-msg"
        :attrs="{autocomplete: 'current-password'}">
        Password
      </ui-textfield>
    </ui-form-field>
    <ui-form-field :class="actionClass">
      <ui-button raised>Submit</ui-button>
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