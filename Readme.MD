<a name="readme-top"></a>


<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="assets/static/base/img/acunmedya_akademi_logo.png" alt="Logo" width="80" height="80">

  <h3 align="center">Acunmedya Akademi Video Panel</h3>

 <p align="center">
    AcunMedya Akademi öğrencileri için geliştirilmiş ders tekrar (video) paneli
    <br />
    <a href="#">
        <a href="#readme-installation">Kurulum Aşamaları</a>
    </a>
    ·
    <a href="https://github.com/furkannozay/AcademyProject/issues">Hata Raporla</a>
    ·
    <a href="https://github.com/furkannozay/AcademyProject/issues">Öneride Bulun</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## Proje Hakkında

Derslerden sonra tekrar yapma gereksinimi doğduğunda videolara
erişmek epey yorucu olabiliyordu, bu sebeple bilgimi bu sorunu
düzeltmek adına kullanmak istedim, ve ortaya bu proje çıktı! <br>

### Kullanılan Teknolojiler

![Python]
![Django] 
![HTML] 
![CSS]
![Bootstrap]
![Javascript]
![SQLite]
![Jquery]

### Kullanılan Temalar
Önyüz: Flowbite UI <br>
Admin: Tabler Theme

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## <a name="readme-installation"></a> Kurulum Aşamaları
#### 1. Adım
- Repoyu klonlayın

    ```bash
    git clone https://github.com/furkannozay/AcademyProject.git
    ```

#### 2. Adım
- Virtual Environment oluşturun
  ```bash
  python -m venv venv
  ```

#### 3. Adım
- Virtual Environment'ı aktif edin
  - Windows için:
    ```bash
    venv\Scripts\activate.bat
    ```
  - Linux & Mac için:
    ```bash
    source venv/bin/activate
    ```

#### 4. Adım
- Gerekli kütüphaneleri yükleyin
  - Windows için:
    ```bash
    pip install -r requirements.txt
    ```
  - Linux & Mac için:
    ```bash
    pip3 install -r requirements.txt
    ```

#### 5. Adım
- Veritabanını oluşturun
  - Windows için:
    ```bash
    python manage.py migrate
    ```
  - Linux & Mac için:
    ```bash
    python3 manage.py migrate
    ```

#### 6. Adım
- Superuser oluşturun
  - Windows için:
    ```bash
    python manage.py createsuperuser
    ```
  - Linux & Mac için:
    ```bash
    python3 manage.py createsuperuser
    ```

#### 7. Adım

- .env dosyasını oluşturun
- .env-example dosyasındaki içerikleri içerisine kopyalayın
- SECRET_KEY'i oluşturun:
  ```bash
  python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
  ```
- .env dosyasını düzenleyin:
  ```
  - EMAIL_HOST= Mail sunucunuzun adresi
  - EMAIL_HOST_USER= Mail sunucunuzun kullanıcı adı
  - EMAIL_HOST_PASSWORD= Mail sunucunuzun şifresi
  - WEBHOOK_URL= Discord Webhook URL'niz
  - DEBUG= True/False
  - BUNNY_USERNAME= BunnyCDN storage adı
  - BUNNY_PASSWORD= BunnyCDN storage şifresi
  - BUNNY_REGION= BunnyCDN storage bölgesi
  ```


#### 8. Adım
- Sunucuyu çalıştırın
  - Windows için:
    ```bash
    python manage.py runserver
    ```
  - Linux & Mac için:
    ```bash
    python3 manage.py runserver
    ```
    
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap
- [ ] Çoklu Dil Desteği
    - [ ] İngilizce
    - [ ] Almanca
- [ ] Faydalı Linkler Özelliği
- [ ] Ödev Takip Sistemi
- [ ] Personel Destek Sistemi
- [ ] İstek Öneri Şikayet Sistemi
- [ ] Yoklama Sistemi
    - [ ] Eğitmen Yoklama Oluşturma
    - [ ] Personel Yoklama Raporu
    - [ ] Öğrenci Kişisel Yoklama Raporu
- [ ] Ders Anketleri Sistemi
- [ ] Vitrin Site
- [ ] Başvuru Sistemi (Gelişmiş)
- [ ] Aday Öğrenci Sistemi
<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Bana Ulaşın

[![Linkedin][linkedin-shield]][linkedin-url] 
[![Instagram][instagram-shield]][instagram-url]
[![Github][github-shield]][github-url]
[![Website][website-shield]][website-url]







[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/furkannozay
[instagram-shield]: https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white
[instagram-url]: https://instagram.com/furkanczay
[github-shield]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[github-url]: https://github.com/furkannozay
[website-shield]: https://img.shields.io/badge/website-000000?style=for-the-badge&logo=About.me&logoColor=white
[website-url]: https://furkanozay.net
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[HTML]: https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white
[CSS]: https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white
[Javascript]: https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black
[Bootstrap]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[SQLite]: https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white
[JQuery]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white

