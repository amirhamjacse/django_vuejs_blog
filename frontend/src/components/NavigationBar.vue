<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container">
        <!-- Brand/Logo -->
        <a class="navbar-brand" href="/">Hamja Blog</a>
        
        <!-- Toggle button for smaller screens -->
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
  
        <!-- Navbar links -->
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto">
            <!-- Home Link -->
            <li class="nav-item">
              <a class="nav-link" href="/">Home</a>
            </li>
            
            <!-- Categories Link -->
            <li class="nav-item">
              <a class="nav-link" href="/categories">Categories</a>
            </li>
  
            <!-- About Link -->
            <li class="nav-item">
              <a class="nav-link" href="/about">About</a>
            </li>
  
            <!-- Contact Link -->
            <li class="nav-item">
              <a class="nav-link" href="/contact">Contact</a>
            </li>
  
            <!-- Blog Post link (if desired) -->
            <li class="nav-item">
              <a class="nav-link" href="/new-post">New Post</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </template>
  
  <script>
  export default {
    name: 'BlogNavbar'
  };
  </script>
  
  <style scoped>
  /* Optional: Custom styling for your navbar */
  .navbar {
    margin-bottom: 30px;
  }
  .navbar-brand {
    font-weight: bold;
  }
  .navbar-nav .nav-link {
    font-size: 1.1rem;
    color: #333;
  }
  
  .navbar-nav .nav-link:hover {
    color: #007bff;
  }
  </style>
  