---
layout: default
title: products
permalink: /products/
---

<h2>Our products</h2>



<div class="product-grid">
  {% for product in site.data.products.zh %}
    <div class="product-item">
      <h3>{{ product.name }}</h3>
      <img src="{{ product.image }}" alt="{{ product.alt }}" style="max-width: 100%; height: auto;">
      <p>{{ product.description }}</p>
    </div>
  {% endfor %}
</div>