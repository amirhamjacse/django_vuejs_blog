<script setup>
import NavigationBar from '@/components/NavigationBar.vue';
import FooterDesign from '@/components/FooterDesign.vue';
</script>
<template>
  <NavigationBar></NavigationBar>
  <div class="container my-5">
    <!-- Blog Title -->
    <div class="text-center mb-4">
      <h1>Welcome to My Blog</h1>
      <p class="lead">Latest Posts and Updates</p>
    </div>

    <!-- Blog Post List -->
    <div class="row">


      <!-- <div v-for="cat in blog_data">
        <div v-for="a in cat">
          <div class="card">
            {{ a.title }}
          </div>
        </div>
        
      </div> -->


  <!-- {{ blog_data.results }} -->
      <div v-for="(post, categoryIndex) in blog_data.results" :key="categoryIndex" class="col-md-12">
        <!-- {{ category }} -->
        
        <!-- Category Header (optional) -->
        <!-- <h3>Category {{ categoryIndex + 1 }}</h3> -->
        
        <!-- Inner loop: Loop through each post within this category -->
        <div class="row">
          <!-- <div v-for="(post, postIndex) in category" :key="post.id" class="col-md-12 mb-4"> -->
            
            <div v-if="post" class="card my-1">
              <div class="card-body">
                <h5 class="card-title">Title: {{ post.title }}</h5>
                <!-- <p class="card-text">{{ post.blog_description }}</p> -->
                <!-- <p class="card-text">{{ getExcerpt(post.blog_description, 6) }}</p> -->
                <!-- <a href="#" class="btn btn-primary">Read More</a> -->
                <router-link :to="'/details/' + post.id" class="btn btn-primary">
                Read More
                </router-link>
              <!-- </div> -->
            </div>
          </div>
        </div>
        
      </div>
    </div>

    <!-- Pagination (if needed) -->
    <nav aria-label="Page navigation">
      <ul class="pagination justify-content-center">
        <li class="page-item" :class="{ disabled: currentPage === 1 }">
          <a class="page-link" href="#" @click="changePage(currentPage - 1)">Previous</a>
        </li>
        <li
          v-for="page in totalPages"
          :key="page"
          class="page-item" 
          :class="{ active: currentPage === page }"
        >
          <a class="page-link" href="#" @click="changePage(page)">{{ page }}</a>
        </li>
        <li class="page-item" :class="{ disabled: currentPage === totalPages }">
          <a class="page-link" href="#" @click="changePage(currentPage + 1)">Next</a>
        </li>
      </ul>
    </nav>
  </div>
  <FooterDesign></FooterDesign>
</template>

  <script>
  import axios from 'axios';
  const apiUrl = import.meta.env.VITE_API_URL;
export default{
    data(){
      return {
        blog_data: "",
      }
    },
    mounted(){
      this.getBlogdata();
    },
    // beforeMount(){
    //   this.getExcerpt();
    // },
    methods: {
      async getBlogdata(){
        const response = await axios.get(`${apiUrl}blog/list/`)
        // const response = axios.get(`http://127.0.0.1:8000/blog/list/`)
        this.blog_data = response.data;
        console.log(response.data);
      },
    //   getExcerpt(content, wordLimit) {
    //     console.log('working')
    //     const words = content.split(' '); // Split content into an array of words
    //     return words.slice(0, wordLimit).join(' ') + (words.length > wordLimit ? '...' : ''); // Return truncated content
    // }
    },
}
  </script>
