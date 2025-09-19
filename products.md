---
layout: default
title: products
permalink: /products/
---

<h2>Our Products</h2>

<!-- 修改这里：用 site.data.products.zh -->
{% assign product_data = site.data.products_zh %}
{% if product_data == nil %}
  <p>暂无产品信息</p>
{% endif %}

{% if product_data and product_data.size > 0 %}
  <div class="product-grid">
    {% for product in product_data %}
      <div class="product-item">
        <h3>{{ product.name }}</h3>
        {% if product.image %}
          <img src="{{ product.image }}" alt="{{ product.alt | default: product.name }}" style="max-width: 100%; height: auto;">
        {% endif %}
        <p>{{ product.description }}</p>
      </div>
    {% endfor %}
  </div>
{% else %}
  <p>目前还没有产品信息，请稍后再查看。</p>
{% endif %}