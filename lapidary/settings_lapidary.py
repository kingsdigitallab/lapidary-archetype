# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# PROJECT settings
# PLEASE DO NOT PLACE ANY SENSITIVE DATA HERE (password, keys, personal
# data, etc.)
# Use local_settings.py for that purpose

# Lightbox
"""
The Lightbox is a separate project, even though it's still tightly linked to Digipal. It is possible to install it through pip:
>>> pip install git+https://github.com/Gbuomprisco/Digital-Lightbox.git
By default, it is disabled. You can enable it by setting the variable LIGHTBOX in your settings:
"""
LIGHTBOX = True

# Mezzanine
SITE_TITLE = 'Lapidary Inscriptions'

# Social
"""
The following variables contains the URLs/username to social networking sites.
- The TWITTER variable asks for the Twitter username.
- The GITHUB variable asks for the relative URL to your Github project or account
- The COMMENTS_DISQUS_SHORTNAME asks for the Disqus shortname
"""
TWITTER = ''
GITHUB = ''
# COMMENTS_DISQUS_SHORTNAME = "exondomesday"

# Annotator Settings

"""
If True, this setting will reject every change to the DB. To be used in production websites.
"""
REJECT_HTTP_API_REQUESTS = False    # if True, prevents any change to the DB

"""
This setting allows to set the number of zoom levels available in the OpenLayers layer.
"""
ANNOTATOR_ZOOM_LEVELS = 7   # This setting sets the number of zoom levels of O

FOOTER_LOGO_LINE = True

# Customise the faceted search settings
MODELS_PRIVATE = ['textcontentxml', 'itempart', 'image', 'graph']
MODELS_PUBLIC = MODELS_PRIVATE


DEBUG_PERFORMANCE = False
COMPRESS_ENABLED = True
#COMPRESS_ENABLED = True

# from customisations.digipal.views.faceted_search.settings import FACETED_SEARCH

# CUSTOM_APPS = ['exon.customisations.mapping']

TEXT_IMAGE_MASTER_CONTENT_TYPE = 'transcription'
KDL_MAINTAINED = True

TEXT_EDITOR_OPTIONS_CUSTOM = {
    'buttons': {
        'btnPersonName': {'label': 'Person name', 'tei': '<rs type="person" subtype="name">{}</rs>'},
        'btnPerson': {'label': 'Person', 'buttons': ['btnPersonName', 'btnPersonMaritalStatus']},

        'btnPlaceName': {'label': 'Place name', 'tei': '<rs type="place" subtype="name">{}</rs>'},
        'btnPlace': {'label': 'Place', 'buttons': ['btnPlaceName', 'btnBirthPlace', 'btnResidence']},

        'btnDate': {'label': 'Date', 'tei': '<rs type="date">{}</rs>'},
    },
    'show_highlights_in_preview': 1,
    'toolbars': {
        'default': 'psclear undo redo pssave | btnPerson btnPlace btnDate | code ',
    },
    'panels': {
        'north': {
            'ratio': 0.5
        },
        'east': {
            'ratio': 0.5
        },
    }
}
