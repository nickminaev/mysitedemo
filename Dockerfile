FROM ruby:2.5.0-alpine3.7
RUN apk update
RUN apk add g++ gcc make musl-dev
RUN gem install jekyll bundler
WORKDIR /site
COPY Gemfile ./
RUN bundle install
