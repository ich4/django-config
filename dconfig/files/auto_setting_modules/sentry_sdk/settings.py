
SENTRY_DSN = getattr(configs, 'SENTRY_DSN', False)
SENTRY_ENVIRONMENT = getattr(configs, 'SENTRY_ENVIRONMENT', 'production')
SENTRY_ENABLE_TRACING = getattr(configs, 'SENTRY_ENABLE_TRACING', False)
SENTRY_TRACES_SAMPLE_RATE = getattr(configs, 'SENTRY_TRACES_SAMPLE_RATE', 1.0)
SENTRY_SEND_DEFAULT_PII = getattr(configs, 'SENTRY_SEND_DEFAULT_PII', True)


if SENTRY_DSN:
    import sentry_sdk

    from sentry_sdk.integrations.django import DjangoIntegration


    sentry_sdk.init(
        SENTRY_DSN,
        integrations=[DjangoIntegration()],
        send_default_pii=SENTRY_SEND_DEFAULT_PII,
        enable_tracing=SENTRY_ENABLE_TRACING,
        environment=SENTRY_ENVIRONMENT,
        traces_sample_rate=SENTRY_TRACES_SAMPLE_RATE,
    )

    LOGGING['formatters']['verbose']  = {
        'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
    }
    LOGGING['handlers']['console']['formatter'] = 'verbose'
