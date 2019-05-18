from django import template

register = template.Library()

@register.filter
def hashtag_link(post):   # 인자
    content = post.content+' '   # 게시글 내용
    hashtags = post.hashtags.all()   # hashtag만 출력
    
    # hashtags를 순회하면서 content 내에서 해당 문자열(해시태그)을
    # 링크를 포함한 문자열(<a>)로 치환
    for hashtag in hashtags:
        content = content.replace(hashtag.content+' ', f'<a href="/posts/hashtag/{hashtag.pk}/">{hashtag.content}</a> ')
    return content
        

# {{ post|hashtag_link }}