import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue';
import AddProductView from '../views/AddProductView.vue'
import ProductsByCategoryView from '../views/ProductsByCategoryView.vue';
import ProductsView from "../views/ProductsView.vue";
import UploadView from '../views/UploadView.vue'
import {LoginView, RegisterView, ProfileView} from '../views/auth';
import { useAuthStore } from '@/stores/auth';
 
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView,
      meta: { requiresAuth: true },
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/add-product',
      name: 'add-product',
      component: AddProductView,
      meta: { requiresAuth: true },
    },
    {
      path: '/products',
      name: 'products',
      //component: ProductsByCategoryView,
      component: ProductsView,
      meta: { requiresAuth: true },
    },
    {
      path: '/upload',
      name: 'upload',
      component: UploadView,
      meta: { requiresAuth: true },
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue'),
    }
  ]
})

export default router
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !useAuthStore().isAuthenticated) {
    next('/login');
  } else {
    next();
  }
});