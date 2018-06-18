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

<!-- START TABS CONTROLS-->
<section pica-tabs-section>
<ul class="pica-tabs" style="margin-bottom: 12px;">
	<li><a href="javascript:SwitchTab(\\\'tb_1\\\', \\\'content_1\\\');" class="tb_1 tabmenu active">Next</a></li>
	<li><a href="javascript:SwitchTab(\\\'tb_2\\\', \\\'content_2\\\');" class="tb_2 tabmenu">Past</a></li>
    <li><a href="javascript:SwitchTab(\\\'tb_3\\\', \\\'content_3\\\');" class="tb_3 tabmenu">Podcasts</a></li>
</ul>
<!-- START TABS PANELS-->
<div class="pica-tab-sections content_1 tabcontent">
    <p><small>All times Eastern</small></p>
    <h3 style="margin-top: 4px; margin-bottom: 2px;">SUNDAY, JUNE 17</h3>
    <p><a href="https://www.fifa.com/worldcup/matches/match/300331529/#match-liveblog">Costa Rica 0,  Serbia 1</a></p>
    <p><a href="https://www.fifa.com/worldcup/matches/match/300331502/#match-liveblog">Germany 0, Mexico 1</a></p>
    <p><a href="https://www.fifa.com/worldcup/matches/match/300331525/#match-liveblog">Brazil 1, Switzerland 1</a></p>
<h3 style="margin-top: 4px; margin-bottom: 2px;">MONDAY, JUNE 18</h3>
   <p><a href="https://www.fifa.com/worldcup/matches/match/300331499/#match-liveblog?cid=go_boxpreview">Sweden vs. South Korea, 8 a.m.</a></p>
   <p><a href="https://www.fifa.com/worldcup/matches/match/300331539/#match-liveblog?cid=go_boxpreview">Belgium vs. Panama, 11 a.m.</a></p>
   <p><a href="https://www.fifa.com/worldcup/matches/match/300331554/#match-liveblog?cid=go_boxpreview">Tunisa vs. England, 2 p.m.</a></p>
   <h3 style="margin-top: 4px; margin-bottom: 2px;">TUESDAY, JUNE 19</h3>
   <p><a href="https://www.fifa.com/worldcup/matches/match/300331550/#match-liveblog?cid=go_boxpreview">Colombia vs. Japan, 8 a.m.</a></p>
   <p><a href="https://www.fifa.com/worldcup/matches/match/300331545/#match-liveblog?cid=go_boxpreview">Poland vs. Senegal, 11 a.m.</a></p>
   <p><a href="https://www.fifa.com/worldcup/matches/match/300331495/#match-liveblog?cid=go_boxpreview">Russia vs. Egypt, 2 p.m.</a></p>
</div> 
<div class="pica-tab-sections content_2 tabcontent" style="display:none;">
<h3 style="margin-top: 4px; margin-bottom: 2px;">SATURDAY, JUNE 16</h3>
    <p>France 2, Australia 1</p>
    <p>Argentina 1, Iceland 1</p>
    <p>Peru 0, Denmark 1</p>
    <p>Croatia 2, Nigeria 0</p>
<h3 style="margin-top: 4px; margin-bottom: 2px;">FRIDAY, JUNE 15</h3>
    <p>Egypt 0, Uruguay 1</p>
    <p>Morocco 0, Iran 1</p>
    <p>Portugal 3, Spain 3</p>
<h3 style="margin-top: 4px; margin-bottom: 2px;">THURSDAY, JUNE 14</h3>
    <p>Russia 5, Saudi Arabia 0</p>
</div>
<div class="pica-tab-sections content_3 tabcontent" style="display:none;">
	<iframe src="https://www.podbean.com/media/player/e3dyn-933b16&?from=site&skin=1&fonts=Helvetica&auto=0&download=0&share=1&btn-skin=103" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>
    <iframe src="https://www.podbean.com/media/player/d3x7v-933b06&?from=site&skin=1&fonts=Helvetica&auto=0&download=0&share=1&btn-skin=103" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>
</div>
</section>
<!-- END TABS -->
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

function SwitchTab(pica_tab, pica_tab_content) {
	// first of all we get all tab content blocks (I think the best way to get them by class names)
	var x = document.getElementsByClassName("tabcontent");
	var i;
	for (i = 0; i < x.length; i++) {
		x[i].style.display = 'none'; // hide all tab content
	}
  
	var y = document.getElementsByClassName(pica_tab_content) 
    // display the content of the tab we need
    for (i = 0; i < y.length; i++) {
		y[i].style.display = 'block'; // hide all tab content
	}
 
	// now we get all tab menu items by class names (use the next code only if you need to highlight current tab)
	var z = document.getElementsByClassName("tabmenu");
	for (i = 0; i < z.length; i++) {
		z[i].className = 'tabmenu'; 
	}

    var q = document.getElementsByClassName(pica_tab)
    var name = pica_tab.toString() + " tabmenu active"
    for (i = 0; i < q.length; i++) {
        q[i].className = name; 
	}
}

'''
