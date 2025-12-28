---
layout: project
title: "Adaptive Learning Systems at Scale"
project_id: "adaptive-learning-systems"
permalink: /projects/adaptive-learning-systems.html
---

# {{ page.title }}

{% assign project = site.data.projects | where: "id", page.project_id | first %}

<div class="project-header">
  <span class="project-status {{ project.status }}">{{ project.status | capitalize }}</span>
  <p class="project-period">{{ project.period }}</p>
  {% if project.funding %}
  <p class="project-funding">💰 {{ project.funding }}</p>
  {% endif %}
</div>

## Overview

{{ project.long_description }}

<div class="project-infographic">
  <img src="{{ project.infographic }}" alt="{{ project.title }} visual summary">
  <p class="caption">Visual summary of the adaptive learning framework</p>
</div>

## Research Questions

1. **How can we personalize learning at scale?**
   - Traditional one-on-one tutoring is effective but doesn't scale
   - We investigate AI-driven personalization for thousands of concurrent learners

2. **What student signals predict learning outcomes?**
   - Click patterns, time-on-task, assessment responses
   - Building real-time models of student knowledge state

3. **How do we balance exploration vs. exploitation?**
   - Trade-off between trying new content strategies vs. using proven approaches
   - Apply reinforcement learning with safety constraints

## Methodology

### Data Collection
- **Platform:** Custom MOOC platform with instrumentation
- **Courses:** 5 STEM courses (CS, Math, Physics)
- **Students:** 50,000+ learners across 3 years
- **Metrics:** Engagement, learning gains, retention

### Algorithms
- **Knowledge Tracing:** Bayesian Knowledge Tracing + Deep Knowledge Tracing
- **Content Recommendation:** Multi-armed bandits with contextual features
- **Intervention Timing:** Survival analysis for dropout prediction

### Evaluation
- **A/B Testing:** Randomized controlled trials comparing personalized vs. control
- **Effect Size:** Cohen's d for learning gains
- **Fairness Audits:** Disaggregated analysis by demographics

## Key Findings

{% for finding in project.key_findings %}
- **{{ finding }}**
{% endfor %}

### Detailed Results

**Learning Outcomes:**
- Students in adaptive condition showed 25% higher assessment scores (p < 0.001)
- Effect sizes consistent across course topics (d = 0.42 - 0.58)
- Gains particularly pronounced for students with lower prior knowledge

**Engagement Metrics:**
- 30% reduction in dropout rates compared to control
- 40% increase in voluntary problem-solving attempts
- Students reported higher satisfaction (4.3/5 vs 3.7/5)

**Generalization:**
- Algorithms trained on one course transferred effectively to others
- Performance maintained across different student populations
- Robust to missing data (common in real-world MOOCs)

## Publications

<!-- Auto-generated from publications.yml -->
{% assign related_pubs = site.data.publications | where_exp: "pub", "pub.tags contains 'education'" | where_exp: "pub", "pub.tags contains 'machine-learning'" | sort: "year" | reverse %}

{% for pub in related_pubs limit:5 %}
<div class="publication-item">
  <h4>{{ pub.title }}</h4>
  <p class="pub-authors">{{ pub.authors }}</p>
  <p class="pub-venue"><strong>{{ pub.venue_short }} {{ pub.year }}</strong></p>
  <p>
    {% if pub.doi %}
    <a href="https://doi.org/{{ pub.doi }}">DOI</a> •
    {% endif %}
    {% if pub.pdf %}
    <a href="{{ pub.pdf }}">PDF</a>
    {% endif %}
  </p>
</div>
{% endfor %}

## Software & Code

**Main Repository:** [adaptive-learning-toolkit](https://github.com/rwaldridge/adaptive-learning-toolkit)

**Features:**
- Plug-and-play integration with learning management systems
- Pre-trained models for common STEM topics
- Privacy-preserving data collection (FERPA compliant)
- Real-time dashboard for instructors

**Installation:**
```bash
pip install adaptive-learning-toolkit
```

**Example Usage:**
```python
from adaptive_learning import PersonalizedRecommender

# Initialize recommender
recommender = PersonalizedRecommender(
    course_id="CS101",
    student_model="deep_kt"
)

# Get next recommended content for student
next_item = recommender.recommend(
    student_id="student_123",
    current_knowledge_state={...}
)
```

## Team

**Principal Investigator:**
- Dr. Robert Aldridge (PI)

**PhD Students:**
- Maria Chen (Algorithms & Implementation)
- James Park (Evaluation & User Studies)
- Sarah Johnson (Fairness & Ethics)

**Postdoctoral Researchers:**
- Dr. Li Wei (Platform Engineering)
- Dr. Ahmed Hassan (Data Science)

**Collaborators:**
- Prof. Jane Smith (University of Michigan) - Learning Sciences
- Dr. Michael Brown (Stanford Online) - Platform Integration

## Funding & Support

- **NSF Grant #1234567:** "CAREER: Adaptive Learning Systems for Personalized STEM Education" ($500,000, 2023-2028)
- **Compute Resources:** AWS Research Credits ($50K)
- **Partner Institutions:** University of Michigan, Stanford Online

## Impact

### Academic Impact
- **Citations:** 150+ (Google Scholar)
- **Media Coverage:** Featured in EdWeek, Inside Higher Ed
- **Awards:** Best Paper Honorable Mention, CHI 2024

### Real-World Deployment
- **Active Users:** 10,000+ students across 3 universities
- **Courses:** Deployed in 8 MOOCs
- **Instructor Adoption:** 25 faculty using toolkit

### Open Educational Resources
- **Documentation:** Comprehensive tutorials and API reference
- **Video Tutorials:** 10-part YouTube series (5K+ views)
- **Workshop Materials:** Presented at 3 conferences

## Future Directions

1. **Multimodal Learning:**
   - Incorporating video engagement, discussion forum participation
   - Building holistic models of student learning

2. **Long-Term Outcomes:**
   - Tracking students beyond course completion
   - Measuring retention in major, career outcomes

3. **Scalability:**
   - Cloud-native architecture for millions of learners
   - Real-time processing with sub-100ms latency

4. **Ethics & Fairness:**
   - Auditing for algorithmic bias
   - Ensuring equitable access and outcomes

## Get Involved

**Interested in collaboration?**
- [Contact me](mailto:your.email@university.edu) for partnerships
- [GitHub Issues](https://github.com/rwaldridge/adaptive-learning-toolkit/issues) for technical questions
- [Slack Community](https://adaptive-learning.slack.com) for discussions

**Resources:**
- [Project Website](https://adaptivelearning.example.com)
- [Documentation](https://docs.adaptivelearning.example.com)
- [Tutorial Videos](https://youtube.com/playlist?list=...)
- [Demo](https://demo.adaptivelearning.example.com)

---

**Last Updated:** December 2024  
**Project Status:** Active  
**Next Milestone:** Large-scale deployment (Spring 2025)
