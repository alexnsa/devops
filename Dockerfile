FROM python3.6
WORKDIR /app
COPY . .
EXPOSE 5000
RUN  pip install -r requirements.txt
ENTRYPOINT ['/usr/bin/python', 'app.py']
