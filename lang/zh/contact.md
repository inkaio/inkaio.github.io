---
layout: default
title: 联系我们
permalink: /zh/contact/
---

<h2>联系我们</h2>

<div class="contact-info">
  <div class="contact-item">
    <h3>邮箱</h3>
    <p><a href="mailto:info@inkaio.com">info@inkaio.com</a></p>
  </div>
  
  <div class="contact-item">
    <h3>电话</h3>
    <p>+1 (555) 123-4567</p>
  </div>
  
  <div class="contact-item">
    <h3>地址</h3>
    <p>123科技街<br>
    创新城市, IC 12345<br>
    美国</p>
  </div>
</div>

<style>
.contact-info {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.contact-item h3 {
  color: #333;
  border-bottom: 2px solid #007bff;
  padding-bottom: 0.5rem;
  margin-bottom: 1rem;
}

.contact-item p {
  font-size: 1.1rem;
  line-height: 1.6;
}

.contact-item a {
  color: #007bff;
  text-decoration: none;
}

.contact-item a:hover {
  text-decoration: underline;
}
</style>