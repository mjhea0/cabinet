from flask import render_template, redirect, url_for, request, flash
from app import app, db
from models import Post

@app.route('/')
@app.route('/index')
def index():
	posts = Post.query
	return render_template('index.html',
		title = 'Home',
		posts = posts)

@app.route('/view/<int:post_id>')
def view(post_id):
	post = Post.query.get(post_id)
	return render_template('post.html',
		title = post.title,
		post = post)

@app.route('/create', methods = ['GET', 'POST'])
def create():
	if request.method == 'POST':
		post = Post(
			title = request.form['title'], 
			body = request.form['body'])
		db.session.add(post)
		db.session.commit()
		flash('A new post was created.')
		return redirect(url_for('index'))
	return render_template('create.html',
		title = 'Create Post')

@app.route('/edit/<int:post_id>', methods = ['GET', 'POST'])
def edit(post_id):
	post = Post.query.get(post_id)
	if request.method == 'POST':
		post.title = request.form['title']
		post.body = request.form['body']
		db.session.add(post)
		db.session.commit()
		flash('The post has been edited.')
		return redirect(url_for('index'))
	return render_template('edit.html',
		title = 'Edit %s' % post.title,
		post = post)

@app.route('/delete/<int:post_id>', methods = ['GET', 'POST'])
def delete(post_id):
	post = Post.query.get(post_id)
	if request.method == 'POST':
		db.session.delete(post)
		db.session.commit()
		flash('The post has been deleted.')
		return redirect(url_for('index'))
	return render_template('delete.html',
		title = 'Delete %s' % post.title,
		post = post)



