
# Kullanıcı İşlemleri API Projesi
Bu proje, Django REST Framework ve Vue.js kullanılarak oluşturulmuş RESTful bir API'dir. Kullanıcılar ve onlara ait ilişkili verilerin görüntülenmesini sağlar.
## Özellikler
- Kullanıcılar ve onlara ait adres ile şirket bilgilerini görüntüleme
- Kullanıcılara ait albümleri ve albüm içindeki fotoğrafları listeleme.
- Gönderileri ve gönderilere ait yorumları listeleme
- Todo listesindeki görevleri görüntüleme
- ModelViewSet kullanılarak yapılandırılmış, ölçeklenebilir API uç noktaları
- Swagger/OpenAPI ile kapsamlı ve test edilebilir API dokümantasyonu
- Veritabanı olarak PostgreSQL kullanımı
- Django admin paneli üzerinden tam CRUD işlemleri yapılabilir
- Vue.js, Tailwind CSS, SASS ve HTML ile oluşturulmuş modern frontend arayüzü
- Geliştirme ve dağıtım için Docker desteği

## Kullanılan Teknolojiler
- Python 3.x
- Django 3.x
- Django REST Framework
- PostgreSQL
- Vue.js
- Tailwind CSS
- SASS
- Docker
- Swagger/OpenAPI dokümantasyonu

# Projeyi Çalıştırma Adımları

## 1. Projeyi Klonlayın

```bash
https://github.com/efnangenc/case.git
```

## 2. Komut Terminalini Açın ve Dizine Gidin

```bash
cd case/user_project
```

## 3. Docker Image'ını Oluşturun

```bash
docker build -t user_project .
```

## 4. Docker Image'ını `.tar.gz` Dosyasına Kaydedin

```bash
docker save user_project -o user_project.tar.gz
```

## 5. `.tar.gz` Dosyasını Yükleyin

```bash
docker load < user_project.tar.gz
```

## 6. Projeyi Docker ile Başlatın

```bash
docker-compose up -d
```

## 7. Var Olan Migrationları Uygulayın (Eğer veritabanı yapılandırılmamışsa)

```bash
docker exec -it user_project-web-1 python manage.py migrate
```

## 8. Seed Verilerini Yükleyin (Eğer veritabanı yapılandırılmamışsa)

```bash
docker exec -it user_project-web-1 python manage.py seed
```

## 9. Süper kullanıcı oluşturun (Admin paneli için)
```bash
docker exec -it user_project-web-1 python manage.py createsuperuser
```


## API dökümanlarına erişim:

Swagger UI: http://localhost:8000/swagger/

OpenAPI JSON: http://localhost:8000/swagger.json

OpenAPI YAML: http://localhost:8000/swagger.yaml

ReDoc UI: http://localhost:8000/redoc/


## İletişim

E-mail: genc.efnan4@gmail.com
