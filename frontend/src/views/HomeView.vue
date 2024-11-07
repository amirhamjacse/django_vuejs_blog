<template>
  <div class="container">
    <h1 class="mt-5">Blog Data</h1>

    <table class="table table-bordered table-striped mt-4">
      <thead>
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Title</th>
          <th scope="col">Description</th>
        </tr>
      </thead>
      <tbody>
        <!-- Loop through blog_data -->
        <tr v-for="(data, index) in blog_data" :key="index">
          <td v-for="(specific, index2) in data" :key="index2">
            <!-- <p><strong>{{ specific.id }}</strong></p> -->
            <p><strong>{{ specific.title }}</strong></p>
            <p>{{ specific.blog_description }}</p>
          </td>
        </tr>
      </tbody>
    </table>
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
