<script setup>
import { ref } from "vue";
const labelsType = ref(1);
    

</script>

<template>
  <ui-grid class=".demo-grid" align="middle" style="background-color:blue">
    <ui-grid-cell class="demo-cell" v-shadow="4" columns="3">
      <ui-form nowrap item-margin-bottom="10" label-width=".90">
        <template #default="{ subitemClass, actionClass }">
          
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
          <ui-form-field>
            <ui-textfield outlined input-type="password"
              required
              pattern=".{8,}"
              helper-text-id="pw-validation-msg"
              :attrs="{autocomplete: 'confirm-password'}">
              Confirm Password
            </ui-textfield>
          </ui-form-field>
          <ui-form-field :class="actionClass">
            <ui-button raised>Submit</ui-button>
            <!--ui-button outlined>Cancel</ui-button-->
          </ui-form-field>
        </template>
      </ui-form>
    </ui-grid-cell>
    <ui-grid-cell class="demo-cell" v-shadow="4" columns="3">
      <ui-form nowrap item-margin-bottom="10" label-width=".90">
        <template #default="{ subitemClass, actionClass }">
          
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
          <ui-form-field>
            <ui-textfield outlined input-type="password"
              required
              pattern=".{8,}"
              helper-text-id="pw-validation-msg"
              :attrs="{autocomplete: 'confirm-password'}">
              Confirm Password
            </ui-textfield>
          </ui-form-field>
          <ui-form-field :class="actionClass">
            <ui-button raised>Submit</ui-button>
            <!--ui-button outlined>Cancel</ui-button-->
          </ui-form-field>
        </template>
      </ui-form>
    </ui-grid-cell>
  </ui-grid>


</template>
<style scoped>
div.demo-grid {
  
}
div.demo-cell{
  padding: 30px;
  display: inline-flex;
  justify-content:center
}
</style>