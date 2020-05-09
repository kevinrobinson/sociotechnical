---
disqus: true
---
{% assign post = site.data.db.posts[0] %}

# {{ post.title }} #{{ post.id }}
{{ post.unsafe_html }}


```
yearsRange: {{ post.context.yearsRange }}
fromCountries: {{ post.context.fromCountries }}
```

{% for flag in post.context.flagsForScrutiny %}
  <div style="padding: 10px; display: inline-block; color: white; background: brown;">{{ flag }}</div>
{% endfor %}
