page_template = '''\
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <title>World Cup curator</title>
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
                <h3 style="margin-top: 8px; margin-bottom: 6px; color: black; font-family: georgia, times, serif; font-weight: 500;" class="">{{ item['title_api']|safe|replace("WORLD CUP:", "") }}</h3>
                <p class=""><small style="color: grey;">{{ item['label_user']|safe if item['label_user'] else item['label_api']|safe }}</small></p>
            </a>
        </div>
    </article>
{% endmacro %}

<!-- STATIC HEADER -->

<!-- START TABS CONTROLS-->
<section pica-tabs-section>
<ul class="pica-tab-controls" style="" data-tab-block="1">
    <li class="pica-tab-control" data-tab="1" data-tab-default="yes">Next matches</li>
    <li class="pica-tab-control" data-tab="2">Previous</li>
    <li class="pica-tab-control" data-tab="3">Podcasts</li>
</ul>
<!-- START TABS PANELS-->
<div class="pica-tab-panels" data-tab-block="1">
    <div class="pica-tab-panel" data-tab="1">
        <p><small>All times Eastern</small></p>
        <div class="pica-tab-panel_items" style="display: flex; flex-wrap: wrap; margin: 0 -10px 0 -10px;">
            <div style="flex: 1; min-width: 240px; margin: 0 10px 0 10px; margin-bottom: 6px;">
                <h3 style="margin-top: 4px; margin-bottom: 2px;">MONDAY, JUNE 25</h3>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331509/#match-liveblog?cid=go_boxpreview">Saudi Arabia vs. Egypt, 8 a.m.</a></p>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331516/#match-liveblog?cid=go_boxpreview">Uruguay vs. Russia, 11 a.m.</a></p>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331500/#match-liveblog?cid=go_boxpreview">Iran vs. Portugal, 2 p.m.</a></p>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300340184/#match-liveblog?cid=go_boxpreview">Spain vs. Morocco, 2 p.m.</a></p>
            </div>
            <div style="flex: 1; min-width: 240px; margin: 0 10px 0 10px; margin-bottom: 6px;">
                <h3 style="margin-top: 4px; margin-bottom: 2px;">TUESDAY, JUNE 26</h3>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331506/#match-liveblog?cid=go_boxpreview">Australia vs. Peru, 10 a.m.</a></p>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331512/#match-liveblog?cid=go_boxpreview">Denmark vs. France, 10 a.m.</a></p>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331519/#match-liveblog?cid=go_boxpreview">Nigeria vs. Argentina, 2 p.m.</a></p>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331510/#match-liveblog?cid=go_boxpreview">Iceland vs. Croatia, 2 p.m.</a></p>
            </div>
            <div style="flex: 1; min-width: 240px; margin: 0 10px 0 10px; margin-bottom: 6px;">
                <h3 style="margin-top: 4px; margin-bottom: 2px;">WEDNESDAY, JUNE 27</h3>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331548/#match-liveblog?cid=go_boxpreview">Mexico vs. Sweden, 10 a.m.</a></p>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331532/#match-liveblog?cid=go_boxpreview">South Korea vs. Germany, 10 a.m.</a></p>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331534/#match-liveblog?cid=go_boxpreview">Switzerland vs. Costa Rica, 2 p.m.</a></p>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331521/#match-liveblog?cid=go_boxpreview">Serbia vs. Brazil, 2 p.m.</a></p>
            </div>
            <div style="flex: 1; min-width: 240px; margin: 0 10px 0 10px; margin-bottom: 6px;">
                <h3 style="margin-top: 4px; margin-bottom: 2px;">THURSDAY, JUNE 28</h3>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331553/#match-liveblog?cid=go_boxpreview">Senegal vs. Colombia, 10 a.m.</a></p>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331507/#match-liveblog?cid=go_boxpreview">Japan vs. Poland, 10 a.m.</a></p>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300340182/#match-liveblog?cid=go_boxpreview">England vs. Belgium, 2 p.m.</a></p>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331520/#match-liveblog?cid=go_boxpreview">Panama vs. Tunisia, 2 p.m.</a></p>
            </div>
        </div>
    </div>
    <div class="pica-tab-panel" data-tab="2">
        <div class="pica-tab-panel_items" style="display: flex; flex-wrap: wrap; margin: 0 -10px 0 -10px;">
            <div style="flex: 1; min-width: 240px; margin: 0 10px 0 10px; margin-bottom: 6px;">
                <h3 style="margin-top: 4px; margin-bottom: 2px;">SUNDAY, JUNE 24</h3>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331546/#match-liveblog?cid=go_boxpreview">England 6, Panama 1</a></p>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331505/#match-liveblog?cid=go_boxpreview">Japan 2, Senegal 2</a></p>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331508/#match-liveblog?cid=go_boxpreview">Colombia 3, Poland 0</a></p>
            </div>
            <div style="flex: 1; min-width: 240px; margin: 0 10px 0 10px; margin-bottom: 6px;">
                <h3 style="margin-top: 4px; margin-bottom: 2px;">SATURDAY, JUNE 23</h3>
                <p>Belgium 5, Tunisia 2</p>
                <p>Mexico 2, South Korea 1</p>
                <p>Germany 2, Sweden 1</p>
            </div>        
            <div style="flex: 1; min-width: 240px; margin: 0 10px 0 10px; margin-bottom: 6px;">
                <h3 style="margin-top: 4px; margin-bottom: 2px;">FRIDAY, JUNE 22</h3>
                <p>Brazil 2, Costa Rica 0</p>
                <p>Nigeria 2, Iceland 0</p>
                <p>Switzerland 2, Serbia 1</p>
            </div>
            <div style="flex: 1; min-width: 240px; margin: 0 10px 0 10px; margin-bottom: 6px;">
                <h3 style="margin-top: 4px; margin-bottom: 2px;">THURSDAY, JUNE 21</h3>
                <p>Denmark 1, Australia 1</p>
                <p>France 1, Peru 0</p>
                <p>Croatia 3, Argentina 0</p>
            </div>
            <div style="flex: 1; min-width: 240px; margin: 0 10px 0 10px; margin-bottom: 6px;">
                <h3 style="margin-top: 4px; margin-bottom: 2px;">WEDNESDAY, JUNE 20</h3>
                <p>Portugal 1, Morroco 0</p>
                <p>Uruguay 1, Saudi Arabia 0</p>
                <p>Spain 1, Iran 0</p>
            </div>
            <div style="flex: 1; min-width: 240px; margin: 0 10px 0 10px; margin-bottom: 6px;">
                <h3 style="margin-top: 4px; margin-bottom: 2px;">TUESDAY, JUNE 19</h3>
                <p>Colombia 1, Japan 2</p>
                <p>Poland 1, Senegal 2</p>
                <p>Russia 3, Egypt 1</p>
            </div>
            <div style="flex: 1; min-width: 240px; margin: 0 10px 0 10px; margin-bottom: 6px;">
                <h3 style="margin-top: 4px; margin-bottom: 2px;">MONDAY, JUNE 18</h3>
                <p>Sweden 1, South Korea 0</p>
                <p>Belgium 3, Panama 0</p>
                <p>Tunisa 1, England 2</p>
            </div>
            <div style="flex: 1; min-width: 240px; margin: 0 10px 0 10px; margin-bottom: 6px;">
                <h3 style="margin-top: 4px; margin-bottom: 2px;">SUNDAY, JUNE 17</h3>
                <p>Costa Rica 0, Serbia 1</p>
                <p>Germany 0, Mexico 1</p>
                <p>Brazil 1, Switzerland 1</p>
            </div>
            <div style="flex: 1; min-width: 240px; margin: 0 10px 0 10px; margin-bottom: 6px;">
                <h3 style="margin-top: 4px; margin-bottom: 2px;">SATURDAY, JUNE 16</h3>
                <p>France 2, Australia 1</p>
                <p>Argentina 1, Iceland 1</p>
                <p>Peru 0, Denmark 1</p>
                <p>Croatia 2, Nigeria 0</p>
            </div>
            <div style="flex: 1; min-width: 240px; margin: 0 10px 0 10px; margin-bottom: 6px;">
                <h3 style="margin-top: 4px; margin-bottom: 2px;">FRIDAY, JUNE 15</h3>
                <p>Egypt 0, Uruguay 1</p>
                <p>Morocco 0, Iran 1</p>
                <p>Portugal 3, Spain 3</p>
            </div>
            <div style="flex: 1; min-width: 240px; margin: 0 10px 0 10px; margin-bottom: 6px;">
                <h3 style="margin-top: 4px; margin-bottom: 2px;">THURSDAY, JUNE 14</h3>
                <p>Russia 5, Saudi Arabia 0</p>
            </div>
        </div>
    </div>
    <div class="pica-tab-panel" data-tab="3">
        <iframe id="multi_iframe" frameborder="0" scrolling="no" allowfullscreen="" src="https://www.podbean.com/media/player/multi?playlist=http%3A%2F%2Fplaylist.podbean.com%2F759247%2Fplaylist_multi.xml&vjs=1&kdsowie31j4k1jlf913=2eb7c0cf1e0b2b2d7e13516349a49cb12aec6af8&size=240&share=1&fonts=Helvetica&auto=0&download=0&rtl=0&skin=3" width="100%" height="430"></iframe>
    </div>
</div>
</section>
<!-- END TABS -->
<!-- END STATIC HEADER -->
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

function pica_tabs_handler(e){
  var tab_id = this.getAttribute('data-tab');
  var block_id = this.parentNode.getAttribute('data-tab-block');
  var panel_blocks = document.querySelectorAll('.pica-tab-panels[data-tab-block="' + block_id + '"] .pica-tab-panel');
  Array.prototype.forEach.call(panel_blocks, function(el, i){
     el.style.display = 'none'; 
  });
  var this_panel = document.querySelectorAll('.pica-tab-panels[data-tab-block="' + block_id + '"] .pica-tab-panel[data-tab="' + tab_id + '"]');
    Array.prototype.forEach.call(this_panel, function(el, i){
     el.style.display = 'block' 
  });
  var tab_controls = this.parentNode.querySelectorAll('li');
  Array.prototype.forEach.call(tab_controls, function(el, i){
    el.className = 'pica-tab-control';
  });
  this.className = 'pica-tab-control active';
}

var tab_controls = document.querySelectorAll('.pica-tab-control');
Array.prototype.forEach.call(tab_controls, function(el, i){
   el.addEventListener('click', pica_tabs_handler, false);
});
var defaults = document.querySelectorAll('li.pica-tab-control[data-tab-default="yes"]')
Array.prototype.forEach.call(defaults, function(el, i){
  el.click();
});

var ids_to_hide = ["div1702", "div1703", "div3404", "div3495"];
var selectors_to_hide = ["#div1195 div section", "#div1195 div p", "#div3472 div section", "#div3472 div p"];
var el;

for (item in ids_to_hide) {
  try {
    el = document.getElementById(ids_to_hide[item]);
    el.style.display = 'none';
  }
  catch(err) {
  }
}
for (item in selectors_to_hide) {
  try {
    el = document.querySelector(selectors_to_hide[item]);
    el.style.display = 'none';
  }
  catch(err) {
  }
}

'''
