<script >
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
export default {
  data() {
    return {
      type: 0,
      title: 'Tiwa',
      openDrawer: false,
      items: [
        {
          text: 'Home',
          icon: 'favorite',
          url: '/',
          name: "home"
        },
        {
          text: 'Music',
          icon: 'music_note',
          url: '/about',
          name: "login"
        },
        {
          text: 'Places',
          icon: 'place',
          name: "home"
        },
        {
          text: 'News',
          icon: 'fiber_new',
          name: "register"
        }
      ],
      active: 1
    };
  },
  methods: {
    onChange(active) {
      console.log(active);
      this.$router.push({
  name: this.items[active].name,
  // preserve current path and remove the first char to avoid the target URL starting with `//`
  //params: { pathMatch: this.$route.path.substring(1).split('/') },
  // preserve existing query and hash if any
  //query: this.$route.query,
})
    }
  }
};
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
      <ui-icon-button
        :class="toolbarItemClass"
        icon="bookmark"
      ></ui-icon-button>
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
        <ui-item>
          <ui-item-first-content>
            <ui-icon>home</ui-icon>
          </ui-item-first-content>
          <ui-item-text-content>Home</ui-item-text-content>
        </ui-item>
        <ui-list-divider></ui-list-divider>
        <ui-item>
          <ui-item-first-content>
            <ui-icon>profile</ui-icon>
          </ui-item-first-content>
          <ui-item-text-content>Profile</ui-item-text-content>
        </ui-item>
        <ui-list-divider></ui-list-divider>
        <ui-item>
          <ui-item-first-content>
            <ui-icon>settings</ui-icon>
          </ui-item-first-content>
          <ui-item-text-content>Settings</ui-item-text-content>
        </ui-item>
        <ui-list-divider></ui-list-divider>
        <ui-item active>
          <ui-item-first-content>
            <ui-icon>arrow_back</ui-icon>
          </ui-item-first-content>
          <ui-item-text-content>Back</ui-item-text-content>
        </ui-item>
        <ui-list-divider></ui-list-divider>
        <ui-item active>
          <ui-item-first-content>
            <ui-icon>arrow_back</ui-icon>
          </ui-item-first-content>
          <ui-item-text-content>Back</ui-item-text-content>
        </ui-item>
        <ui-list-divider></ui-list-divider>
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