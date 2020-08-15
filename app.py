import streamlit as st

'# add color to your file list screenshots'

'## usage'

'paste the output of a **tree** command (`tree -L 2` for example) in the text field'

'add a comment and a color code to the end of the lines you wish to customize'

COLORS = [':gray', ':pink', ':teal']

f"color codes include {', '.join(f'`{color}`' for color in COLORS)}, or an hex code such as `#ff0071`"

'## paste and edit a file list'

file_list = st.text_area('paste a file list, add comments and color codes', '''\
.                                                                           :gray
├── .git                            # git                                   :gray
├── .gitignore                      # git                                   :gray
├── Procfile                        # Heroku                                :pink
├── README.md                       # GitHub                                :gray
├── __pycache__                     # python cache                          #63c470
├── app.py                          # app
├── requirements.txt                # python package                        :teal
├── setup.py                        # python package                        :teal
└── setup.sh                        # link between Heroku and Streamlit     :pink
''', height=300)

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

.file-list {{
    display: flex;
    width: 1000px;
}}
.file-list li {{
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
<div class="file-list">
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

'## bask in admiration to the result'

lines = []

for line in file_list.split('\n'):

    # determining line color
    class_color = 'none'
    hex_color = ''

    if line[-7:-6] == '#':
        hex_color = line[-7:]
        line = line[:-7]
    else:
        for color in COLORS:
            if line[-len(color):] == color:
                class_color = color[1:]
                line = line[:-len(color)]
                break

    lines.append({
            'line' : line,
            'class_color' : class_color,
            'hex_color' : hex_color
        })

# split file and description
files = []
descs = []

for line in lines:
    separator = line['line'].rfind('# ')

    if separator == -1:
        files.append(line)
        descs.append({
                'line' : '&nbsp;',
                'class_color' : 'none',
                'hex_color' : ''
            })
    else:
        files.append({
                'line' : line['line'][:separator].strip(),
                'class_color' : line['class_color'],
                'hex_color' : line['hex_color']
            })
        descs.append({
                'line' : line['line'][separator:].strip(),
                'class_color' : line['class_color'],
                'hex_color' : line['hex_color']
            })

content_file = ''.join([f'''<li><span class="{line['class_color']}" style="color: {line['hex_color']}">{line['line']}</span></li>''' for line in files])
content_desc = ''.join([f'''<li><span class="{line['class_color']}" style="color: {line['hex_color']}">{line['line']}</span></li>''' for line in descs])

html_content = f'''
</style>
<div class="file-list">
    <div class="file-col">
        <ul>
            {content_file}
        </ul>
    </div>
    <div class="desc-col">
        <ul>
            {content_desc}
        </ul>
    </div>
</div>
'''

st.write(html_content, unsafe_allow_html=True)
