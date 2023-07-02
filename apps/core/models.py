from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.text import slugify
from .abstracts import AbstractDatesModel
from django_countries.fields import CountryField
from .validators.videos import validate_file_extension
from django.utils.translation import gettext_lazy as _


# AUTHENTICATE MODELS
class UsersManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email adresi gereklidir.")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class Users(AbstractBaseUser, PermissionsMixin, AbstractDatesModel):
    GENDERS = [
        ('Erkek', 'Erkek'),
        ('Kadın', 'Kadın'),
        ('Diğer', 'Diğer'),
    ]
    student_number = models.CharField(_('Öğrenci Numarası'), max_length=20, unique=True, null=True, blank=True)
    username = models.CharField(_('Kullanıcı Adı'), max_length=100, unique=True, null=True, blank=True)
    email = models.EmailField(_('Eposta Adresi'), max_length=150, unique=True)
    first_name = models.CharField(_('Adı'), max_length=120)
    last_name = models.CharField(_('Soyadı'), max_length=120)
    gender = models.CharField(_('Cinsiyet'), max_length=6, choices=GENDERS, null=True, blank=True)
    avatar = models.ImageField(_('Profil Resmi'), upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(_('Biyografi'), null=True, blank=True)
    birth_date = models.DateField(_('Doğum Tarihi'), null=True)
    country = CountryField(_('Ülke'), null=True)
    is_active = models.BooleanField(_('Aktif mi?'), default=True)
    is_staff = models.BooleanField(_('Personel mi?'), default=False)
    objects = UsersManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    force_password_change = models.BooleanField(_('Şifre Değiştirme Gerekliliği'), default=True)

    class Meta:
        db_table = 'users'
        verbose_name = 'Üye'
        verbose_name_plural = 'Üyeler'

    def __str__(self):
        return self.get_full_name()

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = slugify(self.email.split('@')[0])

        # Avatar atanmamışsa varsayılan avatarı atama
        if not self.avatar:
            self.avatar = 'default-avatar.jpg'
        super(Users, self).save(*args, **kwargs)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name


class UserSocialLinks(AbstractDatesModel):
    title = models.CharField(_('Başlık'), max_length=120, null=True, blank=True)
    link = models.URLField(_('Link'), null=True, blank=True)
    user = models.ForeignKey(Users, related_name='social_links', on_delete=models.CASCADE, verbose_name=_('Üye'))

    class Meta:
        db_table = 'social_links'
        verbose_name = _('Sosyal Link')
        verbose_name_plural = _('Sosyal Linkler')

    def __str__(self):
        return self.title


class CourseCategories(AbstractDatesModel):
    name = models.CharField(_('İsim'), max_length=120)

    class Meta:
        db_table = 'course_categories'
        verbose_name = _('Kurs Kategorisi')
        verbose_name_plural = _('Kurs Kategorileri')

    def __str__(self):
        return self.name


class Courses(AbstractDatesModel):
    name = models.CharField(_('İsim'), max_length=120)
    category = models.ForeignKey(CourseCategories, on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name=_('Kurs Kategorisi'))

    class Meta:
        db_table = 'courses'
        verbose_name = _('Kurs')
        verbose_name_plural = _('Kurslar')

    def __str__(self):
        return self.name


class Period(AbstractDatesModel):
    name = models.CharField(_('İsim'), max_length=120)

    class Meta:
        db_table = 'periods'
        verbose_name = _('Dönem')
        verbose_name_plural = _('Dönemler')

    def __str__(self):
        return self.name


class Classroom(AbstractDatesModel):
    name = models.CharField(_('İsim'), max_length=120)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='classrooms', verbose_name=_('Kurs'))
    period = models.ForeignKey(Period, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('Dönem'))
    instructor = models.ForeignKey(Users, on_delete=models.SET_NULL, related_name='instructor_classrooms', null=True,
                                   verbose_name=_('Eğitmen'), limit_choices_to={'groups__name': 'Eğitmen'})

    class Meta:
        db_table = 'classrooms'
        verbose_name = _('Sınıf')
        verbose_name_plural = _('Sınıflar')

    def __str__(self):
        return f'{self.period} {self.course.name} {self.name}'


class Videos(AbstractDatesModel):
    title = models.CharField(_('Başlık'), max_length=120)
    description = models.TextField(_('Açıklama'))
    video_file = models.FileField(_('Video'), upload_to='videos/', validators=[validate_file_extension])
    link = models.URLField(_('Link'), null=True, blank=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='videos', default=1,
                                  verbose_name=_('Sınıf'))
    instructor = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='instructor_videos', default=1,
                                   verbose_name=_('Eğitmen'), limit_choices_to={'groups__name': 'Eğitmen'})

    class Meta:
        db_table = 'videos'
        verbose_name = _('Video')
        verbose_name_plural = _('Videolar')

    def __str__(self):
        return self.title


class VideoComments(AbstractDatesModel):
    author = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='video_comments', verbose_name=_('Yazan'))
    video = models.ForeignKey(Videos, on_delete=models.CASCADE, related_name='comments', verbose_name=_('Video'))
    comment = models.TextField(_('Yorum'))

    class Meta:
        db_table = 'video_comments'
        verbose_name = _('Video Yorumu')
        verbose_name_plural = _('Video Yorumları')

    def __str__(self):
        return self.author.get_full_name()


class VideoFavorites(AbstractDatesModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='video_favorites',
                             verbose_name=_('Kullanıcı'))
    video = models.ForeignKey(Videos, on_delete=models.CASCADE, related_name='favorites', verbose_name=_('Video'))

    class Meta:
        db_table = 'video_favorites'
        verbose_name = _('Video Favorisi')
        verbose_name_plural = _('Video Favorileri')

    def __str__(self):
        return self.user.get_full_name()
