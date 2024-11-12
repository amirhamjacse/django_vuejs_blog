<script setup>
import NavigationBar from '@/components/NavigationBar.vue';
import FooterDesign from '@/components/FooterDesign.vue';
</script>

<template>
  <NavigationBar></NavigationBar>
  <div class="container my-5">
    <div class="text-center mb-4">
      <h1>Welcome to My Blog</h1>
      <p class="lead">Latest Posts and Updates</p>
    </div>

    <!-- Blog Post List -->
    <div class="row">
      <div v-for="(post, index) in paginatedPosts" :key="index" class="col-md-4 p-4">
        <div class="row">            
          <div v-if="post" class="card">
            <div class="card-body">
              <h5 class="card-title"> {{ post.title }}</h5>
              <img class="p-2" src="https://i.ibb.co/cyy9gTH/blog-camtasia-youtube-thumbnails-1500x1100.png" width="350px;">
              <router-link :to="'/details/' + post.id" class="btn btn-primary mt-2">Read More</router-link>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Pagination -->
    <nav aria-label="Page navigation">
      <ul class="pagination justify-content-center">
        <li class="page-item" :class="{ disabled: currentPage === 1 }">
          <a class="page-link" href="#" @click.prevent="changePage(currentPage - 1)">Previous</a>
        </li>
        <li v-for="page in totalPages" :key="page" class="page-item" :class="{ active: currentPage === page }">
          <a class="page-link" href="#" @click.prevent="changePage(page)">{{ page }}</a>
        </li>
        <li class="page-item" :class="{ disabled: currentPage === totalPages }">
          <a class="page-link" href="#" @click.prevent="changePage(currentPage + 1)">Next</a>
        </li>
      </ul>
    </nav>
  </div>
  <FooterDesign></FooterDesign>
</template>

<script>
import axios from 'axios';
const apiUrl = import.meta.env.VITE_API_URL;

export default {
  data() {
    return {
      blog_data: { results: [] },
      currentPage: 1,
      itemsPerPage: 6,
      totalPages: 1
    };
  },
  mounted() {
    this.getBlogdata();
  },
  methods: {
    async getBlogdata() {
      const response = await axios.get(`${apiUrl}blog/list/`);
      this.blog_data = response.data;
      this.totalPages = Math.ceil(this.blog_data.results.length / this.itemsPerPage);
    },
    changePage(page) {
      if (page >= 1 && page <= this.totalPages) {
        this.currentPage = page;
      }
    }
  },
  computed: {
    paginatedPosts() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      const end = start + this.itemsPerPage;
      return this.blog_data.results.slice(start, end);
    }
  }
};
</script>
