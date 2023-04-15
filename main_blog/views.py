from django.shortcuts import render

from .models import Post, Tag

from r_utils import rst_to_html, md_to_html

page_divide = 10


def index(request):
    count_of_posts = Post.objects.count()

    number_of_pages = (
            count_of_posts // page_divide + (count_of_posts % page_divide > 0) * 1
    )

    current_page = 0
    try:
        current_page = int(request.GET["page"]) - 1
    except KeyError:
        pass

    start = current_page * page_divide
    end = min(start + page_divide, count_of_posts)

    ten_latest_posts = Post.objects.all()[start:end]
    ten_most_used_tags = Tag.get_tags_order_by_more_posts()[:10]

    context = {
        "posts": ten_latest_posts,
        "number_of_pages": number_of_pages,
        "current_page_start_from_1": current_page + 1,
        "tags": ten_most_used_tags,
    }
    return render(request, "main_blog/index.html", context)


def post_view(request, post_id):
    post = Post.objects.get(id=post_id)

    if post.description_format == "rst":
        post.description = rst_to_html(post.description)
    elif post.description_format == 'md':
        post.description = md_to_html(post.description)

    context = {
        "post": post,
    }
    return render(request, "main_blog/post_view.html", context)


def tag_view(request, tag_name):
    tag = Tag.objects.get(name=tag_name)

    count_of_posts = tag.post_set.count()

    number_of_pages = (
            count_of_posts // page_divide + (count_of_posts % page_divide > 0) * 1
    )

    current_page = 0
    try:
        current_page = int(request.GET["page"]) - 1
    except KeyError:
        pass

    start = current_page * page_divide
    end = min(start + page_divide, count_of_posts)

    ten_latest_posts = tag.post_set.all()[start:end]

    context = {
        "tag": tag,
        "posts": ten_latest_posts,
        "number_of_pages": number_of_pages,
        "current_page_start_from_1": current_page + 1,
    }
    return render(request, "main_blog/tag_view.html", context)


def about_me(request):
    return render(request, "main_blog/about_me.html")
