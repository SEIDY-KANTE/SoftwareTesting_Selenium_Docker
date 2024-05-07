from django.shortcuts import render, redirect


def login(request):

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        print("User logged in")

        print("Email: ", email)
        print("Password: ", password)

        return redirect("/index.html")

    else:
        return render(request, "login.html")


def register(request):

    if request.method == "POST":

        email = request.POST["email"]
        password = request.POST["password"]

        print("User created")
        print("Email: ", email)
        print("Password: ", password)

        return redirect("/login")
    else:
        return render(request, "Register.html")


def index(request):
    return render(request, "index.html")


def add_blog(request):

    if request.method == "POST":

        imageURL = request.POST["image"]
        title = request.POST["title"]
        category = request.POST["category"]
        author = request.POST["author"]
        content = request.POST["content"]

        blog = {
            "image": imageURL,
            "title": title,
            "category": category,
            "author": author,
            "content": content,
        }


        print(blog)

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


def add_industry(request):

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
            "title": title,
            "description": description,
            "list_items": list_items,
            "imageUrl": imageUrl,
            "history_sub_title": history_sub_title,
            "history_title": history_title,
            "history_time_line_year": history_time_line_year,
            "history_time_line_description": history_time_line_description,
        }


        print(industry)

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


def blog(request):
    return render(request, "blog.html")


def blog_single_post(request):
    return render(request, "blog-single-post.html")


def home_modern(request):
    return render(request, "home-modern.html")


def home_classic(request):
    return render(request, "home-classic.html")


def about(request):
    return render(request, "about-us.html")


def error(request):
    return render(request, "404.html")


def awards(request):
    return render(request, "awards.html")


def careers(request):
    return render(request, "careers.html")


def case_studies_classic(request):
    return render(request, "case-studies-classic.html")


def case_studies_grid(request):
    return render(request, "case-studies-grid.html")


def case_studies_modern(request):
    return render(request, "case-studies-modern.html")


def case_studies_single(request):
    return render(request, "case-studies-single.html")


def coming_soon(request):
    return render(request, "coming-soon.html")


def contact(request):
    return render(request, "contact-us.html")


def faqs(request):
    return render(request, "faqs.html")


def industries_single_industry(request):
    return render(request, "industries-single-industry.html")


def industries(request):
    return render(request, "industries.html")


def it_solutions_single(request):
    return render(request, "it-solutions-single.html")


def it_solutions(request):
    return render(request, "it-solutions.html")


def leadership_team(request):
    return render(request, "leadership-team.html")


def pricing(request):
    return render(request, "pricing.html")


def request_quote(request):
    return render(request, "request-quote.html")


def search(request):
    return render(request, "search.html")


def why_choose_us(request):
    return render(request, "why-us.html")


def success(request):
    return render(request, "success.html")