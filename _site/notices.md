# Fairness notices
Add automated checks for fairness issues in data dependencies and enforce them in continuous integration and build systems.

<div style="box-shadow: 0 2px 2px -2px #ccc; margin: 20px; border: 1px solid #eee; opacity: 0.8;">
  <img src="/notice.png" width="100%" alt="Fairness notice: US Census data" />
</div>

To add a new notice, please submit a pull request in GitHub.
<ul>
  {% for post in site.data.db.posts %}
    <li>
      <a href="/notice/{{ post.id }}">{{ post.date | date: "%B %-d, %Y"}}: {{ post.title }}</a>
    </li>
  {% endfor %}
</ul>