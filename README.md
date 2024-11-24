# Personal Website

This is a personal website built using [Hugo](https://gohugo.io/), a fast and modern static site generator, with the [Hugo Story theme](https://themes.gohugo.io/hugo-story-theme/). The site features a responsive, single-page design with sections for blog posts, projects, and contact information.

## Getting Started

### Prerequisites
- Install [Hugo](https://gohugo.io/getting-started/installing/)
- Clone this repository

### Local Development
1. Run the development server
```bash
hugo server -D
```
2. View the site at http://localhost:1313

### Adding Content

#### Creating Blog Posts
To create a new blog post:

1. Create a new markdown file in the `content/blog` directory:

```bash
hugo new blog/my-first-post.md
```

2. Edit the newly created file in the `content/blog` directory.

```markdown
---
title: "Example Post"
date: 2024-01-01
draft: true
---

# Welcome to the example post
content goes here

```

3. Set the `draft` field to `false` when you're ready to publish the post.

### Editing Site Content

The site content is organized in the following way:

1. **Main Page Sections**
   - Banner text: Edit `data/banner.yml`
   - About section: Edit `data/about.yml`
   - Skills/Items: Edit `data/items.yml`

2. **Configuration**
   - Site title and basic settings: Edit `hugo.toml`
   - Social media links: Edit the `[Params.social]` section in `hugo.toml`

3. **Templates**
   - Blog list layout: `layouts/_default/list.html`
   - Blog post layout: `layouts/_default/single.html`
   - Main page layout: `layouts/index.html`

### Building for Production

To build the site for production:
```bash
hugo --minify
```
The generated `public` directory will contain the static site files.
