# 1. Temel imaj olarak Python 3.11 slim kullanıyoruz
FROM python:3.11-slim

# 2. Çalışma dizinini belirle
WORKDIR /app

# 3. Gereksinim dosyasını kopyala ve bağımlılıkları yükle
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 4. Proje dosyalarını kopyala
COPY . /app/

# 5. Django'nun runserver komutunu başlat
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
