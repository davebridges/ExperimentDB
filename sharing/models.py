# -*- coding: utf-8 -*-

"""This package defines the database models for for the sharing application.

This application tracks shipments of constructs to other groups.

These tests include the following models:
- Institution
- Laboratory
- Recipient
- ConstructShipment

In the terms of this application, **ConstructShipments** are sent to **Recipients**, who are in **Laboratories** at **Institutions**.
"""

from django.db import models
from experimentdb.reagents.models import Construct
from experimentdb.external.models import Contact

INSTITUTE_TYPE = (
	('academic', 'Academic'),
	('pharmaceutical', 'Pharmaceutical'),
	)

# This Python file uses the following encoding: utf-8
# ISO 3166-1 country names and codes from http://opencountrycodes.appspot.com/python

COUNTRIES = (("AF", "Afghanistan"),("AX", "Åland Islands"),("AL", "Albania"),("DZ", "Algeria"),("AS", "American Samoa"),("AD", "Andorra"),("AO", "Angola"),("AI", "Anguilla"),("AQ", "Antarctica"),("AG", "Antigua and Barbuda"),("AR", "Argentina"),("AM", "Armenia"),("AW", "Aruba"),("AU", "Australia"),("AT", "Austria"),("AZ", "Azerbaijan"),("BS", "Bahamas"),("BH", "Bahrain"),("BD", "Bangladesh"),("BB", "Barbados"),("BY", "Belarus"),("BE", "Belgium"),("BZ", "Belize"),("BJ", "Benin"),("BM", "Bermuda"),("BT", "Bhutan"),("BO", "Bolivia, Plurinational State of"),("BA", "Bosnia and Herzegovina"),("BW", "Botswana"),("BV", "Bouvet Island"),("BR", "Brazil"),("IO", "British Indian Ocean Territory"),("BN", "Brunei Darussalam"),("BG", "Bulgaria"),("BF", "Burkina Faso"),("BI", "Burundi"),("KH", "Cambodia"),("CM", "Cameroon"),("CA", "Canada"),("CV", "Cape Verde"),("KY", "Cayman Islands"),("CF", "Central African Republic"),("TD", "Chad"),("CL", "Chile"),("CN", "China"),("CX", "Christmas Island"),("CC", "Cocos (Keeling) Islands"),("CO", "Colombia"),("KM", "Comoros"),("CG", "Congo"),("CD", "Congo, The Democratic Republic of the"),("CK", "Cook Islands"),("CR", "Costa Rica"),("CI", "Côte d'Ivoire"),("HR", "Croatia"),("CU", "Cuba"),("CY", "Cyprus"),("CZ", "Czech Republic"),("DK", "Denmark"),("DJ", "Djibouti"),("DM", "Dominica"),("DO", "Dominican Republic"),("EC", "Ecuador"),("EG", "Egypt"),("SV", "El Salvador"),("GQ", "Equatorial Guinea"),("ER", "Eritrea"),("EE", "Estonia"),("ET", "Ethiopia"),("FK", "Falkland Islands (Malvinas)"),("FO", "Faroe Islands"),("FJ", "Fiji"),("FI", "Finland"),("FR", "France"),("GF", "French Guiana"),("PF", "French Polynesia"),("TF", "French Southern Territories"),("GA", "Gabon"),("GM", "Gambia"),("GE", "Georgia"),("DE", "Germany"),("GH", "Ghana"),("GI", "Gibraltar"),("GR", "Greece"),("GL", "Greenland"),("GD", "Grenada"),("GP", "Guadeloupe"),("GU", "Guam"),("GT", "Guatemala"),("GG", "Guernsey"),("GN", "Guinea"),("GW", "Guinea-Bissau"),("GY", "Guyana"),("HT", "Haiti"),("HM", "Heard Island and McDonald Islands"),("VA", "Holy See (Vatican City State)"),("HN", "Honduras"),("HK", "Hong Kong"),("HU", "Hungary"),("IS", "Iceland"),("IN", "India"),("ID", "Indonesia"),("IR", "Iran, Islamic Republic of"),("IQ", "Iraq"),("IE", "Ireland"),("IM", "Isle of Man"),("IL", "Israel"),("IT", "Italy"),("JM", "Jamaica"),("JP", "Japan"),("JE", "Jersey"),("JO", "Jordan"),("KZ", "Kazakhstan"),("KE", "Kenya"),("KI", "Kiribati"),("KP", "Korea, Democratic People's Republic of"),("KR", "Korea, Republic of"),("KW", "Kuwait"),("KG", "Kyrgyzstan"),("LA", "Lao People's Democratic Republic"),("LV", "Latvia"),("LB", "Lebanon"),("LS", "Lesotho"),("LR", "Liberia"),("LY", "Libyan Arab Jamahiriya"),("LI", "Liechtenstein"),("LT", "Lithuania"),("LU", "Luxembourg"),("MO", "Macao"),("MK", "Macedonia, The Former Yugoslav Republic of"),("MG", "Madagascar"),("MW", "Malawi"),("MY", "Malaysia"),("MV", "Maldives"),("ML", "Mali"),("MT", "Malta"),("MH", "Marshall Islands"),("MQ", "Martinique"),("MR", "Mauritania"),("MU", "Mauritius"),("YT", "Mayotte"),("MX", "Mexico"),("FM", "Micronesia, Federated States of"),("MD", "Moldova, Republic of"),("MC", "Monaco"),("MN", "Mongolia"),("ME", "Montenegro"),("MS", "Montserrat"),("MA", "Morocco"),("MZ", "Mozambique"),("MM", "Myanmar"),("NA", "Namibia"),("NR", "Nauru"),("NP", "Nepal"),("NL", "Netherlands"),("AN", "Netherlands Antilles"),("NC", "New Caledonia"),("NZ", "New Zealand"),("NI", "Nicaragua"),("NE", "Niger"),("NG", "Nigeria"),("NU", "Niue"),("NF", "Norfolk Island"),("MP", "Northern Mariana Islands"),("NO", "Norway"),("OM", "Oman"),("PK", "Pakistan"),("PW", "Palau"),("PS", "Palestinian Territory, Occupied"),("PA", "Panama"),("PG", "Papua New Guinea"),("PY", "Paraguay"),("PE", "Peru"),("PH", "Philippines"),("PN", "Pitcairn"),("PL", "Poland"),("PT", "Portugal"),("PR", "Puerto Rico"),("QA", "Qatar"),("RE", "Réunion"),("RO", "Romania"),("RU", "Russian Federation"),("RW", "Rwanda"),("BL", "Saint Barthélemy"),("SH", "Saint Helena, Ascension and Tristan Da Cunha"),("KN", "Saint Kitts and Nevis"),("LC", "Saint Lucia"),("MF", "Saint Martin"),("PM", "Saint Pierre and Miquelon"),("VC", "Saint Vincent and the Grenadines"),("WS", "Samoa"),("SM", "San Marino"),("ST", "Sao Tome and Principe"),("SA", "Saudi Arabia"),("SN", "Senegal"),("RS", "Serbia"),("SC", "Seychelles"),("SL", "Sierra Leone"),("SG", "Singapore"),("SK", "Slovakia"),("SI", "Slovenia"),("SB", "Solomon Islands"),("SO", "Somalia"),("ZA", "South Africa"),("GS", "South Georgia and the South Sandwich Islands"),("ES", "Spain"),("LK", "Sri Lanka"),("SD", "Sudan"),("SR", "Suriname"),("SJ", "Svalbard and Jan Mayen"),("SZ", "Swaziland"),("SE", "Sweden"),("CH", "Switzerland"),("SY", "Syrian Arab Republic"),("TW", "Taiwan, Province of China"),("TJ", "Tajikistan"),("TZ", "Tanzania, United Republic of"),("TH", "Thailand"),("TL", "Timor-Leste"),("TG", "Togo"),("TK", "Tokelau"),("TO", "Tonga"),("TT", "Trinidad and Tobago"),("TN", "Tunisia"),("TR", "Turkey"),("TM", "Turkmenistan"),("TC", "Turks and Caicos Islands"),("TV", "Tuvalu"),("UG", "Uganda"),("UA", "Ukraine"),("AE", "United Arab Emirates"),("GB", "United Kingdom"),("US", "United States"),("UM", "United States Minor Outlying Islands"),("UY", "Uruguay"),("UZ", "Uzbekistan"),("VU", "Vanuatu"),("VE", "Venezuela, Bolivarian Republic of"),("VN", "Viet Nam"),("VG", "Virgin Islands, British"),("VI", "Virgin Islands, U.S."),("WF", "Wallis and Futuna"),("EH", "Western Sahara"),("YE", "Yemen"),("ZM", "Zambia"),("ZW", "Zimbabwe"),)

