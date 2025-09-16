---
layout: page
title: 产品中心
permalink: /products/
---

<h2>我们的产品系列</h2>

<div class="product-grid">
  {% for product in site.data.products %}
    <div class="product-item">
      <h3>{{ product.name }}</h3>
      <img src="{{ image }}" alt="{{ product.alt }}" style="max-width: 100%; height: auto;">
      <p>{{ product.description }}</p>
    </div>
  {% endfor %}
</div>
