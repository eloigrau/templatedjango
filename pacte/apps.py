from django.apps import AppConfig

class PacteConfig(AppConfig):
    name = 'pacte'

    def ready(self):
        from actstream import registry
        from django.contrib.auth.models import Group
        from fiches.models import Fiche, Atelier as fiche_at
        registry.register(self.get_model('Profil'))
        registry.register(self.get_model('MessageGeneral'))
        registry.register(self.get_model('Conversation'))
        registry.register(self.get_model('Suivis'))
        registry.register(Fiche)
        registry.register(fiche_at)
        registry.register(Group)
