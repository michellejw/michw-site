import xml.etree.ElementTree as ET
from datetime import datetime
from typing import List
from dataclasses import dataclass
import re
import os

@dataclass
class BlogPost:
    """Class to store blog post data with consistent structure."""
    title: str
    date: str
    content: str
    categories: List[str]
    tags: List[str]

def clean_html(raw_html: str) -> str:
    """Remove HTML tags and WordPress-specific content markers from text.

    Args:
        raw_html (str): The raw HTML string to clean.

    Returns:
        str: The cleaned text without HTML tags and WordPress markers.
    """
    clean_text = re.sub(r'<!-- wp:(.*?)-->', '', raw_html)
    clean_text = re.sub(r'<[^>]+>', '', clean_text)
    clean_text = clean_text.replace('&amp;', '&')
    clean_text = clean_text.replace('&#8217;', "'")
    clean_text = re.sub(r'\n\s*\n', '\n\n', clean_text.strip())
    return clean_text

def parse_wordpress_export(file_path: str) -> List[BlogPost]:
    """Parse WordPress XML export file and extract blog posts.

    Args:
        file_path (str): The path to the WordPress XML export file.

    Returns:
        List[BlogPost]: A list of BlogPost objects extracted from the XML.
    """
    namespaces = {
        'content': 'http://purl.org/rss/1.0/modules/content/',
        'wp': 'http://wordpress.org/export/1.2/',
        'excerpt': 'http://wordpress.org/export/1.2/excerpt/',
        'dc': 'http://purl.org/dc/elements/1.1/'
    }

    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # Find all items (posts) in the XML
    posts = []
    for item in root.findall('.//item'):
        # Skip attachments and other non-post content
        post_type = item.find('wp:post_type', namespaces)
        if post_type is not None and post_type.text != 'post':
            continue

        # Extract post status
        status = item.find('wp:status', namespaces)
        if status is not None and status.text != 'publish':
            continue

        # Extract title (handle CDATA)
        title_elem = item.find('title')
        title = title_elem.text if title_elem.text else ''
        if title.startswith('<![CDATA['):
            title = title[9:-3]

        date_elem = item.find('wp:post_date', namespaces)
        date = datetime.strptime(date_elem.text, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')

        content_elem = item.find('content:encoded', namespaces)
        content = content_elem.text if content_elem is not None else ''
        if content and content.startswith('<![CDATA['):
            content = content[9:-3]
        content = clean_html(content)

        # Extract categories and tags
        categories = []
        tags = []
        for category in item.findall('category'):
            domain = category.get('domain', '')
            if domain == 'category':
                categories.append(category.text)
            elif domain == 'post_tag':
                tags.append(category.text)

        # Create BlogPost object with consistent structure
        post = BlogPost(
            title=title,
            date=date,
            content=content,
            categories=categories if categories else ['uncategorized'],
            tags=tags if tags else []
        )
        posts.append(post)

    posts.sort(key=lambda x: x.date)
    return posts

def export_posts_to_markdown(posts: List[BlogPost], output_dir: str) -> None:
    """Export BlogPost objects to Markdown files.

    Args:
        posts (List[BlogPost]): A list of BlogPost objects to export.
        output_dir (str): The directory where Markdown files will be saved.

    Returns:
        None
    """
    output_dir = os.path.join('content', 'blog')
    
    os.makedirs(output_dir, exist_ok=True)

    for post in posts:
        md_file_name = f"{post.title.replace(' ', '_').replace('/', '-')}.md"
        md_file_path = os.path.join(output_dir, md_file_name)

        with open(md_file_path, 'w', encoding='utf-8') as md_file:
            # Write front matter
            md_file.write('---\n')  # Start of front matter
            md_file.write(f'title: "{post.title}"\n')  # Title
            md_file.write(f'date: {post.date}\n')  # Date
            md_file.write('draft: false\n')  # Draft status
            md_file.write('---\n\n')  # End of front matter
            
            # Write content with image placeholder
            md_file.write(post.content)
            md_file.write('\n\n<!-- Placeholder for images -->\n')

# Example usage
if __name__ == '__main__':
    input_file = 'old-blog-backup/michelleweirathmueller.WordPress.2024-11-24-posts.xml'
    output_dir = 'blog_posts'

    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), input_file)
    
    try:
        posts = parse_wordpress_export(file_path)
        export_posts_to_markdown(posts, output_dir)
        
        print(f"Found {len(posts)} posts and exported them to Markdown files.")
    except Exception as e:
        print(f"Error processing file: {e}")

