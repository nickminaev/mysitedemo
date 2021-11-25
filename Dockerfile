FROM ruby:2.5.0-alpine3.7
RUN apk update
RUN apk add g++ gcc make musl-dev
RUN gem install jekyll bundler
WORKDIR /
RUN jekyll new myblog --blank
WORKDIR /myblog
COPY Gemfile ./
RUN bundle install
RUN rm -f index.md
RUN rm -rf assets _data _layouts _includes _ssas
COPY _config.yml 404.html about.markdown index.markdown ./
COPY _posts/ ./_posts/
ENTRYPOINT ["bundle"]
CMD ["exec", "jekyll", "serve", "--host=0.0.0.0"]
