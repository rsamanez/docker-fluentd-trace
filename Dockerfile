FROM fluent/fluentd:v1.11-1
USER root
COPY fluent-plugin-newrelic-trace-1.0.49.gem /fluentd/etc/plugin/
COPY fluent.conf /fluentd/etc/
RUN fluent-gem install fluent-plugin-newrelic \
 && fluent-gem install /fluentd/etc/plugin/fluent-plugin-newrelic-trace-1.0.49.gem

ENV HTTPS_PROXY="https://10.0.0.210:8090"

USER fluent
