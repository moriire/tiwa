//import './assets/main.css'
import 'balm-ui/dist/balm-ui.css'; // Import BalmUI CSS
import 'balm-ui/dist/balm-ui.css'; // Import BalmUI CSS
import BalmUI from 'balm-ui'; // Official Google Material Components
import BalmUIPlus from 'balm-ui/dist/balm-ui-plus'; // BalmJS Team Material Components
import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
const app = createApp(App)

app.use(BalmUI); // Mandatory
app.use(BalmUIPlus); // Optional

app.use(createPinia())
app.use(router)

app.mount('#app')
