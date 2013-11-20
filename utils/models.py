from django.db import models

#https://github.com/tttallis/django-singletons/blob/master/singleton_models/models.py
class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.id = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass


class SingleValueSingleton(SingletonModel):
    valor = models.FloatField()

    class Meta:
        abstract = True

    def __unicode__(self):
        return u"%s" % self.valor

    @classmethod
    def getval(cls):
        try:
            return cls.objects.all()[0].valor
        except IndexError:
            return None

    @classmethod
    def getint(cls):
        try:
            return int(cls.getval())
        except:
            return None


class VisibleManager(models.Manager):
    def get_query_set(self):
        return super(VisibleManager, self).get_query_set().filter(visible=True)


class BaseModel(models.Model):
    visible = models.BooleanField(default=True)
    title = models.CharField('título', max_length=200)
    slug = models.SlugField('ruta')
    date = models.DateField('fecha')

    def __unicode__(self):
        return self.title

    def link(self):
        return "<a href='%s'>%s</a>" % (self.get_absolute_url(), self.__unicode__())

    class Meta:
        abstract = True
        ordering = ['-fecha']

    objects = models.Manager()
    visibles = VisibleManager()

    @models.permalink
    def get_absolute_url(self):
        viewname = self.__class__.__name__.lower()
        try:
            return ('%s' % viewname, [self.slug])
        except:
            return ('%s' % viewname, [str(self.id)])

