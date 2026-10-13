from checker import (
    SITES,
    build_url,
    check_headers,
    check_site,
    is_https,
    retry_check,
    scan_sites,
    show_response,
)


def main():
    print("Partea 1: build_url si is_https")
    print("build_url fara slash:", build_url("example.com", "login"))
    print("build_url cu slash:", build_url("example.com", "/login"))
    print("is_https pentru HTTPS:", is_https("https://example.com"))
    print("is_https pentru HTTP:", is_https("http://example.com"))

    print("\nPartea 2: show_response")
    print("Raspuns pentru un site functional:")
    show_response("https://example.com")
    print("Raspuns pentru un site inexistent:")
    show_response("http://this-site-does-not-exist.invalid")

    print("\nPartea 3: check_site pentru fiecare adresa din SITES")
    for url in SITES:
        print(url, "->", check_site(url))

    print("\nPartea 4: scan_sites")
    scan_sites()

    print("\nPartea 5: check_headers")
    print(SITES[10], "->", check_headers(SITES[10]))
    print(SITES[11], "->", check_headers(SITES[11]))
    print("Site inexistent ->", check_headers(SITES[9]))

    print("\nPartea 6: retry_check")
    print("retry_check pentru status 200:", retry_check(SITES[3]))
    print("retry_check pentru status 404:", retry_check(SITES[6]))
    print("retry_check pentru status 500:", retry_check(SITES[7]))
    print("retry_check pentru site inexistent:", retry_check(SITES[9]))


if __name__ == "__main__":
    main()
