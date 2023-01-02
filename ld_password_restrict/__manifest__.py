{
    'name': "Restrict Password - [Sign Up / Reset Password]",
    'version': "14.0.0.1",
    'summary': """Put Restrictions during Signup / Reset from webpage - [Sign Up / Reset Password]""",
    'description': """This Module have the functionality by which user can control their password during
        Signup / Reset password.
        Password must following Pattern : 
            * Password must be 8 characters or more.
            * atleast 1 Numeric number
            * atleast 1 Alphabatic letter""",
    'author': "Livedigital Technologies Private Limited",
    'website': "ldtech.in",
    'category': 'Tools',
    "license": "LGPL-3",
    'depends': ['website','auth_signup'],
    'data': [
        'views/assets.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'live_test_url' : 'https://www.youtube.com/watch?v=Yra14IxmFY4'
}
