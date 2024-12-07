# Hatırlatıcı Uygulaması

Bu proje, kullanıcıların hatırlatıcılar ekleyip yönetebileceği bir masaüstü uygulamasıdır. Kullanıcılar, belirli bir saat ve dakikada hatırlatıcılar ekleyebilir ve bu hatırlatıcılar geldiğinde bildirim alabilirler.

## Özellikler

- Kullanıcı dostu arayüz
- Saat ve dakika girişi
- Hatırlatıcı mesajı ekleme
- Aktif hatırlatıcıları görüntüleme
- Hatırlatıcıları silme
- Uygulama kapatıldığında hatırlatıcıları kaydetme ve yükleme
- Günlük sıfırlama ile hatırlatıcıların otomatik olarak aktif hale gelmesi

## Gereksinimler

- Python 3.x
- `customtkinter` kütüphanesi
- `clock` modülü
- `reminders` modülü
- `notifications` modülü

## Kurulum

1. Bu projeyi klonlayın veya indirin:
   ```bash
   git clone https://github.com/faust-lvii/timer
   cd timer
   ```

2. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install customtkinter
   ```

3. Uygulamayı çalıştırın:
   ```bash
   python main.py
   ```

## Kullanım

1. Uygulamayı başlattıktan sonra, "Yeni Hatırlatıc�� Ekle" bölümüne gidin.
2. Saat ve dakika girin (saat 0-23, dakika 0-59 aralığında olmalıdır).
3. Hatırlatıcı mesajınızı girin.
4. "Hatırlatıcı Ekle" butonuna tıklayın.
5. Aktif hatırlatıcılar bölümünde eklediğiniz hatırlatıcıları görebilirsiniz.
6. Hatırlatıcıyı silmek için ❌ butonuna tıklayın.

## Katkıda Bulunma

Bu projeye katkıda bulunmak isterseniz, lütfen bir pull request oluşturun veya sorunlarınızı bildirin.

## Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.
