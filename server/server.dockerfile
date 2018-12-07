FROM tutum/nginx

RUN mkdir -p /root/certs/delcien.usal.es/
COPY ssl_certificates/* /root/certs/delcien.usal.es/
RUN ls /root/certs/delcien.usal.es
RUN rm /etc/nginx/sites-enabled/default
ADD sites-enabled/ /etc/nginx/sites-enabled

EXPOSE 80
EXPOSE 443
