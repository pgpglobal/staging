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
    <div class="col-xs-8 col-md-9 lead-div">
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

  <h3>2005</h3>
  <ul>
    <li>
      <strong>The Personal Genome Project</strong><br>
      George Church. Molecular Systems Biology, Dec 2005. (<a href="http://www.nature.com/msb/journal/v1/n1/full/msb4100040.html">full text</a>)
    </li>
  </ul>

  <p></p>
    </div>
  </div>
</div>
