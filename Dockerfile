FROM python:3.9.5-slim AS runtime-deps

# Install runtime dependencies
RUN set -ex \
		&& apt-get update && apt-get install -y --no-install-recommends \
				# Needed for simpleaudio
				libasound2-dev

FROM runtime-deps AS build-deps

WORKDIR /build

COPY Pipfile* /build/

# Install build dependencies
RUN set -ex \
		&& apt-get update && apt-get install -y --no-install-recommends \
				gcc \
				libnacl-dev \
				libffi-dev \
				libc6-dev \
		\
		&& pip install pipenv \
		&& PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

FROM runtime-deps

COPY --from=build-deps /build/.venv /.venv

COPY /bot /bot

ENV PATH="/.venv/bin:$PATH"

CMD ["python3", "-m", "bot"]