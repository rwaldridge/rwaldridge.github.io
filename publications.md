---
layout: default
title: Publications
---

# Publications

{% assign publications_by_year = site.data.publications | group_by: "year" | sort: "name" | reverse %}

{% for year_group in publications_by_year %}
## {{ year_group.name }}

{% for pub in year_group.items %}
<div class="publication">
  <div class="pub-title">{{ pub.title }}</div>
  <div class="pub-authors">{{ pub.authors }}</div>
  <div class="pub-venue">
    {% if pub.venue %}
      <em>{{ pub.venue }}</em>
      {% if pub.volume %}, Vol. {{ pub.volume }}{% endif %}{% if pub.pages %}, pp. {{ pub.pages }}{% endif %}
    {% endif %}
  </div>
  {% if pub.doi %}
  <div class="pub-links">
    <a href="https://doi.org/{{ pub.doi }}" target="_blank" rel="noopener">DOI: {{ pub.doi }}</a>
  </div>
  {% endif %}
</div>
{% endfor %}

{% endfor %}
