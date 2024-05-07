from django.shortcuts import render, redirect
from SoftwareTesting_Selenium_Docker.models.industry_model import IndustryModel
from SoftwareTesting_Selenium_Docker.models.blog_model import BlogModel
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import transaction


def login(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)

            return redirect("/index.html")
        else:
            return render(request, "login.html", {"Error": True})

    else:
        return render(request, "login.html")


def register(request):

    if request.method == "POST":

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        user.save()

        return redirect("/login.html")
    else:
        return render(request, "Register.html")


def logout(request):
    auth.logout(request)
    return redirect("/login.html")


def index(request):
    if request.user.is_authenticated:
        return render(request, "index.html")
    else:
        return redirect("/login.html")


def add_blog(request):
    if request.user.is_authenticated:

        if request.method == "POST":

            imageURL = request.POST["image"]
            title = request.POST["title"]
            category = request.POST["category"]
            author = request.POST["author"]
            content = request.POST["content"]

            blog = {
                "Image": imageURL,
                "Title": title,
                "Category": category,
                "Author": author,
                "Content": content,
            }

            with transaction.atomic():
                b = BlogModel(**blog)
                b.save()

            return render(
                request,
                "success.html",
                {
                    "message": "Blog Post is saved successfully",
                    "redirect_url": "/blog.html",
                },
            )

        else:
            return render(request, "add-blog.html")
    else:
        return redirect("/login.html")


def add_industry(request):

    if request.user.is_authenticated:

        if request.method == "POST":

            title = request.POST["title"]
            description = request.POST["description-content"]
            list_items = request.POST["list-items"]
            imageUrl = request.POST["image"]
            history_sub_title = request.POST["history-timeline-subtitle"]
            history_title = request.POST["history-timeline-title"]
            history_time_line_year = request.POST["history-timeline-year"]
            history_time_line_description = request.POST["history-timeline-description"]

            industry = {
                "Title": title,
                "Description": description,
                "ListItems": list_items,
                "Image": imageUrl,
                "HistorySubTitle": history_sub_title,
                "HistoryTitle": history_title,
                "HistoryTimeLineYear": history_time_line_year,
                "HistoryTimeLineDescription": history_time_line_description,
            }

            with transaction.atomic():
                i = IndustryModel(**industry)
                i.save()

            return render(
                request,
                "success.html",
                {
                    "message": "Inudstry is saved successfully",
                    "redirect_url": "/industries.html",
                },
            )

        else:
            return render(request, "add-industry.html")
    else:
        return redirect("/login.html")


def blog(request):
    if request.user.is_authenticated:
        blogs = BlogModel.objects.all()
        return render(request, "blog.html", {"blogs": blogs})
    else:
        return redirect("/login.html")


def blog_single_post(request):
    if request.user.is_authenticated:
        post_id = request.GET["post_id"]
        post = BlogModel.objects.get(pk=post_id)
        return render(request, "blog-single-post.html", {"post": post})
    else:
        return redirect("/login.html")


def industries(request):
    if request.user.is_authenticated:
        return render(request, "industries.html")
    else:
        return redirect("/login.html")


def industries_single_industry(request):
    if request.user.is_authenticated:
        return render(request, "industries-single-industry.html")
    else:
        return redirect("/login.html")


def home_modern(request):
    if request.user.is_authenticated:
        return render(request, "home-modern.html")
    else:
        return redirect("/login.html")


def home_classic(request):
    if request.user.is_authenticated:
        return render(request, "home-classic.html")
    else:
        return redirect("/login.html")


def about(request):
    if request.user.is_authenticated:
        return render(request, "about-us.html")
    else:
        return redirect("/login.html")


def error(request):
    if request.user.is_authenticated:
        return render(request, "404.html")
    else:
        return redirect("/login.html")


def awards(request):
    if request.user.is_authenticated:
        return render(request, "awards.html")
    else:
        return redirect("/login.html")


def careers(request):
    if request.user.is_authenticated:
        return render(request, "careers.html")
    else:
        return redirect("/login.html")


def case_studies_classic(request):
    if request.user.is_authenticated:
        return render(request, "case-studies-classic.html")
    else:
        return redirect("/login.html")


def case_studies_grid(request):
    if request.user.is_authenticated:
        return render(request, "case-studies-grid.html")
    else:
        return redirect("/login.html")


def case_studies_modern(request):
    if request.user.is_authenticated:
        return render(request, "case-studies-modern.html")
    else:
        return redirect("/login.html")


def case_studies_single(request):
    if request.user.is_authenticated:
        return render(request, "case-studies-single.html")
    else:
        return redirect("/login.html")


def coming_soon(request):
    if request.user.is_authenticated:
        return render(request, "coming-soon.html")
    else:
        return redirect("/login.html")


def contact(request):
    if request.user.is_authenticated:
        return render(request, "contact-us.html")
    else:
        return redirect("/login.html")


def faqs(request):
    if request.user.is_authenticated:
        return render(request, "faqs.html")
    else:
        return redirect("/login.html")


def it_solutions_single(request):
    if request.user.is_authenticated:
        return render(request, "it-solutions-single.html")
    else:
        return redirect("/login.html")


def it_solutions(request):
    if request.user.is_authenticated:
        return render(request, "it-solutions.html")
    else:
        return redirect("/login.html")


def leadership_team(request):
    if request.user.is_authenticated:
        return render(request, "leadership-team.html")
    else:
        return redirect("/login.html")


def pricing(request):
    if request.user.is_authenticated:
        return render(request, "pricing.html")
    else:
        return redirect("/login.html")


def request_quote(request):
    if request.user.is_authenticated:
        return render(request, "request-quote.html")
    else:
        return redirect("/login.html")


def search(request):
    if request.user.is_authenticated:
        return render(request, "search.html")
    else:
        return redirect("/login.html")


def why_choose_us(request):
    if request.user.is_authenticated:
        return render(request, "why-us.html")
    else:
        return redirect("/login.html")


def success(request):
    if request.user.is_authenticated:
        return render(request, "success.html")
    else:
        return redirect("/login.html")
