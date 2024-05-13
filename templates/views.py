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

        if username.strip() == "" or password.strip() == "":
            return render(
                request,
                "login.html",
                {"Error": True, "Message": "All fields are required"},
            )

        else:

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("/index.html")
            else:
                return render(
                    request,
                    "login.html",
                    {"Error": True, "Message": "Invalid username or password!"},
                )

    else:
        return render(request, "login.html")


def register(request):

    if request.method == "POST":

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if username.strip() == "" or email.strip() == "" or password.strip() == "":

            return render(
                request,
                "Register.html",
                {"Error": True, "Message": "All fields are required"},
            )

        elif (
            User.objects.filter(username=username).exists()
            or User.objects.filter(email=email).exists()
        ):
            return render(
                request,
                "Register.html",
                {"Error": True, "Message": "Username or Email already exists!"},
            )

        else:
            user = User.objects.create_user(
                username=username, email=email, password=password
            )
            user.save()

            return render(
                request,
                "success.html",
                {
                    "message": "User is registered successfully",
                    "redirect_url": "/login.html",
                },
            )
    else:
        return render(request, "Register.html")


def logout(request):
    auth.logout(request)
    return redirect("/login.html")


def index(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, "index.html", {"username": username})
    else:
        return redirect("/login.html")


def add_blog(request):
    if request.user.is_authenticated:

        username = request.user.username

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

            if (
                not title.strip()
                or not content.strip()
                or not author.strip()
                or not category.strip()
            ):
                return redirect("/404.html")

            else:
                with transaction.atomic():
                    b = BlogModel(**blog)
                    b.save()

                return render(
                    request,
                    "success.html",
                    {
                        "message": "Blog Post is saved successfully",
                        "redirect_url": "/blog.html",
                        "username": username,
                    },
                )

        else:
            return render(request, "add-blog.html", {"username": username})
    else:
        return redirect("/login.html")


def add_industry(request):

    if request.user.is_authenticated:

        username = request.user.username

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

            if (
                not title.strip()
                or not description.strip()
                or not history_sub_title.strip()
                or (
                    history_sub_title.strip()
                    and not history_title.strip()
                    and not history_time_line_year.strip()
                    and not history_time_line_description.strip()
                )
            ):
                return redirect("/404.html")

            else:

                with transaction.atomic():
                    i = IndustryModel(**industry)
                    i.save()

                return render(
                    request,
                    "success.html",
                    {
                        "message": "Inudstry is saved successfully",
                        "redirect_url": "/industries.html",
                        "username": username,
                    },
                )

        else:
            return render(request, "add-industry.html", {"username": username})
    else:
        return redirect("/login.html")


def blog(request):
    if request.user.is_authenticated:
        username = request.user.username
        blogs = BlogModel.objects.all()
        return render(request, "blog.html", {"blogs": blogs, "username": username})
    else:
        return redirect("/login.html")


def blog_single_post(request):
    if request.user.is_authenticated:
        username = request.user.username
        post_id = request.GET["post_id"]
        post = BlogModel.objects.get(pk=post_id)
        return render(
            request, "blog-single-post.html", {"post": post, "username": username}
        )
    else:
        return redirect("/login.html")


def industries(request):
    if request.user.is_authenticated:
        username = request.user.username
        industries = IndustryModel.objects.all()
        return render(
            request, "industries.html", {"industries": industries, "username": username}
        )
    else:
        return redirect("/login.html")


def industries_single_industry(request):
    if request.user.is_authenticated:
        username = request.user.username
        industry_id = request.GET["industry_id"]
        industry = IndustryModel.objects.get(pk=industry_id)

        years = industry.HistoryTimeLineYear.split("\n")
        descriptions = industry.HistoryTimeLineDescription.split("\n")
        timeline_data = zip(years, descriptions)

        return render(
            request,
            "industries-single-industry.html",
            {
                "industry": industry,
                "timeline_data": timeline_data,
                "username": username,
            },
        )
    else:
        return redirect("/login.html")


def home_modern(request):
    if request.user.is_authenticated:
        return render(request, "home-modern.html")
    else:
        return redirect("/login.html")


def home_classic(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, "home-classic.html", {"username": username})
    else:
        return redirect("/login.html")


def about(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, "about-us.html", {"username": username})
    else:
        return redirect("/login.html")


def error(request):
    if request.user.is_authenticated:
        return render(request, "404.html")
    else:
        return redirect("/login.html")


def awards(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, "awards.html", {"username": username})
    else:
        return redirect("/login.html")


def careers(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, "careers.html", {"username": username})
    else:
        return redirect("/login.html")


def case_studies_classic(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, "case-studies-classic.html", {"username": username})
    else:
        return redirect("/login.html")


def case_studies_grid(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, "case-studies-grid.html", {"username": username})
    else:
        return redirect("/login.html")


def case_studies_modern(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, "case-studies-modern.html", {"username": username})
    else:
        return redirect("/login.html")


def case_studies_single(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, "case-studies-single.html", {"username": username})
    else:
        return redirect("/login.html")


def coming_soon(request):
    if request.user.is_authenticated:
        return render(request, "coming-soon.html")
    else:
        return redirect("/login.html")


def contact(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, "contact-us.html", {"username": username})
    else:
        return redirect("/login.html")


def faqs(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, "faqs.html", {"username": username})
    else:
        return redirect("/login.html")


def it_solutions_single(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, "it-solutions-single.html", {"username": username})
    else:
        return redirect("/login.html")


def it_solutions(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, "it-solutions.html", {"username": username})
    else:
        return redirect("/login.html")


def leadership_team(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, "leadership-team.html", {"username": username})
    else:
        return redirect("/login.html")


def pricing(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, "pricing.html", {"username": username})
    else:
        return redirect("/login.html")


def request_quote(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, "request-quote.html", {"username": username})
    else:
        return redirect("/login.html")


def search(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, "search.html", {"username": username})
    else:
        return redirect("/login.html")


def why_choose_us(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, "why-us.html", {"username": username})
    else:
        return redirect("/login.html")


def success(request):
    if request.user.is_authenticated:
        return render(request, "success.html")
    else:
        return redirect("/login.html")
