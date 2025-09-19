---
layout: default
title: Our Products
permalink: /products/
---

<!-- 删除:<h2>Our Products</h2> -->
<!-- 删除:<h2>我们的产品</h2> -->
<h2>Our Products</h2>

{% assign product_data = site.data.products.zh %}

{% if product_data == nil %}
  {% assign product_data = site.data.products_zh %}
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
  <!-- 删除:<p>暂无产品信息</p> -->
  <!-- 删除:<p>目前还没有产品信息，请稍后再查看。</p> -->
  <p>No product information available at the moment. Please check back later.</p>
  <!-- 添加调试信息 -->
  <p>Debug info: products_data = {{ product_data }}</p>
  <p>Debug info: site.data.products = {{ site.data.products }}</p>
  <p>Debug info: site.data.products_zh = {{ site.data.products_zh }}</p>
{% endif %}

