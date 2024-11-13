<script setup>
import NavigationBar from '@/components/NavigationBar.vue';
import FooterDesign from '@/components/FooterDesign.vue';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
</script>

<template>
  <NavigationBar></NavigationBar>
  <div class="container my-5">
    <!-- Blog Post Detail -->
    <div v-if="loading" class="card shadow-sm">
      <div class="card-header bg-primary text-white">
        <div class="skeleton-title mb-3"></div>
      </div>
      <div class="card-body">
        <div class="skeleton-text mb-3"></div>
        <div class="skeleton-text mb-3"></div>
        <div class="skeleton-btn mb-3"></div>
      </div>
    </div>

    <article v-else v-if="post" class="card shadow-sm">
      <div class="card-header bg-primary text-white d-flex justify-content-between align-items-center">
        <h2 class="mb-0">{{ isEditing ? 'Edit Post' : post.title }}</h2>
        <div>
          <button v-if="!isEditing" @click="startEdit" class="btn btn-warning btn-sm mx-2">
            <i class="fas fa-edit"></i> Edit
          </button>
          <button @click="deletePost" class="btn btn-danger btn-sm">
            <i class="fas fa-trash"></i> Delete
          </button>
        </div>
      </div>

      <div class="card-body">
        <p class="text-muted">
          <strong>Published on:</strong> {{ post.date }} |
          <strong>Author:</strong> Hamja {{ post.author }}
        </p>
        <hr>

        <!-- Editable Fields -->
        <div v-if="isEditing">
          <div class="mb-3">
            <label for="title" class="form-label">Title</label>
            <input v-model="editablePost.title" type="text" class="form-control" id="title" />
          </div>
          <div class="mb-3">
            <label for="description" class="form-label">Description</label>
            <textarea v-model="editablePost.blog_description" class="form-control" id="description" rows="5"></textarea>
          </div>
          <button @click="saveChanges" class="btn btn-success mx-2">Save</button>
          <button @click="cancelEdit" class="btn btn-secondary">Cancel</button>
        </div>

        <!-- Non-editable View -->
        <div v-else>
          <div v-html="post.blog_description"></div>
        </div>
      </div>
      
      <div class="card-footer">
        <router-link :to="'/'" class="btn btn-secondary">Back to Blog</router-link>
      </div>
    </article>
  </div>
  <FooterDesign></FooterDesign>
</template>


<script>
import axios from 'axios';
const apiUrl = import.meta.env.VITE_API_URL;

export default {
  props: ['id'],
  data() {
    return {
      post: null, // Initially null until data is loaded
      editablePost: {
        title: "",
        blog_description: ""
      },
      isEditing: false,
      loading: true // To track if data is being loaded
    };
  },
  mounted() {
    this.detailsBlog();
  },
  methods: {
    async detailsBlog() {
      try {
        const response = await axios.get(`${apiUrl}blog/details/${this.id}/`);
        this.post = response.data;
        this.setEditableFields();
      } catch (error) {
        console.error("Failed to load post:", error);
        alert("An error occurred while loading the post.");
      } finally {
        this.loading = false; // Data is loaded, turn off loading state
      }
    },
    setEditableFields() {
      this.editablePost.title = this.post.title;
      this.editablePost.blog_description = this.post.blog_description;
    },
    startEdit() {
      this.isEditing = true;
    },
    cancelEdit() {
      this.isEditing = false;
      this.setEditableFields(); // Reset fields to original values
    },
    async saveChanges() {
      try {
        const response = await axios.put(`${apiUrl}blog/update/${this.id}/`, {
          title: this.editablePost.title,
          blog_description: this.editablePost.blog_description,
        });
        this.post = response.data; // Update post with new data
        this.isEditing = false;
      } catch (error) {
        console.error("Failed to update post:", error);
        alert("An error occurred while saving the changes.");
      }
    },
    async deletePost() {
      if (confirm("Are you sure you want to delete this post?")) {
        try {
          await axios.delete(`${apiUrl}blog/delete/${this.id}/`);
          alert("Post deleted successfully.");
          router.push('/'); // Redirect back to the main blog list page
        } catch (error) {
          console.error("Failed to delete post:", error);
          alert("An error occurred while deleting the post.");
        }
      }
    },
  }
};
</script>

<style scoped>
/* Skeleton loader styles */
.skeleton-title {
  width: 70%;
  height: 25px;
  background-color: #ddd;
  margin-bottom: 15px;
}

.skeleton-text {
  width: 100%;
  height: 15px;
  background-color: #ddd;
  margin-bottom: 10px;
}

.skeleton-btn {
  width: 50%;
  height: 40px;
  background-color: #ddd;
}
</style>
