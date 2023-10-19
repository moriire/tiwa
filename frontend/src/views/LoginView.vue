<script setup>
import { ref } from "vue";
const labelsType = ref(1);
    

</script>

<template>
 <ui-form nowrap item-margin-bottom="16" label-width="80" center>
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
    <ui-form-field :class="actionClass">
      <ui-button raised>Submit</ui-button>
      <!--ui-button outlined>Cancel</ui-button-->
    </ui-form-field>
  </template>
</ui-form>

</template>
<style scoped lang="scss">
@use '@material/image-list' with (
  $standard-gutter-size: 4px,
  $masonry-gutter-size: 16px,
  $icon-size: 24px,
  $text-protection-background-color: rgba(0, 0, 0, 0.6),
  $text-protection-height: 48px,
  $text-protection-horizontal-padding: 16px,
  $shape-radius: 0
);

</style>