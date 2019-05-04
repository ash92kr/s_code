from django import template
import re


register = template.Library()

@register.filter
# def hashtag_link(post):
#     content = post.content
#     hashtags = post.hashtags.all()

#     for hashtag in hashtags:
        # content = content.replace(f'{hashtag.content}', f'<a href="/posts/hashtag/{hashtag.pk}/">{hashtag.content}</a>')

        # content = re.sub(fr'{hashtag.content}\b',  f'<a href="/posts/hashtag/{hashtag.pk}/">{hashtag.content}</a> ', content)

        # content = content.replace(hashtag.content, f'<a href="/posts/hashtag/{hashtag.pk}/">{hashtag.content}</a>')
        # content = re.sub(hashtag.content + r'\b', f'<a href="/posts/hashtag/{hashtag.pk}/">{hashtag.content}</a>', content)
    # return content


@register.filter
def hashtag_link(post):
   content = post.content
   hashtags = post.hashtags.all()

   for hashtag in hashtags:
        content = re.sub(fr'{hashtag.content}\b', f'<a href="/posts/hashtags/{hashtag.pk}/">{hashtag.content}</a> ', content)
   return content
