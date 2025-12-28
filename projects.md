---
layout: default
title: Research Projects
---

# Research Projects

An overview of my research projects spanning AI, federated analytics, and global health data science.

## Active Projects

{% assign active_projects = site.data.projects | where: "status", "active" %}
{% for project in active_projects %}
<div class="project-card">
  <h3>{{ project.title }}</h3>
  <p class="project-meta"><strong>{{ project.period }}</strong> | Status: <span class="status-active">{{ project.status }}</span></p>
  {% if project.funding %}
  <p class="project-funding">💰 {{ project.funding }}</p>
  {% endif %}
  {% if project.collaborators %}
  <p class="project-collaborators">🤝 Collaborators: {{ project.collaborators | join: ", " }}</p>
  {% endif %}
  <p>{{ project.short_description }}</p>
  {% if project.long_description %}
  <details>
    <summary>Read more</summary>
    <div class="project-long-description">
      {{ project.long_description | markdownify }}
    </div>
  </details>
  {% endif %}
  {% if project.tags %}
  <p class="project-tags">
    {% for tag in project.tags %}
      <span class="tag">{{ tag }}</span>
    {% endfor %}
  </p>
  {% endif %}
  {% if project.outputs %}
  <div class="project-outputs">
    <strong>Key Outputs:</strong>
    <ul>
      {% for output in project.outputs %}
        <li>{{ output }}</li>
      {% endfor %}
    </ul>
  </div>
  {% endif %}
</div>
{% endfor %}

## Completed Projects

{% assign completed_projects = site.data.projects | where: "status", "completed" %}
{% for project in completed_projects %}
<div class="project-card">
  <h3>{{ project.title }}</h3>
  <p class="project-meta"><strong>{{ project.period }}</strong> | Status: <span class="status-completed">{{ project.status }}</span></p>
  {% if project.funding %}
  <p class="project-funding">💰 {{ project.funding }}</p>
  {% endif %}
  {% if project.team_size %}
  <p class="project-team">👥 Team: {{ project.team_size }}</p>
  {% endif %}
  <p>{{ project.short_description }}</p>
  {% if project.long_description %}
  <details>
    <summary>Read more</summary>
    <div class="project-long-description">
      {{ project.long_description | markdownify }}
    </div>
  </details>
  {% endif %}
  {% if project.tags %}
  <p class="project-tags">
    {% for tag in project.tags %}
      <span class="tag">{{ tag }}</span>
    {% endfor %}
  </p>
  {% endif %}
</div>
{% endfor %}
