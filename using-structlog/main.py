import structlog

log = structlog.get_logger()
log.msg("greeted", whom="world", more_than_a_string=[1, 2, 3])

logger = structlog.get_logger()


def view(request):
    log = logger.bind(
        user_agent=request.get("HTTP_USER_AGENT", "UNKNOWN"),
        peer_ip=request.client_addr,
    )
    foo = request.get("foo")
    if foo:
        log = log.bind(foo=foo)
    if something:
        log.msg("something")
        return "something"
    elif something_else:
        log.msg("something_else")
        return "something_else"
    else:
        log.msg("else")
        return "else"
