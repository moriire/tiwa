//import './assets/main.css'

import App from "./App.vue";
import { createApp } from 'vue'
//import PrimeVue from 'primevue/config';
import { createPinia } from 'pinia'
import router from "./router";

const app = createApp(App)
app.use(createPinia())
app.use(router)

app.mount('#app')
