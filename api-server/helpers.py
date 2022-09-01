def get_domain(service: str, port: int = 8000) -> str:
    return f"http://{service}:{port}"
