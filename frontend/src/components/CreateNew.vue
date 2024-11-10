<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router'; // Import useRouter from Vue Router
import NavigationBar from '@/components/NavigationBar.vue';
import FooterDesign from '@/components/FooterDesign.vue';

const apiUrl = import.meta.env.VITE_API_URL;

// Form state
const title = ref('');
const blogDescription = ref('');
const isActive = ref(true);

// Get the router instance
const router = useRouter();

// Form submission method
const createPost = async () => {
  try {
    const response = await axios.post(`${apiUrl}blog/create/`, {
      title: title.value,
      blog_description: blogDescription.value,
      is_active: isActive.value,
      date: new Date().toISOString(),
    });

    console.log('Post created successfully:', response.data);
    
    // Redirect to the list page after successful post creation
    router.push({ name: 'home' }); // Assuming your list page route name is 'blog-list'

  } catch (error) {
    console.error('Error creating post:', error);
  }
};
</script>

<template>
  <NavigationBar />
  <div class="container">
    <h1>Create Blog Post</h1>
    
    <div class="form-group">
      <div class="row">
        <!-- Title input -->
        <div class="col-md-6">
          <label for="title">Title</label>
          <input
            type="text"
            class="form-control"
            id="title"
            v-model="title"
            placeholder="Enter the blog title"
            required
          />
        </div>

        <!-- Description input -->
        <div class="col-md-6">
          <label for="blogDescription">Blog Description</label>
          <textarea
            class="form-control"
            id="blogDescription"
            v-model="blogDescription"
            placeholder="Enter the blog description"
            rows="5"
            required
          ></textarea>
        </div>
      </div>

      <!-- Is Active input -->
      <div class="form-check">
        <input
          type="checkbox"
          class="form-check-input"
          id="isActive"
          v-model="isActive"
        />
        <label class="form-check-label" for="isActive">Is Active?</label>
      </div>
    </div>

    <div class="form-group">
      <button class="btn btn-primary" @click="createPost">Create Post</button>
    </div>
  </div>
  <FooterDesign></FooterDesign>
</template>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.form-group {
  margin-bottom: 20px;
}

textarea {
  resize: vertical;
}
</style>
