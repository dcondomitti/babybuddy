/* Baby Buddy
 *
 * Default namespace for the Baby Buddy app.
 */
if (typeof jQuery === 'undefined') {
  throw new Error('Baby Buddy requires jQuery.')
}

var BabyBuddy = function () {
    var BabyBuddy = {};
    return BabyBuddy;
}();

/* Some dependencies (e.g. django-recurrence) require django.jQuery. */
var django = django || {};
django.jQuery = jQuery.noConflict(true);
