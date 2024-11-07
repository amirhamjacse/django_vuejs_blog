<template>
  <div class="container mt-5">
    <!-- <h1 class="text-center">Blog Posts</h1> -->

    <!-- Outer loop: Loop through each category in blog_data -->
    <div class="row">
      <div v-for="(category, categoryIndex) in blog_data" :key="categoryIndex" class="col-md-12">
        
        <!-- Category Header (optional) -->
        <!-- <h3>Category {{ categoryIndex + 1 }}</h3> -->
        
        <!-- Inner loop: Loop through each post within this category -->
        <div class="row">
          <div v-for="(post, postIndex) in category" :key="post.id" class="col-md-12 mb-4">
            <div class="card">
              <div class="card-body">
                <h5 class="card-title">{{ post.title }}</h5>
                <p class="card-text">{{ post.blog_description }}</p>
                <a href="#" class="btn btn-primary">Read More</a>
              </div>
            </div>
          </div>
        </div>
        
      </div>
    </div>
  </div>
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
    methods: {
      async getBlogdata(){
        const response = await axios.get(`${apiUrl}/blog/list/`)
        // const response = axios.get(`http://127.0.0.1:8000/blog/list/`)
        this.blog_data = response.data;
        console.log(response.data);
      }
    },
}
  </script>
