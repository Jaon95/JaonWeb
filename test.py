import lxml.html


tree = lxml.html.fromstring("""
     <html>
        <body>
            <div class='content'>
                <table>
                    <tr>
                        <td>nihao:ddd</td>
                        <td>dafad</td>
                    </tr>
                     <tr>
                        <td>nihao:ddd</td>
                        <td>dafad</td>
                    </tr>                   
                </table>
            </div>
        </body>
     </html>
""")

elements = tree.cssselect('.content tr')
for item in elements:
    print(item.text_content())