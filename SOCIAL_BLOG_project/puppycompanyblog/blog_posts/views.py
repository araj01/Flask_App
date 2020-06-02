from flask import render_template, url_for, flash,redirect, request, Blueprint, abort
from flask_login import current_user, login_required
from puppycompanyblog import db
from puppycompanyblog.models import BlogPost
from puppycompanyblog.blog_posts.forms import BlogPostForm

blog_posts = Blueprint('blog_posts', __name__)

#create blogpost
@blog_posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = BlogPostForm()

    if form.validate_on_submit():

        blog_post = BlogPost(title=form.title.data, #form
                            text=form.text.data, #form
                            user_id=current_user.id) #from currently logged in user
        db.session.add(blog_post)
        db.session.commit()
        flash('Blog Post Created')  
        return redirect(url_for('core.index'))

    return render_template('create_post.html', form=form)               

# blog post(view)
@blog_posts.route('/<int:blog_post_id>')#<...> is used so that users can enter the /post id, and int is integer
def blog_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)#inorder to successfully query we use int in route so it will look for an integer rather than string
    return render_template("blog_post.html", title=blog_post.title,
                            date=blog_post.date, post=blog_post, author=blog_post.author)


#update
@blog_posts.route('/<int:blog_post_id>/update', methods=['GET', 'POST'])
@login_required
def update(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)

    if blog_post.author != current_user:
        abort(403)#permission error codes
    
    form = BlogPostForm()

    if form.validate_on_submit():

        blog_post.title = form.title.data #form
        blog_post.text = form.text.data #form
       
        db.session.commit()
        flash('Blog Post Updated')  
        return redirect(url_for('blog_posts.blog_post', blog_post_id=blog_post_id))#redirects to blog_post view which takes blog post id

#to make sure original text and title is maintained the first time when they need to update
    elif request.method == 'GET':
        form.title.data = blog_post.title
        form.text.data = blog_post.text
        
    return render_template('create_post.html', title='Updating', form=form)               

#delete
@blog_posts.route('/<int:blog_post_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_post(blog_post_id):

    blog_post = BlogPost.query.get_or_404(blog_post_id)
    if blog_post.author != current_user:
        abort(403)

    db.session.delete(blog_post)
    db.session.commit()
    flash('Blog Post Deleted')
    return redirect(url_for('core.index'))

    #there wont be delete.html instead there will be a button that executes this