---
layout: default
title: products
permalink: /products/
---

<h2>我们的产品系列</h2>

<!-- 调试：确认数据被读取 -->
<!--<p><strong>调试信息：</strong>1共找到 {{ site.data.products.size }} 个产品</p>-->

<div class="product-grid">
  {% for product in site.data.products %}
    <div class="product-item">
      <h3>{{ product.name }}</h3>
      <img src="{{ product.image }}" alt="{{ product.alt }}" style="max-width: 100%; height: auto;">
      <p>{{ product.description }}</p>
    </div>
  {% endfor %}
</div>