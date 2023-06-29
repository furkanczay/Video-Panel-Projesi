#### v1.0.0-beta2 | DEV
* Favori videolardan video detay sayfasına erişelemiyordu düzeltildi
* Navbardaki fazla kodlar kaldırıldı
* Video listeleme sayfasındaki filtreleme hatası giderildi
* .env-example güncellendi
* Video favorilere ekleme özelliği eklendi, gerekli view, template ve kontrol yapıları hazırlandı
* Footer üzerinde iyileştirmeler yapıldı, video listesi sayfasında sayfalama işlemi yapıldı ve başlığa göre filtreleme özelliği eklendi
* anonymous_required decorator hazırlandı, login ve login-validate sayfaları için uygulandı
* Profil güncelleme sayfası ve formu hazırlandı gerekli url yapılandırmaları ayarlandı
* Headerda iyileştirmeler yapıldı, eğitmenler için video düzenleme sayfası hazırlandı
* Şifre alanları geri eklendi, hatalar üzerinde düzeltmeler yapıldı, OTP login iyileştirildi, password login için temel hazırlandı
* requirements.txt güncellendi
* Bildirimler açılır alanı devre dışı bırakıldı, bildirim sistemi hazırlandığında tekrar aktif edilecek
* Dil seçici gösterimi devre dışı bırakıldı, çoklu dil desteği ertelendi
* Önyüz headerda iyileştirmeler yapıldı, destekle, sorun bildir ve discord butonları aktif hale getirildi, site içindeki sorunlar modeli ve viewları kaldırıldı github üzerinden yönetilecek
* Admin paneline video yönetim alanı oluşturuldu
* Anasayfada eğitmen video sayısı istatistiği gösterimi ayarlandı
* Signals üzerinde ufak iyileştirmeler yapıldı
* BunnyCDN bağlandı ve videolar, kullanıcı avatarları gibi medya dosyaları cdn ile işlenmeye başlandı
* Yorumlar üzerinde izin ayarlamaları yapıldı ve yorum yap modalındaki başlık hatası giderildi
* Sayfalara giriş sorgusu eklendi ve giriş yapmamış kullanıcıları otomatik login sayfasına yönlendirme ayarlandı
* OTP sistemi oluşturuldu, tek kullanımlık şifre doğrulama süreçleri elden geçirildi, 5 dakika zaman aşımı süresi ayarlandı
* Eğitmen video yükleyince discorda bildirim gitmesi için webhook kütüphanesi yüklendi ve ayarları yapıldı
* Readme dosyası güncellendi
* Önyüz anasayfada düzenlemeler ve iyileştirmeler yapıldı
* Önyüz navbarda iyileştirmeler yapıldı
* Önyüz headerda iyileştirmeler yapıldı
* Önyüz meta etiketleri admin panelden yönetilebilir hale getirildi
* admin panelde sınıf listeleme ekleme ve düzenleme sayfaları hazırlandı
* Admin panel navbarda iyileştirmeler yapıldı
* Admin navbarda düzenlemeler yapıldı
* Kurslar ve kurs kategorileri yönetimi admin panele eklendi
* Listeleme sayfaları düzenlendi, uyarı mesajları için sweetalert entegre edildi
* Tabler icons sisteme dahil edildi ve admin headerında düzenlemeler yapıldı
* Eğitmen, öğrenci ve kullanıcı grupları listeleme sayfalarına ekleme butonları eklendi
* Giriş sayfasında iyileştirmeler yapıldı
* Video yükleme formunda help texts eklendi
* Video yükleme formundaki isim alanı translation uygun hale getirildi
* SuperAdmin üzerinden eğitmen seçimlerine filtreleme getirildi, ve model formlarda düzgün görünmesi için video modelde verbose name işlemi uygulandı
* Video listesi sayfasına sınıf filtrelemesi eklendi
* Video.js kütüphanesinin testleri yapıldı, filtreleme alanına eğitmen bölümü de eklendi
* Video yükleme formunda help texts eklendi
* Video yükleme formundaki isim alanı translation uygun hale getirildi
* SuperAdmin üzerinden eğitmen seçimlerine filtreleme getirildi, ve model formlarda düzgün görünmesi için video modelde verbose name işlemi uygulandı
* Video listesi sayfasına sınıf filtrelemesi eklendi
* Video.js kütüphanesinin testleri yapıldı, filtreleme alanına eğitmen bölümü de eklendi
* Admin panel üzerinde sayfalar hazırlandı, viewlar düzenlendi ve iyileştirmeler yapıldı
* Template üzerinde iyileştirmeler yapıldı ve requirements dosyası oluşturuldu


#### v1.0.0-beta1 | DEV
* Video listeleme sayfasına filtreleme özelliği eklendi ve eğitmen video yükleme formuna yalnızca kendi sınıflarını görmesi için filtreleme yapıldı
* Eğitmen paneli üzerinden eğitmenin kendi videolarına direkt erişmesi için link ayarı yapıldı
* Önyüz header üzerinde iyileştirmeler yapıldı
* Settings model verileri templatetags aracılığıyla template üzerine getirildi, admin panel ve önyüzde veriler ekrana bastırıldı
* Admin panelde öğrenci ekleme, listeleme sayfaları hazırlandı
* Admin panel genel ayarlar düzenleme sayfası oluşturuldu
* Template üzerinde iyileştirmeler yapıldı ve LoginRequired Middleware hazırlandı
* Yorum ekleme modalı oluşturuldu ve view hazırlandı
* Video güncelleme ve silme ayarları yapılandırıldı
* Video yorum özelliği eklendi, toastr kütüphanesi projeye dahil edildi
* Video detay sayfası iyileştirildi
* Videolar sınıflara bağlandı, sınıflar kurslara bağlandı, video detay sayfası güncellendi
* Eğitmen paneli hazırlandı
* Videolar için dosya doğrulayıcı hazırlandı
* Issues model ve template yapısı hazırlandı
* Admin sayfası hazırlandı ve grupların otomatik oluşması için signals hazırlandı
* Profil sayfası view hazırlandı
* Giriş sayfası iyileştirildi
* Crispy forms yüklendi, giriş sayfası güncellendi
* Ayarlamalar, dosya düzenleri ve yapı değişiklikleri yapıldı
* TemplateTags oluşturuldu
* Videopanel projesinin temel yapısı oluşturuldu

