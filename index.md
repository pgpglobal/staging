---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: The Personal Genome Project
---

<div class="container">
  <div class="row lead-row">
    <div class="col-xs-8 col-md-9 lead-div">
      <a id="about" class="anchor-offset"></a>
      <h1 class="page-title">{{ page.title }}</h1>
      <p class="lead">
        The Personal&nbsp;Genome Project, initiated in 2005, is a vision
        and coalition of projects across the world dedicated to creating
        public genome, health, and trait data. Sharing data is critical
        to scientific progress, but has been hampered by traditional
        research practices. The PGP approach is to invite willing
        participants to publicly share their personal data
        for the greater good.
      </p>
    </div>
    <div class="col-xs-4 col-md-3 lead-div">
      <img class="logo" src="assets/images/pgp-logo.png">
    </div>
  </div>
  <div class="row lead-row">
    <div class="local-projects-wrap col-xs-12 col-md-9 lead-div">

      <div class="local-projects">
        <span class="local-projects-header">Local Projects</span>
        <h3>Harvard PGP (United States)</h3>
        <p>
          Founded in August 2005, the Harvard Personal Genome Project is
          the pilot PGP site, and is based in George Church's laboratory
          at Harvard Medical School.
        </p>
        <button class="btn btn-default"><a href="https://pgp.med.harvard.edu/">Go to the Harvard PGP website</a></button>

      </div>
    </div>
  </div>
  <hr>

  <div class="row">
    <a id="projects" class="anchor-offset"></a>

    <div class="col-xs-12">


      <h2>International Projects</h2>

      <p>
        The Global Network of Personal Genome Projects includes researchers
        at leading institutions around the globe:
      </p>

      <ul>
        {% assign sorted = site.projects | sort: 'order' %}
        {% for item in sorted %}
          <li>
            <h3>{{ item.title }} ({{ item.locale }})</h3>
            <p>{{ item.description }}</p>
            <button class="btn btn-default"><a href="{{ item.link }}">Go to the {{ item.title }} website</a></button>
          </li>
        {% endfor %}
      </ul>

    </div>
    <div class="col-xs-12">
      <a id="project-guidelines" class="anchor-offset"></a>

      <h3>Global Network Guidelines</h3>

      <p>
        Members of the Global Network of Personal Genome Projects adhere to
        the following guidelines:
      </p>

      <ol>
        <li>
          <p>
            <b>Public Data.</b> Participants are invited to publicly share
            their genomic and trait data in an integrated, publicly-accessible
            format using a CC0 waiver or equivalent public domain license.
          </p>
        </li>
        <li>
          <p>
            <b>Non-anonymous.</b> The risks of participant
            re-identification are addressed up front, as an integral part of
            the consent and enrollment process; neither anonymity nor
            confidentiality of participant identities or their data are
            promised to research participants.
          </p>
        </li>
        <li>
          <b>Equal access.</b> Participants are provided access to their
          individual research data in a timely and complete fashion (i.e.,
          raw data and not just summary results, where feasible).
        </li>
        <li>
          <b>Oversight.</b> Each member must at all times maintain
          current Institutional Review Board (IRB) approval or local
          equivalent, and will work with PersonalGenomes.org to continue to
          implement identified best practices for responsible public
          genomics research.
        </li>
        <li>
          <b>Not for profit.</b> The research project is managed or
          sponsored by a non-profit organization (or local equivalent). In
          addition, other than purposes of reasonable cost recovery, the
          member shall not sell or license participant data or tissues.
        </li>

      </ol></div> <!-- .col-xs-12 -->

    </div> <!-- /#projects .row -->

</div>
