---
layout: default
title: Home
---

# Rob Aldridge

I am Professor of Health Metrics Sciences and Team Lead for Clinical Informatics on the Global Burden of Disease (GBD) study at the University of Washington. In this role, I drive the application of federated data analytics, advanced AI and machine learning methods to create billions of estimates for 375 diseases using 60 electronic health record sources from across the globe. Across my career I have integrated engineering, epidemiology, and medicine, enabling the development of innovative approaches to improving health and discovering scientific insights. Previously, as Professor at University College London, I founded and led a Public Health Data Science research group which focused on improving population health through complex health data analysis and the creation of equitable digital health solutions. 

## Featured Research Projects

{% for project in site.data.projects %}
  {% if project.featured %}
  <div class="project-card">
    <h3>{{ project.title }}</h3>
    <p class="project-meta"><strong>{{ project.period }}</strong> | Status: {{ project.status }}</p>
    {% if project.funding %}
    <p class="project-funding">💰 {{ project.funding }}</p>
    {% endif %}
    <p>{{ project.short_description }}</p>
    {% if project.tags %}
    <p class="project-tags">
      {% for tag in project.tags %}
        <span class="tag">{{ tag }}</span>
      {% endfor %}
    </p>
    {% endif %}
  </div>
  {% endif %}
{% endfor %}

## Recent Publications

Coming soon - add your publications to `_data/publications.yml`.

## Contact

- Email: rob.aldridge@gmail.com
- GitHub: [rwaldridge](https://github.com/rwaldridge)
