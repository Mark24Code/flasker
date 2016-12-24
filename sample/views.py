from flask import render_template, flash, redirect, url_for
from sample import bp


@bp.route('')
def index():
    return render_template('sample/sample.html',name="SAMPLE")
