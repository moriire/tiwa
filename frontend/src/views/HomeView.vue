<template>
  <swiper
    :effect="'coverflow'"
    :grabCursor="true"
    :centeredSlides="true"
    :slidesPerView="'auto'"
    :coverflowEffect="{
      rotate: 50,
      stretch: 0,
      depth: 100,
      modifier: 1,
      slideShadows: true,
    }"
    :pagination="true"
    :modules="modules"
    class="mySwiper"
  >
    <swiper-slide v-for="cat in category.categories" v-bind:key="cat.id">
      <router-link :to="{name:'upload'}">
      <img :src="cat.thumb" />
      </router-link>
    </swiper-slide>
  </swiper>
</template>
<script>
  // Import Swiper Vue.js components
  import { Swiper, SwiperSlide } from 'swiper/vue';
import { onMounted } from "vue";
  import 'swiper/css';

  import 'swiper/css/effect-coverflow';
  import 'swiper/css/pagination';
import { useCategoryStore } from "@/stores/categories";
  import { EffectCoverflow, Pagination } from 'swiper/modules';

  export default {
    components: {
      Swiper,
      SwiperSlide,
    },
    setup() {
      const category = useCategoryStore();
      onMounted(()=>{
        category.getCategories()
      })
      return {
        category,
        cats: category.categories,
        modules: [EffectCoverflow, Pagination],
      };
    },
  };
</script>
<style>
#app { height: 100% }
html,
body {
  position: relative;
  height: 100%;
}

body {
  background: #eee;
  font-family: Helvetica Neue, Helvetica, Arial, sans-serif;
  font-size: 14px;
  color: #000;
  margin: 0;
  padding: 0;
}

.swiper {
  width: 100%;
  padding-top: 50px;
  padding-bottom: 50px;
}

.swiper-slide {
  background-position: center;
  background-size: cover;
  width: 300px;
  height: 300px;
}

.swiper-slide img {
  display: block;
  width: 100%;
}

</style>