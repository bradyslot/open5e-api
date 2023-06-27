from locust import HttpUser, task, between

class MyUser(HttpUser):
    @task
    def get_manifest(self):
        self.client.get("/v1/manifest/")

    @task
    def get_spells(self):
        self.client.get("/v1/spells/")

    @task
    def get_spelllist(self):
        self.client.get("/v1/spelllist/")

    @task
    def get_monsters(self):
        self.client.get("/v1/monsters/")

    @task
    def get_documents(self):
        self.client.get("/v1/documents/")

    @task
    def get_backgrounds(self):
        self.client.get("/v1/backgrounds/")

    @task
    def get_planes(self):
        self.client.get("/v1/planes/")

    @task
    def get_sections(self):
        self.client.get("/v1/sections/")

    @task
    def get_feats(self):
        self.client.get("/v1/feats/")

    @task
    def get_conditions(self):
        self.client.get("/v1/conditions/")

    @task
    def get_races(self):
        self.client.get("/v1/races/")

    @task
    def get_classes(self):
        self.client.get("/v1/classes/")

    @task
    def get_magicitems(self):
        self.client.get("/v1/magicitems/")

    @task
    def get_weapons(self):
        self.client.get("/v1/weapons/")

    @task
    def get_armor(self):
        self.client.get("/v1/armor/")

    @task
    def get_search(self):
        self.client.get("/v1/search/")
