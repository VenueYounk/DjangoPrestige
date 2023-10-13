from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse

from wagtail.models import Page
from wagtail.search.models import Query
from home.models import ServicesPage, Lawyer


def search(request):
    search_query = request.GET.get("query", None)
    page = request.GET.get("page", 1)

    # Search
    if search_query:
        search_results = Page.objects.live().search(search_query)
        query = Query.get(search_query)

        # Record hit
        query.add_hit()
    else:
        search_results = Page.objects.none()

    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return TemplateResponse(
        request,
        "search/search.html",
        {
            "search_query": search_query,
            "search_results": search_results,
        },
    )


def search_service(request):
    q = request.GET.get("q") if request.GET.get("q") else ""
    if q != "":
        services = ServicesPage.objects.live().filter(title__icontains=q)[:12]
        return TemplateResponse(
            request,
            "home/modules/services_search_results.html",
            {"pages": services},
        )


def search_lawyer_and_services(request):
    q = request.GET.get("q") if request.GET.get("q") else ""
    if q != "":
        lawyers = Lawyer.objects.live().filter(title__icontains=q)
        services = ServicesPage.objects.live().filter(title__icontains=q)
        result = lawyers.union(services).order_by("title")
        return TemplateResponse(
            request,
            "home/modules/lawyer_and_services_search_results.html",
            {"pages": result},
        )
