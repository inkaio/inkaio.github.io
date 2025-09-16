---
layout: default
title: Products
permalink: /en/products/
---

<h2>Our Products</h2>

<div class="product-grid">
  {% for product in site.data.products.en %}
    <div class="product-item">
      <h3>{{ product.name }}</h3>
      <img src="{{ product.image }}" alt="{{ product.alt }}" style="max-width: 100%; height: auto;">
      <p>{{ product.description }}</p>
    </div>
  {% endfor %}
</div>