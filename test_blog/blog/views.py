from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm

# Class Based Pagination
# class PostLists(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'index.html'
#     paginate_by = 3

#class PostDetail(generic.DetailView):
#    model = Post
#    template_name = 'post_detail.html'

#Test representation of index.html request
#def index(request):
#    my_dict = {"insert_me": "I am from views.py"}
#    return render(request,'index.html',context=my_dict)

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Function based pagination
def PostLists(request):
    object_list = Post.objects.filter(status=1).order_by('-created_on')
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    return render(request,
                  'index.html',
                  {'page': page,
                   'post_list': post_list})

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm


def contact_view(request):
    new_message = None
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid() and request.recaptcha_is_valid:
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            subject = "{0}. email: {1}".format(name, from_email)
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, 'contact_form@example.com', ['my_contact@example.com'])
                new_message = message
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    return render(request, "contact.html", {'form': form, 'new_message': new_message})
