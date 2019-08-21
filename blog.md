---
layout: blog
class: blog
title: Blog
permalink: /blog/
---

{% for post in site.posts %}
<article>
  <div class="post-header">
    <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
    <div class="date">{{ post.date | date: "%B %-d, %Y" }}</div>
  </div>
  <p>{{ post.excerpt }}</p>
</article>
{% endfor %}