class Institution(models.Model):
    """This class defines Institution models.

    The only required is **institution**.
    The institution describes part of the address (city/state/country) the rest is defined under Laboratory.
    """
    institution = models.CharField(max_length=75)
    institution_type = models.CharField(max_length=25, blank=True, null=True, choices=INSTITUTE_TYPE)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=3, blank=True, null=True)
    country = models.CharField(max_length=30, choices=COUNTRIES, blank=True, null=True, default="US")

    def __unicode__(self):
        return u'%s' % self.institution

class Laboratory(models.Model):
    """This class describes groups or laboratories.

    This class has two required fields, **principal_investigator** and **institution**.
    In this context, a laboratory could be a single person or a group of people at an institution.
    Typically the recipient of the shipment works at the laboratory.
    The laboratory may or may not also be a contact, as defined in the external app.
    """
    principal_investigator = models.CharField(max_length=25, help_text="Last Name of PI", verbose_name="Principal Investigator")
    contact = models.ForeignKey(Contact, blank=True, null=True, help_text="If the laboratory is also a contact as defined in the external app")
    institution = models.ForeignKey(Institution)
    department = models.CharField(max_length=100, blank=True, null=True)
    address_line_1 = models.CharField(max_length=100, blank=True, null=True)
    address_line_2 = models.CharField(max_length=100, blank=True, null=True)
    address_line_3 = models.CharField(max_length=100, blank=True, null=True)
    postal_code=models.CharField(max_length=20, blank=True, null=True)

    def __unicode__(self):
        return u'%s Laboratory' % self.principal_investigator

    class Meta:
        verbose_name_plural = "Laboratories"		

	
