<script setup>
import { ref } from "vue";
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { useAuthStore } from "@/stores/auth";
const router = useRouter();
      const type = 0;
      const title = "Tiwa 'n' Tiwa";
      const openDrawer = ref(false);
      const sidebar =  [
        {
          text: 'Home',
          icon: 'favorite',
          name: "home",
          auth: true
        },
        {
          text: 'Profile',
          icon: 'profile',
          name: "profile",
          auth: true
        },
        {
          text: 'Settings',
          icon: 'settings',
          name: "register",
          auth: true
        },
        {
          text: 'Sign up',
          icon: 'login',
          name: "register",
          auth: false
        },
        {
          text: 'Login',
          icon: 'fiber_new',
          name: "login",
          auth: false
        },
        {
          text: 'Forgot Password',
          icon: 'fiber_new',
          name: "about",
          auth: false
        },
        {
          text: 'About',
          icon: 'fiber_new',
          name: "about",
          auth: false
        },
      ];
      const items =  [
        {
          text: 'Home',
          icon: 'favorite',
          name: "home"
        },
        {
          text: 'For Sale',
          icon: 'category',
          name: "products"
        },
        {
          text: 'Sell',
          icon: 'store_front',
          name: "add-product"
        },
        {
          text: 'Dashboard',
          icon: 'dashboard',
          name: "register"
        }
      ];
      const active = ref(0);
    const logout = () => {
      useAuthStore().logout()
    };
    const onChange = (active) => {
      console.log(active);
      router.push({
  name: items[active].name,
  // preserve current path and remove the first char to avoid the target URL starting with `//`
  //params: { pathMatch: this.$route.path.substring(1).split('/') },
  // preserve existing query and hash if any
  //query: this.$route.query,
})
    }
</script>

<template>
  <div class="page-top-app-bar">
  <ui-top-app-bar
    content-selector="#content-main"
    :type="type"
    :title="title"
    @nav="openDrawer = true"
  >
    <template #toolbar="{ toolbarItemClass }">
      <ui-icon-button
        :class="toolbarItemClass"
        icon="file_download"
      ></ui-icon-button>
      <ui-icon-button :class="toolbarItemClass" icon="print"></ui-icon-button>
      <!--ui-icon-button
        :class="toolbarItemClass"
        icon="bookmark"
      ></ui-icon-button-->
    </template>
  </ui-top-app-bar>

  <ui-drawer v-model="openDrawer" type="modal">
    <ui-drawer-header>
      <ui-drawer-title>Tiwa-Our Culture</ui-drawer-title>
    </ui-drawer-header>
    <ui-drawer-content>
      <ui-list>
        <ui-item active>
          <ui-item-first-content>
            <ui-icon>arrow_back</ui-icon>
          </ui-item-first-content>
          <ui-item-text-content>Back</ui-item-text-content>
        </ui-item>
        <ui-list-divider></ui-list-divider>
        <div v-for="(bar, index) in sidebar" v-bind:value="index" v-show="useAuthStore().isAuthenticated==bar.auth">
        <ui-item>
          <router-link :to="{name: bar.name}">
          <ui-item-first-content>
            <ui-icon>{{bar.icon}}</ui-icon>
          </ui-item-first-content>
          <ui-item-text-content>{{ bar.text }}</ui-item-text-content>
          
          </router-link>
        </ui-item>
        <ui-list-divider></ui-list-divider>
        </div>

        <div v-if="useAuthStore().isAuthenticated">
        <ui-item @click="logout()">
          <ui-item-first-content>
            <ui-icon>logout</ui-icon>
          </ui-item-first-content>
          <ui-item-text-content>Logout</ui-item-text-content>
        </ui-item>
        <ui-list-divider></ui-list-divider>
        </div>
      </ui-list>
    </ui-drawer-content>
  </ui-drawer>

  <div id="content-main">
    <div class="container">
      <!-- Content -->

      <ui-navigation-bar content-selector=".container" stacked>
        <ui-tabs
          v-model="active"
          type="textWithIcon"
          :items="items"
          stacked
          @update:model-value="onChange"
        ></ui-tabs>
      </ui-navigation-bar>
    </div>
    <RouterView />
  </div>
</div>

</template>
<style scoped>
</style>