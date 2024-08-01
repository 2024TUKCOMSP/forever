import './assets/css/index.css';
import './assets/css/tailwind.css';
import '@fortawesome/fontawesome-free/js/all.js'

import { createApp } from 'vue'
import { createPinia } from 'pinia';
import App from './App.vue'
import router from './router';

const app = createApp(App);


app.config.globalProperties.$isVisibleNotYetTask = true;
app.config.globalProperties.$isVisibleTodayTask = true;
app.config.globalProperties.$isVisibleSomeTask = true;

app.config.globalProperties.$postScreenMode = "Light";

app.use(createPinia());
app.use(router);

app.mount('#app');


