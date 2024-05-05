from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("login.html", views.login, name="login"),
    path("login/", views.login, name="login"),
    path("register.html", views.register, name="register"),
    path("index.html", views.index, name="index"),
    path("blog.html", views.blog, name="blog"),
    path("blog-single-post.html", views.blog_single_post, name="blog single post"),
    path("home-modern.html", views.home_modern, name="home modern"),
    path("home-classic.html", views.home_classic, name="home classic"),
    path("about-us.html", views.about, name="about us"),
    path("404.html", views.error, name="404"),
    path("awards.html", views.awards, name="awards"),
    path("careers.html", views.careers, name="careers"),
    path(
        "case-studies-classic.html",
        views.case_studies_classic,
        name="case-studies-classic",
    ),
    path("case-studies-grid.html", views.case_studies_grid, name="case-studies-grid"),
    path(
        "case-studies-modern.html",
        views.case_studies_modern,
        name="case-studies-modern",
    ),
    path(
        "case-studies-single.html",
        views.case_studies_single,
        name="case-studies-single",
    ),
    path("coming-soon.html", views.coming_soon, name="coming-soon"),
    path("contact-us.html", views.contact, name="contact-us"),
    path("faqs.html", views.faqs, name="faqs"),
    path(
        "industries-single-industry.html",
        views.industries_single_industry,
        name="industries-single-industry",
    ),
    path("industries.html", views.industries, name="industries"),
    path(
        "it-solutions-single.html",
        views.it_solutions_single,
        name="it-solutions-single",
    ),
    path("it-solutions.html", views.it_solutions, name="it-solutions"),
    path("leadership-team.html", views.leadership_team, name="leadership-team"),
    path("pricing.html", views.pricing, name="pricing"),
    path("request-quote.html", views.request_quote, name="request-quote"),
    path("search.html", views.search, name="search"),
    path("why-us.html", views.why_choose_us, name=""),
    path("add-blog.html", views.add_blog, name="add-blog"),
]
