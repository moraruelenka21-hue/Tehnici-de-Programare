from checker import (
    SITES,
    build_url,
    check_headers,
    is_https,
    retry_check,
    scan_sites,
    show_response,
)


def main():
    example_url = build_url("example.com", "/login")
    print(f"URL construit: {example_url}")
    print(f"Foloseste HTTPS: {is_https(example_url)}\n")

    print("Raspunsul primului site:")
    show_response(SITES[0])

    print("\nVerificarea site-urilor:")
    scan_sites()

    print("\nAntete de securitate:")
    for url in SITES:
        if "response-headers" in url:
            result = check_headers(url)
            print(url)
            print(f"Antete gasite: {result['present']}")
            print(f"Antete lipsa: {result['missing']}")
            print(f"Scor: {result['score']}%")

    print("\nReincercarea site-ului cu raspuns aleatoriu:")
    result = retry_check(SITES[-1])
    print(f"Status: {result['status']}")
    print(f"Incercari: {result['attempts']}")


if __name__ == "__main__":
    main()