class Recipient(models.Model):
    """This class describes the recipient of a shipment.

    The recipient could be the principal investigator, or a member of their group.
    The required fields for this model are **first_name**, **last_name** and **lab**.
    """
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    initials = models.CharField(max_length=25, blank=True, null=True)
    lab = models.ForeignKey(Laboratory)

    def __unicode__(self):
        return u'%s %s (%s)' %(self.first_name, self.last_name, self.lab)
		
class ConstructShipment(models.Model):
    """This class describes a shipment of constructs.

    The required fields are **constructs**, **ship_date**, **recipient** (who is defined as part of a Laboratory and in turn an Institution).
    """
    constructs = models.ManyToManyField(Construct)
    ship_date = models.DateField()
    recieved_date = models.DateField(blank=True, null=True)
    recipient = models.ForeignKey(Recipient)
    notes = models.TextField(max_length=500, blank=True, null=True, help_text="Paste in the request details here.")

    def __unicode__(self):
        return u'%s (%s)' % (self.recipient.lab, self.ship_date)

    def get_absolute_url(self):
        return '/experimentdb/shipment/%i' % self.id

    @models.permalink
    def get_absolute_url(self):
        return ("shipment-detail", [str(self.id)])

    class Meta:
        ordering = ['-ship_date']

	

	
