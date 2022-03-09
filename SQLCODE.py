import os
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_sqlcode_table(sqlcode):
    link = 'https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_74/rzala/rzalaml.htm'
    html = urlopen(link).read()
    soup = BeautifulSoup(html, 'html.parser')
    sql_table = soup.find_all(id='messages__' + sqlcode)[-1]
    return str(sql_table)


def get_sqlcode_details(sqlcode):
    html = ''
    html += '<!DOCTYPE html><html>' \
            '<head><style>' \
            'table{' \
                'font-family: arial, sans-serif;' \
                'border-collapse: collapse;' \
                'margin: 25px 0;' \
                'width: 100%;' \
                'box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);' \
            '}' \
            'th,td{' \
                'padding: 12px;' \
                'text-align: left;' \
                'border-bottom: 1px solid #DDD;' \
                'word-wrap: break-word;' \
            '}' \
            'td:not(:first-child){' \
                'padding-top:20px;' \
                'padding-bottom:20px;' \
                'padding-right:20px;' \
            '}' \
            'tr:hover {' \
                'background-color: #dcfce5;' \
            '}' \
            '</style></head>'
    html += '<body>'
    if re.search('^SQL[0-9]{4}$', sqlcode.upper()):
        html += get_sqlcode_table(sqlcode.upper())
    else:
        html += '<b>Invalid SQL Code - ' + sqlcode.upper() + '</b><br><br>'
    html += '<i>Source: ' \
            '<a href="https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_74/rzala/rzalaml.htm#messages__' + \
            sqlcode.upper() + '">' \
            'https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_74/rzala/rzalaml.htm</a></i>'
    html += '</body></html>'
    return html


with open('sqlcode.html', 'w') as file:
    file.write(get_sqlcode_details('SQL0100'))
os.startfile('sqlcode.html')
