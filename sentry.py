import sentry_sdk

sentry_sdk.init(
    dsn="https://8f8165d5356fd2206611a4b1b9ab5f7e@o4509704900837376.ingest.us.sentry.io/4509704905162752",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)