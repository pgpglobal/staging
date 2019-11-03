<div class="ArticleCopy language-"><sp-social-share></sp-social-share>

<div class="l-mt3 l-mh5--2col">

HTML5 introduces a couple of new attributes for implementing browser-based form validation. The `pattern` attribute is a regular-expression that defines the range of valid inputs for `textarea` elements and most types of `input`. The `required` attribute specifies whether a field is required. For legacy browsers that don’t implement these attributes, we can use their values as the basis of a polyfill. We can also use them to provide a more interesting enhancement – instant form validation.

We have to be very careful here not to get carried away, creating overly aggressive validation that breaks the natural browsing behavior and gets in people’s way. For example, I’ve seen forms where it’s impossible to <kbd>Tab</kbd> away from an invalid field – JavaScript is used (or rather _abused_) to force the focus to stay inside the field until it’s valid. This is very poor usability, and directly contravenes [accessibility guidelines](http://www.w3.org/TR/UNDERSTANDING-WCAG20/navigation-mechanisms-focus-order.html "Understanding Success Criterion 2.4.3: Focus Order (WCAG 2.0)").

What we’re going to do in this article is far less intrusive. It’s not even full client-side validation – it’s just a subtle usability enhancement, implemented in an accessible way, which (as I discovered while testing the script) is almost identical to something that Firefox now does natively!

## The Basic Concept

In recent versions of Firefox, if a `required` field is empty or its value doesn’t match the `pattern` then the field will show a red outline, as illustrated by the following figure.

![Invalid field indication in Firefox 16](./Instant Form Validation Using JavaScript_files/instant-validation-firefox.jpg)

This doesn’t happen straight away of course. If it did, then every required field would have that outline by default. Instead, these outlines are only shown **after** you’ve interacted with the field, which is basically (though not precisely) analogous to the `onchange` event.

So that’s what we’re going to do, using `onchange` as the triggering event. As an alternative, we could use the `oninput` event, which fires as soon as any value is typed or pasted into the field. But this is really _too_ instant, as it could easily be triggered on and off many types in rapid succession while typing, creating a flashing effect which would be annoying or impossibly distracting for some users. And, in any case, `oninput` doesn’t fire from programmatic input, which `onchange` does, and we might need that to handle things like auto-complete from third-party add-ons.

## Defining the HTML and CSS

So let’s have a look at our implementation, starting with the HTML it’s based on:

    <form action="#" method="post">
      <fieldset>

        <legend><strong>Add your comment</strong></legend>

        <p>
          <label for="author">Name <abbr title="Required">*</abbr></label>
          <input
            aria-required="true"
            id="author"
            name="author"
            pattern="^([- \w\d\u00c0-\u024f]+)$"
            required="required"
            size="20"
            spellcheck="false"
            title="Your name (no special characters, diacritics are okay)"
            type="text"
            value="">
        </p>

        <p>
          <label for="email">Email <abbr title="Required">*</abbr></label>
          <input
            aria-required="true"
            id="email"
            name="email"
            pattern="^(([-\w\d]+)(\.[-\w\d]+)*@([-\w\d]+)(\.[-\w\d]+)*(\.([a-zA-Z]{2,5}|[\d]{1,3})){1,2})$"
            required="required"
            size="30"
            spellcheck="false"
            title="Your email address"
            type="email"
            value="">
        </p>

        <p>
          <label for="website">Website</label>
          <input
            id="website"
            name="website"
            pattern="^(http[s]?:\/\/)?([-\w\d]+)(\.[-\w\d]+)*(\.([a-zA-Z]{2,5}|[\d]{1,3})){1,2}(\/([-~%\.\(\)\w\d]*\/*)*(#[-\w\d]+)?)?$"
            size="30"
            spellcheck="false"
            title="Your website address"
            type="url"
            value="">
        </p>

        <p>
          <label for="text">Comment <abbr title="Required">*</abbr></label>
          <textarea
            aria-required="true"
            cols="40"
            id="text"
            name="text"
            required="required"
            rows="10"
            spellcheck="true"
            title="Your comment"></textarea>
        </p>

      </fieldset>
      <fieldset>

        <button name="preview" type="submit">Preview</button>
        <button name="save" type="submit">Submit Comment</button>

      </fieldset>
    </form>

This example is a simple comments form, in which some fields are required, some are validated, and some are both. The fields which have `required` also have `aria-required`, to provide fallback-semantics for assistive technologies that don’t understand the new `input` types.

The [ARIA specification](http://www.w3.org/TR/wai-aria/) also defines an `aria-invalid` attribute, and that’s what we’re going to use to indicate when a field is invalid (for which there is no equivalent attribute in HTML5). The `aria-invalid` attribute obviously provides accessible information, but it can be also used as a CSS hook to apply the red outline:

    input[aria-invalid="true"], textarea[aria-invalid="true"] {
      border: 1px solid #f00;
      box-shadow: 0 0 4px 0 #f00;
    }

We could just use `box-shadow` and not bother with the `border`, and frankly that would look nicer, but then we’d have no indication in browsers that don’t support box-shadows, such as IE8.

## Adding the JavaScript

Now that we have the static code, we can add the scripting. The first thing we’ll need is a basic `addEvent()` function:

    function addEvent(node, type, callback) {
      if (node.addEventListener) {
        node.addEventListener(type, function(e) {
          callback(e, e.target);
        }, false);
      } else if (node.attachEvent) {
        node.attachEvent('on' + type, function(e) {
          callback(e, e.srcElement);
        });
      }
    }

Next, we’ll need a function for determining whether a given field should be validated, which simply tests that it’s neither disabled nor readonly, and that it has either a `pattern` or a `required` attribute:

    function shouldBeValidated(field) {
      return (
        !(field.getAttribute("readonly") || field.readonly) &&
        !(field.getAttribute("disabled") || field.disabled) &&
        (field.getAttribute("pattern") || field.getAttribute("required"))
      );
    }

The first two conditions may seem verbose, but they are necessary, because an element’s `disabled` and `readonly` properties don’t necessarily reflect its attribute states. In Opera, for example, a field with the hard-coded attribute `readonly="readonly"` will still return `undefined` for its `readonly` property (the dot property only matches states which are set through scripting).

Once we’ve got those utilities we can define the main validation function, which tests the field and then performs the actual validation, if applicable:

    function instantValidation(field) {
      if (shouldBeValidated(field)) {
        var invalid =
          (field.getAttribute("required") && !field.value) ||
          (field.getAttribute("pattern") &&
            field.value &&
            !new RegExp(field.getAttribute("pattern")).test(field.value));
        if (!invalid && field.getAttribute("aria-invalid")) {
          field.removeAttribute("aria-invalid");
        } else if (invalid && !field.getAttribute("aria-invalid")) {
          field.setAttribute("aria-invalid", "true");
        }
      }
    }

So a field is **invalid** if it’s required but doesn’t have a value, or it has a pattern and a value but the value doesn’t match the pattern.

Since the `pattern` already defines the string form of a regular-expression, all we have to do is pass that string to the `RegExp` constructor and that will create a regex object we can test against the value. But, we do have to _pre-test_ the value to make sure it isn’t empty, so that the regular expression itself doesn’t have to account for empty strings.

Once we’ve established whether a field is invalid, we can then control its `aria-invalid` attribute to indicate that state – adding it to an invalid field that doesn’t already have it, or removing it from a valid field that does. Simple! Finally, to put this all into action, we need to bind the validation function to an `onchange` event. It _should_ be as simple as this:

    addEvent(document, "change", function(e, target) {
      instantValidation(target);
    });

However for that to work, the `onchange` events **must bubble** (using a technique that’s usually known as [event delegation](https://www.sitepoint.com/event-bubbling-javascript/)), but in Internet Explorer 8 and earlier, `onchange` events _don’t bubble_. We could just choose to ignore those browsers, but I think that would be a shame, especially when the problem is so simple to workaround. It just means a bit more convoluted code – we have to get the collections of `input` and `textarea` elements, iterate through them and bind the `onchange` event to each field individually:

    var fields = [
      document.getElementsByTagName("input"),
      document.getElementsByTagName("textarea")
    ];
    for (var a = fields.length, i = 0; i < a; i++) {
      for (var b = fields[i].length, j = 0; j < b; j++) {
        addEvent(fields[i][j], "change", function(e, target) {
          instantValidation(target);
        });
      }
    }

## Conclusion and Beyond

So there we have it – a simple and non-intrusive enhancement for instant form validation, providing accessible and visual cues to help users complete forms. You can check out a demo below:

<div class="cp_embed_wrapper"><iframe name="cp_embed_1" src="./Instant Form Validation Using JavaScript_files/XgvNNe.html" scrolling="no" frameborder="0" height="400" allowtransparency="true" allowfullscreen="true" allowpaymentrequest="true" title="Instant Form Validation" class="cp_embed_iframe " style="width: 100%; overflow:hidden; display:block;" id="cp_embed_XgvNNe"></iframe></div>

Once that scripting is implemented, we’re actually only a couple of skips and hops away from a complete polyfill. Such a script is beyond the scope of this article, but if you wanted to develop it further, all of the basic blocks are there – testing whether a field should be validated, validating a field against a pattern and/or required, and binding trigger events.

I have to confess, I’m not sure it’s really worth it! If you already have this enhancement (which works in all modern browsers back to IE7), and given that you have _**no choice**_ but to implement server-side validation as well, and given that browsers which support `pattern` and `required` already use them for pre-submission validation – given all that, is there really any point adding another polyfill?

<div class="Article_authorBio l-mv4 t-bg-white m-border l-pa3">

<div class="l-d-f l-pt3">[![](./Instant Form Validation Using JavaScript_files/c0866060bbd63730723bc5036643f337.jpeg)](https://www.sitepoint.com/author/brothercake/)

<div class="f-lh-title">

<div class="f-c-grey-300">Meet the author</div>

<div class="f-large">[James Edwards](https://www.sitepoint.com/author/brothercake/)[](https://twitter.com/brothercake)</div>

</div>

</div>

<div class="f-light f-lh-copy l-mt3">James is a freelance web developer based in the UK, specialising in JavaScript application development and building accessible websites. With more than a decade's professional experience, he is a published author, a frequent blogger and speaker, and an outspoken advocate of standards-based development.</div>

</div>

</div>

</div>
