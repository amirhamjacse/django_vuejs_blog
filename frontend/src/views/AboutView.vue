<template>
  <div class="about">
    <h1>This is an about page</h1>
    <p><strong>Post ID:</strong> {{ id }}</p>

  </div>
</template>

<script>
export default {
  props: ['id'],  // This will automatically receive the `id` from the route params
  data() {
    return {
      id: this.id,
      post: {
        title: 'Loading title...',
        blog_description: 'Loading description...'
      }
    };
  },
}

</script>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
