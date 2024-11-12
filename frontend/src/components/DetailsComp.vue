<script setup>
import NavigationBar from '@/components/NavigationBar.vue';
import FooterDesign from '@/components/FooterDesign.vue';
</script>
    <template>
    <NavigationBar></NavigationBar>
    <div class="container my-5">
      <!-- Blog Post Detail -->
      <div v-if="post" class="card shadow-sm">
        <div class="card-header bg-primary text-white">
          <h2 class="justify-content-center">{{ post.title }} Edit/ Delete</h2>
        </div>
        <div class="card-body">
          <p class="text-muted">
            <strong>Published on:</strong> {{ post.date }} |
            <strong>Author:</strong> Hamja {{ post.author }}
          </p>
          <hr>
          <div v-html="post.blog_description"></div>
        </div>
        <div class="card-footer">
            <router-link :to="'/'" class="btn btn-secondary">
                Back to Blog
                </router-link>
          <!-- <button class="btn btn-secondary" @click="goBack">Back to Blog</button> -->
        </div>
      </div>
    </div>
    <FooterDesign></FooterDesign>
  </template>

<script>
import axios from 'axios';
const apiUrl = import.meta.env.VITE_API_URL;
export default{
    props: ['id'],
    data(){
        return{
            description: '',
            post: "",
            // id: this.id
        }
    },
    mounted(){
        this.detailsBlog();
    },
    methods:{
        async detailsBlog(){
        // console.log(this.id, 'working')
        const response = await axios.get(`${apiUrl}blog/details/${this.id}/`);
        this.post = response.data;
        // console.log(response);

        }
    }
}
</script>