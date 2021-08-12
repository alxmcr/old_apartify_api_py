from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.name} {self.lastname}"

"""
Relationships

(1:N)
- Apartment - Photo (1 Apart -- has -> N Photo)
- Apartment - Flat (1 Apart -- has -> N Flat)
- City - Apartment (1 City -- has -> N Apartment)
- State - Apartment (1 State -- has -> N Apartment)
- Country - Apartment (1 Country -- has -> N Apartment)
- Neighborhood - Apartment (1 Neighborhood -- has -> N Apartment)
- Street - Apartment (1 Street -- has -> N Apartment)

(N:N)
* Apartment - Feature 
 - (1 Apart -- has -> N Feature)
 - (N Apart <- has -- 1 Feature)
 => (N:N - "ApartHasFeature")


* Apartment - Investment 
 - (1 Apart -- has -> N Investment)
 - (N Apart <- has -- 1 Investment)
 => (N:N - "ApartHasInvestment")
 
* Apartment - Pleasantness 
 - (1 Apart -- has -> N Pleasantness)
 - (N Apart <- has -- 1 Pleasantness)
 => (N:N - "ApartHasPleasantness")

"""

class Country(models.Model):
    co_country = models.BigAutoField(primary_key=True)
    co_name = models.CharField("Name", max_length=50, null=False)
    co_abbr = models.CharField("Abbreviation", max_length=5, null=False)
    co_url = models.CharField("URL Photo", max_length=80)
    co_alt = models.CharField("Photo Alternative Text", max_length=80)

    def __str__(self):
        return f"{self.co_country}. {self.co_name}"

class State(models.Model):
    st_state = models.BigAutoField(primary_key=True)
    st_name = models.CharField("Name", max_length=50, null=False)
    st_abbr = models.CharField("Abbreviation", max_length=5, null=False)
    st_url = models.CharField("URL Photo", max_length=80)
    st_alt = models.CharField("Photo Alternative Text", max_length=80)
    
    def __str__(self):
        return f"{self.st_state}. {self.st_name}"

class City(models.Model):
    ci_city = models.BigAutoField(primary_key=True)
    ci_name = models.CharField("Name", max_length=50, null=False)
    ci_abbr = models.CharField("Abbreviation", max_length=5, null=False)
    ci_url = models.CharField("URL Photo", max_length=80)
    ci_alt = models.CharField("Photo Alternative Text", max_length=80)

    def __str__(self):
        return f"{self.ci_city}. {self.ci_name}"

class Neighborhood(models.Model):
    ne_neighborhood = models.BigAutoField(primary_key=True)
    ne_name = models.CharField("Name", max_length=50, null=False)
    ne_abbr = models.CharField("Abbreviation", max_length=5, null=False)
    ne_url = models.CharField("URL Photo", max_length=80)
    ne_alt = models.CharField("Photo Alternative Text", max_length=80)

    def __str__(self):
        return f"{self.ne_neighborhood}. {self.ne_name}"

class Street(models.Model):
    st_street = models.BigAutoField(primary_key=True)
    st_name = models.CharField("Name", max_length=50, null=False)
    st_abbr = models.CharField("Abbreviation", max_length=5, null=False)
    st_url = models.CharField("URL Photo", max_length=80)
    st_alt = models.CharField("Photo Alternative Text", max_length=80)

    def __str__(self):
        return f"{self.st_street}. {self.st_name}"

class Feature(models.Model):
    fe_feature = models.BigAutoField(primary_key=True)
    fe_type = models.CharField("Type", max_length=50, null=False)
    fe_name = models.CharField("Name", max_length=50, null=False)
    fe_icon_url = models.CharField("URL Icon", max_length=80, null=False)
    fe_icon_color = models.CharField("Color Icon", max_length=80, null=False)
    fe_is_visible = models.BooleanField("Is it visible?", null=False, default=True)
    fe_is_card = models.BooleanField("Is it in a card?", null=False, default=True)

    def __str__(self):
        return f"{self.fe_feature}. {self.fe_type} - {self.fe_name}"

class Investment(models.Model):
    in_investment = models.BigAutoField(primary_key=True)
    in_type = models.CharField("Type", max_length=30, null=False)
    in_name = models.CharField("Name", max_length=30, null=False)
    in_icon_url = models.CharField("URL Icon", max_length=80, null=False)
    in_icon_color = models.CharField("Color Icon", max_length=80, null=False)
    in_is_visible = models.BooleanField("Is it visible?", null=False, default=True)
    in_is_card = models.BooleanField("Is it in a card?", null=False, default=True)

    def __str__(self):
        return f"{self.in_investment}. {self.in_type} - {self.in_name}"

class Pleasantness(models.Model):
    pl_pleasantness = models.BigAutoField(primary_key=True)
    pl_type = models.CharField("Type", max_length=30, null=False)
    pl_name = models.CharField("Name", max_length=30, null=False)
    pl_icon_url = models.CharField("URL Icon", max_length=80, null=False)
    pl_icon_color = models.CharField("Color Icon", max_length=80, null=False)
    pl_is_visible = models.BooleanField("Is it visible?", null=False, default=True)
    pl_is_card = models.BooleanField("Is it in a card?", null=False, default=True)

class Apartment(models.Model):
    ap_apartment = models.BigAutoField(primary_key=True)
    ap_descripcion = models.CharField("Description", max_length=50, null=False)
    ap_cost_offer = models.CharField("Offer Cost", max_length=50)
    ap_cost_list = models.CharField("List cost", max_length=50, null=False)
    ap_is_remodeling = models.BooleanField("Is it remodeling?", null=False)
    ap_latitude = models.DecimalField("Latitude", decimal_places=4, max_digits=4, null=False)
    ap_longitude = models.DecimalField("Longitude", decimal_places=4, max_digits=4, null=False)

    def __str__(self):
        return f"{self.ap_apartment}. {self.ap_descripcion}"

class Photo(models.Model):
    ph_photo = models.BigAutoField(primary_key=True)
    ph_url = models.CharField("URL Photo", max_length=80, null=False)
    ph_alt = models.CharField("Photo Alternative Text", max_length=80, null=False)

    def __str__(self):
        return f"{self.ph_photo}. {self.ph_url}"

class Flat(models.Model):
    fl_flat = models.BigAutoField(primary_key=True)
    fl_url = models.CharField("URL Flat", max_length=80, null=False)
    fl_alt = models.CharField("Flat Alternative Text", max_length=80, null=False)

    def __str__(self):
        return f"{self.fl_flat}. {self.fl_url}"