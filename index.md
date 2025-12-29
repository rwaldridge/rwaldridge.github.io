---
layout: default
title: Home
---

<div class="profile-section">
  <img src="{{ '/assets/images/profile.jpg' | relative_url }}" alt="Rob Aldridge" class="profile-photo">
  <div class="profile-text">
    <h1>Rob Aldridge</h1>
    <p>I am Professor of Health Metrics Sciences and Team Lead for Clinical Informatics on the Global Burden of Disease (GBD) study at the University of Washington. In this role, I drive the application of federated data analytics, advanced AI and machine learning methods to create billions of estimates for 375 diseases using 60 electronic health record sources from across the globe. Across my career I have integrated engineering, epidemiology, and medicine, enabling the development of innovative approaches to improving health and discovering scientific insights. Previously, as Professor at University College London, I founded and led a Public Health Data Science research group which focused on improving population health through complex health data analysis and the creation of equitable digital health solutions.</p>
  </div>
</div> 

## Featured Research Projects

{% for project in site.data.projects %}
  {% if project.featured %}
  <div class="project-card">
    {% if project.infographic %}
    <div class="project-infographic-small">
      <img src="{{ project.infographic | relative_url }}" alt="{{ project.title }} infographic">
    </div>
    {% endif %}
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

{% assign all_pubs = site.data.publications | where_exp: "item", "item.year" | sort: 'year' | reverse %}
{% for pub in all_pubs limit: 10 %}
<div class="publication">
  <div class="pub-title">{{ pub.title }}</div>
  <div class="pub-authors">{{ pub.authors }}</div>
  <div class="pub-venue">
    {% if pub.venue %}<em>{{ pub.venue }}</em>{% endif %}
    {% if pub.year %} ({{ pub.year }}){% endif %}
  </div>
  {% if pub.doi %}
  <div class="pub-links">
    <a href="https://doi.org/{{ pub.doi }}" target="_blank" rel="noopener">View Publication</a>
  </div>
  {% endif %}
</div>
{% endfor %}

[View all publications →](/publications.html)

## Featured GitHub Repositories

<div class="repo-grid">
  <div class="repo-card">
    <h3><a href="https://github.com/homeappstudy" target="_blank" rel="noopener">Home App Study</a></h3>
    <p>Research tools and resources for the Home App Study cohort.</p>
    <a href="https://github.com/homeappstudy" class="repo-link" target="_blank" rel="noopener">View Repository →</a>
  </div>
  
  <div class="repo-card">
    <h3><a href="https://github.com/UCL-Public-Health-Data-Science/CPRD-GOLD-migrant-phenotype-validation" target="_blank" rel="noopener">CPRD GOLD Migrant Phenotype</a></h3>
    <p>Validation of EHR phenotypes for studying migration and health in the UK.</p>
    <a href="https://github.com/UCL-Public-Health-Data-Science/CPRD-GOLD-migrant-phenotype-validation" class="repo-link" target="_blank" rel="noopener">View Repository →</a>
  </div>
  
  <div class="repo-card">
    <h3><a href="https://github.com/UCL-Public-Health-Data-Science/VirusWatch_Overcrowding" target="_blank" rel="noopener">Virus Watch Overcrowding</a></h3>
    <p>Analysis of household overcrowding and SARS-CoV-2 risk from the Virus Watch cohort.</p>
    <a href="https://github.com/UCL-Public-Health-Data-Science/VirusWatch_Overcrowding" class="repo-link" target="_blank" rel="noopener">View Repository →</a>
  </div>
</div>

[View all repositories →](/github.html)