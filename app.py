import streamlit as st

CONTENT = [{
        'file' :  '.',
        'desc' :  '&nbsp;',
        'color' : 'gray'
    },
    {
        'file' :  '├── .git</span>',
        'desc' :  '# git',
        'color' : 'gray'
    },
    {
        'file' :  '├── .gitignore</span>',
        'desc' :  '# git',
        'color' : 'gray'
    },
    {
        'file' :  '├── Procfile',
        'desc' :  '# Heroku',
        'color' : 'pink'
    },
    {
        'file' :  '├── README.md',
        'desc' :  '# GitHub',
        'color' : 'gray'
    },
    {
        'file' :  '├── __pycache__',
        'desc' :  '# python cache',
        'color' : 'gray'
    },
    {
        'file' :  '├── app.py',
        'desc' :  '# app',
        'color' : 'black'
    },
    {
        'file' :  '├── requirements.txt',
        'desc' :  '# python package',
        'color' : 'teal'
    },
    {
        'file' :  '├── setup.py',
        'desc' :  '# python package',
        'color' : 'teal'
    },
    {
        'file' :  '└── setup.sh',
        'desc' :  '# link between Heroku and Streamlit',
        'color' : 'pink'
    }]

CONTENT_FILE = ''.join([f'''<li><span class="{content['color']}">{content['file']}</span></li>''' for content in CONTENT])
CONTENT_DESC = ''.join([f'''<li><span class="{content['color']}">{content['desc']}</span></li>''' for content in CONTENT])

HTML = f'''
<style>

/* input */

.Widget.stTextArea {{
    width: 1000px !important;
}}

textarea {{
    font-family: monaco !important;
    font-size: 24px;
    box-sizing: border-box;
}}

/* output */

#file-list {{
    display: flex;
    width: 1000px;
}}
#file-list li {{
    font-family: monaco;
    font-size: 24px;
}}

li {{
    list-style: none;
}}

.desc-col {{
    margin-left: 100px;
}}

.gray {{
    color: #ccc;
}}

.pink {{
    color: #ff0071;
}}

.teal {{
    color: #017979;
}}

</style>
<div id="file-list">
    <div class="file-col">
        <ul>
            {CONTENT_FILE}
        </ul>
    </div>
    <div class="desc-col">
        <ul>
            {CONTENT_DESC}
        </ul>
    </div>
</div>
'''

st.write(HTML, unsafe_allow_html=True)
