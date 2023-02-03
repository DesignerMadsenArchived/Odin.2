from opentelemetry.instrumentation.redis \
    import RedisInstrumentor


class SystemRuntime:
    def __init__(self):
        RedisInstrumentor().instrument()