FROM python:3
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
WORKDIR /api
COPY /api /api
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3", "app.py"]