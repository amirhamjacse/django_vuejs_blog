<template>
    <!-- Main Footer Section -->
    <footer class="bg-dark text-white py-4">
      <div class="container">
        <div class="row">
          
          <!-- About Section -->
          <div class="col-md-4">
            <h5>About Us</h5>
            <p>
              Welcome to Demo-Blog! Stay up-to-date with the latest blog posts, articles, and insights in the world of sustainability, technology, and more.
            </p>
          </div>
  
          <!-- Quick Links Section -->
          <div class="col-md-4">
            <h5>Quick Links</h5>
            <ul class="list-unstyled">
              <li><a href="/" class="text-white">Home</a></li>
              <li><a href="/blog" class="text-white">Blog</a></li>
              <li><a href="/about" class="text-white">About</a></li>
              <li><a href="/contact" class="text-white">Contact</a></li>
              <li><a href="/privacy-policy" class="text-white">Privacy Policy</a></li>
            </ul>
          </div>
  
          <!-- Social Media Links -->
          <div class="col-md-4">
            <h5>Follow Us</h5>
            <div>
              <a href="https://twitter.com" target="_blank" class="text-white mx-2"><i class="fab fa-twitter"></i> Twitter</a>
              <a href="https://facebook.com" target="_blank" class="text-white mx-2"><i class="fab fa-facebook-f"></i> Facebook</a>
              <a href="https://instagram.com" target="_blank" class="text-white mx-2"><i class="fab fa-instagram"></i> Instagram</a>
              <a href="https://linkedin.com" target="_blank" class="text-white mx-2"><i class="fab fa-linkedin-in"></i> LinkedIn</a>
            </div>
          </div>
          
        </div>
  
        <!-- Footer Bottom Section -->
        <div class="row mt-4">
          <div class="col text-center">
            <p class="mb-0">&copy; 2024 Demo-Blog. All Rights Reserved.</p>
          </div>
        </div>
      </div>
    </footer>
  </template>
  
  <script setup>
  // No script needed unless you want to add specific functionalities (like form handling, etc.)
  </script>
  
  <style scoped>
  footer {
    background-color: #343a40;
  }
  
  footer a {
    text-decoration: none;
  }
  
  footer a:hover {
    color: #007bff;
  }
  
  footer .fab {
    font-size: 1.5rem;
  }
  
  /* Ensuring responsive behavior */
  @media (max-width: 767px) {
    footer .row {
      text-align: center;
    }
    footer .col-md-4 {
      margin-bottom: 15px;
    }
  }
  </style>
  