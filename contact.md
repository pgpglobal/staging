---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
class: contact
title: Contact
permalink: /contact/
---

<script src="{{ "/assets/js/jquery-3.4.1.min.js" | relative_url }}"></script>
<script type="text/javascript">var submitted=false;</script>
<script type="text/javascript">
$('#gform').on('submit', function(e) {
  $('#gform *').fadeOut(2000);
  $('#gform').prepend('Your submission has been processed...');
  });
</script>

<h2>Contact Us</h2>

<p>For questions or more information about the {{ site.title }}, please use the form below to contact us.</p>
<form name="gform" id="gform" enctype="text/plain" method="post" action="https://docs.google.com/forms/d/e/1FAIpQLSeAV6TIsbXg3dDpcEKiRfQH6eqqFRoFQl2ulQeerrppCRldRw/formResponse?" target="hidden_iframe" onsubmit="submitted=true;">
  <p>Your name:<br>
    <input class="span4" type="text" name="entry.1444497041" id="entry.1444497041"></p>

  <p>Your email:<br>
    <input class="span4" type="text" name="entry.1474335269" id="entry.1474335269"></p>

  <p>Subject:<br>
    <input class="span8" type="text" name="entry.1141066379" id="entry.1141066379"></p>

  <p>Message:<br>
    <textarea class="span8" name="entry.1316810993" id="entry.1316810993" rows="10" cols="50"></textarea></p>
  <p><input class="btn btn-primary btn-large" type="submit" value="Submit"></p>
</form>

<iframe name="hidden_iframe" id="hidden_iframe" style="display:none;" onload="if(submitted) {}"></iframe>

