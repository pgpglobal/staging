---
layout: blog
class: blog-feed
title: Blog
permalink: /blog/
---

{% for post in site.posts %}
<article>
  <div class="post-header">
    <h2><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
    <div class="date">{{ post.date | date: "%B %-d, %Y" }}</div>
  </div>

<div class="meta clear">
  {%- if post.author -%}
  <div class="author">
    <span class="by-author">
      <span class="sep">by</span>
      <a class="url fn n" title="View all posts by {{ post.author | escape }}" rel="author" href="{{ post.author.url }}">{{ post.author | escape }}</a>
    </span>
  </div>
  {%- endif-%}
</div>

  <p>{{ post.excerpt }}</p>
</article>
{% endfor %}

