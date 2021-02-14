from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

from django.shortcuts import redirect

from blog_project.forms import RegisterForm, CommentForm
from blog_project.models import Post, Status

User = get_user_model()


class RegisterFormView(generic.FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.save()

        username = self.request.POST['username']
        password = self.request.POST['password1']

        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(RegisterFormView, self).form_valid(form)


class UpdateProfileView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'users/update_profile.html'
    success_url = reverse_lazy('index')
    success_message = 'Profile updated'

    def get_object(self, queryset=None):
        user = self.request.user
        return user


class PostListView(generic.ListView):
    queryset = Post.objects.filter(published_state=Status.PUBLISHED).order_by('title')
    template_name = 'index.html'
    paginate_by = 3


class PostDetailView(SuccessMessageMixin, generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = self.get_object().comments.filter(is_published=True)
        comment_form = CommentForm()
        context.update({'comments': comments, 'comment_form': comment_form})
        return context

    # post comments
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = self.object
            new_comment.save()
            messages.success(request, 'Your comment sent to moderators')
            return redirect('post_detail', pk=self.object.pk)
        context = self.get_context_data(object=self.object)
        context['comment_form'] = comment_form
        return self.render_to_response(context)


class PostCreateView(LoginRequiredMixin, generic.CreateView, SuccessMessageMixin, ):
    model = Post
    template_name = 'blog/post_create.html'
    fields = ['title', 'short_description', 'image', 'published_state', 'full_description']
    success_url = reverse_lazy('index')
    success_message = 'Post created'

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)


class UsersListView(generic.ListView):
    model = User
    template_name = 'users/user_list.html'
    paginate_by = 20


class UserDetailView(generic.DetailView):
    model = User
    template_name = 'users/user_details.html'


class UserPostsListView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'users/user_posts.html'

    def get_object(self, queryset=None):
        user = self.request.user
        return user

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)


class UpdatePostView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Post
    fields = ['title', 'published_state', 'short_description', 'image', 'full_description']
    template_name = 'blog/update_post.html'
    success_url = reverse_lazy('user_posts')
    success_message = 'Post updated'

    # Only author can see his posts
    def get_queryset(self):
        queryset = super(UpdatePostView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

