page_template = '''\
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <title>Ontario Election 2018</title>
    <link rel="stylesheet" href="https://unpkg.com/tachyons@4.8.0/css/tachyons.min.css"/>
    <style type="text/css">
        $css
    </style>

</head>
    <body style="max-width: 800px;margin: auto;">
        $core
    </body>
</html
'''

core_template = '''\

{% macro show_post(item) %}
    <article class="pica-card pica-fade" style="margin-top: 18px;">
        {% if item['img_api'] != '' %}
        <div class="pica-card-image">
            <a class="pica-link" target="_blank" href="{{ item['link'] }}">
                <div class="pica-image-wrapper" style="">
                    <img class="pica-image" style="" src="{{ item['img_api'] }}">
                </div>
            </a>
        </div>
        {% endif %}
        <div class="pica-card-text">
            <a class="pica-link" target="_blank" href="{{ item['link'] }}">
                <h3 style="margin-top: 8px; margin-bottom: 6px; color: black; font-family: -apple-system, BlinkMacSystemFont, avenir, helvetica, ubuntu, roboto, noto, arial, sans-serif; font-weight: 500;" class="">{{ item['title_api']|safe|replace("WORLD CUP:", "") }}</h3>
                <p class=""><small style="color: grey;">{{ item['label_user']|safe if item['label_user'] else item['label_api']|safe }}</small></p>
            </a>
        </div>
    </article>
{% endmacro %}

<!-- STATIC HEADER -->
<h2>Upcoming matches</h2>
<p>All times Eastern</p>
<p><b>THURSDAY, JUNE 14</b></p>
<p>Russia vs. Saudi Arabia, 11 a.m.</p>
<p><b>FRIDAY, JUNE 15</b></p>
<p>Egypt vs. Uruguay, 8 a.m.</p>
<p>Morocco vs. Iran, 11 a.m.</p>
<p>Portugal vs. Spain, 2 p.m.</p>
<p><b>SATURDAY, JUNE 16</b></p>
<p>France vs. Australia, 6 a.m.</p>
<p>Argentina vs. Iceland, 10 a.m.</p>
<p>Peru vs. Denmark, 12 p.m.</p>
<p>Croatia vs. Nigeria, 3 p.m.</p>
<p><b>SUNDAY, JUNE 17</b></p>
<p>Costa Rica vs. Serbia, 8 a.m.</p>
<p>Germany vs. Mexico, 11 a.m.</p>
<p>Brazil vs. Switzerland, 2 p.m.</p>
<!-- END STATIC HEADER -->
<hr>
<!-- CURATION LIST -->
<section class="pica-cards">
    {%- for item in data['posts'] -%}
        {{ show_post(item) }}
    {%- endfor %}
</section>
<!-- END CURATION LIST -->
'''

script_template = '''\
var pica_add = (function() {
    var executed = false;
    return function() {
      if (!executed) {
        if (document.getElementById("pica-style") === null) {
            executed = true;
            var css = '$css',
              head = document.head || document.getElementsByTagName('head')[0],
              style = document.createElement('style');
            style.setAttribute('id', 'pica-style');
            style.type = 'text/css';
            if (style.styleSheet){
              style.styleSheet.cssText = css;
            } else {
              style.appendChild(document.createTextNode(css));
            }
            head.appendChild(style);
          }
        }
    };
})();
pica_add();
var html_string = '$minified';
var matches = document.querySelectorAll('div.pica-results');
for (var i=0; i<matches.length; i++)
    matches[i].innerHTML = html_string;
'''
