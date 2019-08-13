---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
class: contact
title: Contact
permalink: /contact/
---

<h2>Contact Us</h2>

<p>For questions or more information about the {{ site.title }}, please use the form below to contact us.</p>
<form action="" method="post">
  <table class="table lead">
    <tr><td>Subject:</td>
      <td><input class="span8" type="text" name="subject"></td>
    </tr>
    <tr><td>Your email:</td>
      <td><input class="span4" type="text" name="sender_email"></td>
    </tr>
    <tr><td>Your name:</td>
      <td><input class="span4" type="text" name="sender_name"></td>
    </tr>
    <tr><td>Message:</td>
      <td><textarea class="span8" name="message" rows="10" cols="50"></textarea></td>
    </tr>
    <tr><td></td>
      <td>
  <input class="btn btn-primary btn-large" type="submit" value="Submit message">
      </td>
    </tr>
  </table>
</form>
