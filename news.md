---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
class: news
title: News
permalink: /news/
---

<div class="container">
  <div class="row lead-row">
    <div class="col-xs-11 col-md-12 col-lg-12 lead-div">
      <h1 class="page-title">{{ page.title }}</h1>

      {% assign sorted = site.news | sort: 'date' | reverse %}
      {% for item in sorted %}
      <article class="news-{{ item.year }}">
        <h3>{{ item.year }}</h3>
        {{ item.content }}
      </article>
      {% endfor %}

    </div>
  </div>

</div>
