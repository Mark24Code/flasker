from flask import render_template, flash, redirect, url_for
from blog import bp

@bp.route('')
def index():
    return render_template("blog/blog.html",name="BLOG")
